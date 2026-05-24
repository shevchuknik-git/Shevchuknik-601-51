def unpack_recursive(obj):
    def _gen(o):
        if isinstance(o, (list, tuple, set)):
            for item in o:
                yield from _gen(item)
        elif isinstance(o, dict):
            for k, v in o.items():
                yield from _gen(k)
                yield from _gen(v)
        else:
            yield o
    return list(_gen(obj))

def test_unpack_recursive():
    data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
    result = unpack_recursive(data)
    assert len(result) == 6
    assert set(result) == {None, 1, 2, 3, 'foo', 'bar'}

if __name__ == "__main__":
    print(unpack_recursive([None, [1, ({2, 3}, {'foo': 'bar'})]]))