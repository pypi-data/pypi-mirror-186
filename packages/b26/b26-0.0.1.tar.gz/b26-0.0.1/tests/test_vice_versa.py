import b26

def test_vice_versa():
    for i in range(10_000):
        assert b26.decode(b26.encode(i)) == i
