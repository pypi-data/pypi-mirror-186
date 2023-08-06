import types

def abstract(method: types.MethodType):
    return method.__code__.co_code == b'd\x00S\x00'