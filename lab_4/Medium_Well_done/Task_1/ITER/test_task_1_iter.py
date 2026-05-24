def unpack_iterative(obj):
    result = []
    stack = [obj]
    s_pop, s_extend, s_append, r_append = stack.pop, stack.extend, stack.append, result.append
    
    while stack:
        current = s_pop()
        if isinstance(current, (list, tuple)):
            s_extend(reversed(current))
        elif isinstance(current, set):
            s_extend(current) 
        elif isinstance(current, dict):
            for key in reversed(current):
                s_append(current[key])
                s_append(key)
        else:
            r_append(current)
    return result

def test_unpack_iterative():
    data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
    result = unpack_iterative(data)
    assert len(result) == 6
    assert set(result) == {None, 1, 2, 3, 'foo', 'bar'}

if __name__ == "__main__":
    print(unpack_iterative([None, [1, ({2, 3}, {'foo': 'bar'})]]))