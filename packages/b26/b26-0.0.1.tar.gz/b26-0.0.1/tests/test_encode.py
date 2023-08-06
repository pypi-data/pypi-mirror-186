import b26
import pytest

def test_simple():
    assert b26.encode(0) == "A"
    assert b26.encode(1) == "B"
    assert b26.encode(25) == "Z"

def test_overflow():
    assert b26.encode(26) == "AA"
    assert b26.encode(27) == "AB"
    assert b26.encode(51) == "AZ"
    assert b26.encode(52) == "BA"
    assert b26.encode(676) == "ZA"

def test_wrong_type():
    with pytest.raises(TypeError):
        b26.encode("1")

def test_negative():
    with pytest.raises(b26.EncodeError):
        b26.encode(-1)
