#Setup frameworks
from importlib import import_module
from pkgutil import iter_modules as iterate_modules
from langchain_core.tools import StructuredTool

TOOL_REGISTERY = {}

def LoadTools():
    global TOOL_REGISTERY

    package_name = "tools"
    package_folder = import_module(package_name)

    active_tools = []

    for _, module_name, _ in iterate_modules(package_folder.__path__):
        module = import_module(f"{package_name}.{module_name}")

        for obj in vars(module).values():
            if isinstance(obj, StructuredTool):
                TOOL_REGISTERY[obj.name] = obj
                active_tools.append(obj)
    
    return active_tools

plugins_loaded = {"loaded": False}
enabled_tools = LoadTools()
plugins_loaded["loaded"] = True

def Execute_Tool_Function(func_name: str, func_args: dict):
    global TOOL_REGISTERY
    tool = TOOL_REGISTERY.get(func_name)
    return tool.invoke(func_args)




