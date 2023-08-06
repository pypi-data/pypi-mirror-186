__edit = lambda __lines:"\n".join(
    line.split("==",1)[0] for line in __lines if "==" in line and not line.startswith("#")
)
def edit(__path:str,settings:dict=None):
    with open(__path,"r") as lines:
        result = __edit(lines)
        lines.close()
    if settings is not None and isinstance(settings,dict):
        rewrite = settings.get("rewrite",False)
        if not isinstance(rewrite,bool):
            rewrite = False
        if rewrite:
            with open(__path,"w+") as file:
                file.write(result)
                file.close()
    return result