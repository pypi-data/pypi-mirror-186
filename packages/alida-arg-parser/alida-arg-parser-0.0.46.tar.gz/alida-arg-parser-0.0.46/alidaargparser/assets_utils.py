from alidaargparser import ArgumentParser
import sys

def replace_dashes(string):
    key = string.split("=")[0]
    value = string.replace(key, "")
    return "--" + key.replace("-", "_")[2:] + value


def get_asset_property(asset_name, property=None):
    
    to_find = "--" + asset_name.replace("-", "_")
    if property is not None:
        to_find = to_find + "." + property

    args = sys.argv[1:]

    # Replace all dashes in the mid of a word with underscores
    args = [replace_dashes(arg) for arg in args]
    
    for arg in args:
        if arg.split("=")[0] == to_find:
            return "=".join(arg.split("=")[1:])
            