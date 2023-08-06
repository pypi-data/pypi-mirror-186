
import sys
from typing import TypeVar,List,Union
from .utils.import_module import import_module

SETTINGS = {"rewrite":True}
KEYS = ["method_id","path"]

O = TypeVar("O")

isint = lambda __o:isinstance(__o,int)

class getlist(List[O]):

    def get(self,__key:Union[int,O],default=None):
        if isinstance(__key,int):
            result = self[__key]
        else:
            result = next((o for o in self if o == __key),default)
        return result


def run_method(method_id:str,path:str,settings:dict):
    module = import_module(method_id)
    method = getattr(module,"edit")
    result = method(path,settings)
    return result


def main():
    sysargs = getlist(sys.argv[1:])
    kwargs = {key:sysargs.get(i,None) for (i,key) in enumerate(KEYS)}
    kwargs["settings"] = SETTINGS
    run_method(**kwargs)

main()



