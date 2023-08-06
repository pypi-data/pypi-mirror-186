def setattr(source, name, value):
    """set attribute."""
    import builtins

    builtins.setattr(source, name, value)
    return source


def getitem(source, index):
    """Get items from a array."""
    if type(index) in (int, float):
        index = [index]
    index = [int(i) for i in index]
    if isinstance(source, list):
        result = [source[i] for i in index]
    else:
        result = source[index]
    results = (result,)
    return results


def setitem(source, index, value):
    """Set items value for a array."""
    if type(index) in (int, float):
        index = [index]
    index = [int(i) for i in index]
    if isinstance(source, list):
        for i in index:
            source[i] = value[i]
    else:
        source[index] = value
    return source
