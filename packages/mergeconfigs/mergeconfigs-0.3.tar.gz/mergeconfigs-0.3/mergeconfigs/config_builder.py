from pathlib import Path
import re
import yaml
from yaml import Loader


VAR_REGEX = r"\${(\w+@[.\w]+)}"
ENVS_FNAME = "envs.yaml"


def _get_var(var_name, parent_vars):
    """var_name is in format file@variable"""
    try:
        in_file, var = var_name.split("@")
    except ValueError:
        raise Exception(f"Bad variable name {var_name}")

    if in_file not in parent_vars:
        raise Exception(f"No such file {in_file}: {list(parent_vars.keys())}")

    v = parent_vars.get(in_file)
    subkeys = var.split(".")
    while subkeys:
        k = subkeys.pop(0)
        try:
            v = v[k]
        except:
            raise Exception(f"Bad subkey {k} in {var}")

    return v

def _resolve_variables(val, content):
    if isinstance(val, list):
        return [_resolve_variables(e, content) for e in val]
    elif isinstance(val, dict):
        return {k:_resolve_variables(v, content) for k,v in val.items()}

    if not isinstance(val, str):
        return val

    try:
        val = re.sub(VAR_REGEX, lambda m: _get_var(m.groups()[0], content), val)
    except Exception as exc:
        print(f"Error on value {val}: {exc}")
        raise

    return val



def resolve_yaml(file: Path, workdir=Path("."), env=".", envs_ctx=None, parent_vars=None, callers=None):
    callers = callers or []
    parent_vars = parent_vars or {}

    if not file.is_file():
        file = workdir.joinpath("default").joinpath(file.name)

    try:
        env_ctx = envs_ctx[env]
    except KeyError:
        raise ValueError(f"Environment {env} is not defined ({envs_ctx=}")

    parent_env = env_ctx.get("fallback", "")
    parent_env_ctx = envs_ctx.get(parent_env, {"dirname":workdir.name})

    file_content = yaml.load(open(file.absolute()), Loader=Loader)

    file_vars = file_content.copy()
    parent_vars[file.stem] = file_vars

    lines = open(file.absolute()).readlines()

    for line in lines:
        line = line.replace("$$ENV$$", env_ctx.get("dirname", env))
        line = line.replace("$$PARENT_ENV$$", parent_env_ctx.get("dirname", parent_env))

        if line.startswith("#extends"):
            extends_yaml = line.split(" ")[1].strip()
            fpath = workdir.joinpath(extends_yaml)
            content = resolve_yaml(file=fpath, workdir=workdir, envs_ctx=envs_ctx, env=env, parent_vars=parent_vars, callers=callers+[file.stem])
            content.update(file_content)
            file_content = content

        elif line.startswith("#include"):
            include_yaml = line.split(" ")[1].strip()
            fpath = workdir.joinpath(include_yaml)
            if fpath.stem in callers:
                raise RecursionError(f"Circular import of {fpath.name} in {file.name}")
            content = resolve_yaml(file=fpath, workdir=workdir, envs_ctx=envs_ctx, env=env, parent_vars=parent_vars, callers=callers+[file.stem])
            file_content.update(content)

        elif line.startswith("#load"):
            load_yaml = line.split(" ")[1].strip()
            fpath = workdir.joinpath(load_yaml)
            if fpath.stem in callers:
                raise RecursionError(f"Circular import of {fpath.name} in {file.name}")
            content = resolve_yaml(file=fpath, workdir=workdir, envs_ctx=envs_ctx, env=env, parent_vars=parent_vars, callers=callers+[file.stem])
            parent_vars[fpath.stem] = content

    for k,v in file_content.items():
        file_content[k] = _resolve_variables(v, parent_vars)

    return file_content


def build_config(filename="config.yaml", workdir=Path("."), env="."):

    workdir = Path(workdir)
    file = workdir.joinpath(filename)
    envs_file = workdir.joinpath(ENVS_FNAME)

    envs_ctx = yaml.load(open(envs_file.absolute()), Loader=Loader)

    full_config_dict = resolve_yaml(
            file=file, 
            workdir=workdir, 
            env=env, 
            envs_ctx=envs_ctx
            )

    return full_config_dict
