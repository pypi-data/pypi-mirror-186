from pathlib import Path
from importlib.machinery import SourceFileLoader


def import_module(name:str):
    path = Path(__file__).parent.joinpath("methods").joinpath(f"{name}.py")
    fullname = str(path.name)
    if "." in fullname:
        fullname = fullname.split(".",1)[0]
    loader = SourceFileLoader(fullname=fullname,path=path)
    module = loader.load_module()
    return module

