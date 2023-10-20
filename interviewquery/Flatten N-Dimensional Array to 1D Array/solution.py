def flatten_array(array):
    flattened = []
    for e in array:
        if isinstance(e, list):
            flattened.extend(flatten_array(e))
        else:
            flattened.append(e)
    return flattened
        