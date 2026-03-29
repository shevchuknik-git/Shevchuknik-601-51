def unpack_recursive(obj):
    result = []

    if isinstance(obj, (list, tuple, set)):
        for item in obj:
            result.extend(unpack_recursive(item))
    elif isinstance(obj, dict):
        for key, value in obj.items():
            result.extend(unpack_recursive(key))
            result.extend(unpack_recursive(value))
    else:
        result.append(obj)
    return result

print(unpack_recursive([None, [1, ({2, 3}, {'foo': 'bar'})]]))