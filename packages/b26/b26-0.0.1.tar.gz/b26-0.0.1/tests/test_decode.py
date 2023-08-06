import b26
import pytest

def test_simple():
    assert b26.decode("A") == 0
    assert b26.decode("B") == 1
    assert b26.decode("Z") == 25

def test_overflow():
    assert b26.decode("AA") == 26
    assert b26.decode("AB") == 27
    assert b26.decode("AZ") == 51
    assert b26.decode("ZA") == 676

def test_wrong_type():
    with pytest.raises(TypeError):
        b26.decode(65)

def test_wrong_char():
    with pytest.raises(b26.DecodeError):
        b26.decode("ABC1")
    
    with pytest.raises(b26.DecodeError):
        b26.decode("1")
