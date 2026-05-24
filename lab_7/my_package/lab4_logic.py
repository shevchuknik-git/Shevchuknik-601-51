def unpack_recursive(obj):
    """Рекурсивная распаковка вложенных структур данных."""
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

def unpack_iterative(obj):
    """Итеративная распаковка вложенных структур данных (через стек)."""
    result = []
    stack = [obj]
    
    while stack:
        current = stack.pop()
        
        if isinstance(current, (list, tuple)):
            stack.extend(reversed(current))
        elif isinstance(current, set):
            stack.extend(reversed(list(current)))
        elif isinstance(current, dict):
            for key, value in reversed(list(current.items())):
                stack.append(value)
                stack.append(key)
        else:
            result.append(current)
            
    return result