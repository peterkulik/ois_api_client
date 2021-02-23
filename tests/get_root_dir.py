from pathlib import Path


def get_root_dir(pytestconfig) -> Path:
    return Path(pytestconfig.rootdir).parent if Path(pytestconfig.rootdir).name == 'tests' else Path(
        pytestconfig.rootdir)
