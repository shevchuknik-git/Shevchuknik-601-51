def unpack_iterative(obj):
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

print(unpack_iterative([None, [1, ({2, 3}, {'foo': 'bar'})]]))