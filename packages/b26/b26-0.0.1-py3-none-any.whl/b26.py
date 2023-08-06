"""
Base 26 Encoder and Decoder.

A common example usage is alphabetical counting:
When 'Z' is reached, the next items will be 'AA',
'AB' and so on.
"""

from __future__ import annotations
import string as stringlib

class DecodeError(Exception):
    """
    Error that may occure during decoding.
    
    Attributes
    ----------
    message
        The error message.
    
    character
        An invalid character encountered
        while decoding.
    
    location
        The location of the invalid character.
    """
    def __init__(
        self,
        message: Optional[str] = None,
        character: Optional[str] = None,
        location: Optional[int] = None,
    ):
        self.message = message
        self.character = character
        self.location = location
        super().__init__(self.message)

class EncodeError(Exception):
    """
    Error that may occure during encoding.
    """

def decode(string: str) -> int:
    """
    Converts an alphabetical string into an integer.
    
    Parameters
    ----------
    string
        A string that only consists of ASCII letters to
        convert into an integer.
    """
    if not isinstance(string, str):
        raise TypeError(f"expected {str!r}, got {type(string)!r}")
    
    string = string.upper()
    
    length = len(string)
    integer = 0;
    
    for i, char in enumerate(string):
        if char not in stringlib.ascii_uppercase:
            raise DecodeError(
                f"character {char!r} at position {i} should be an uppercase ASCII letter.",
                character = char,
                location = i,
            )
        integer += (ord(char) - ord("A")) * (26 ** (length - i - 1))
        if i > 0:
            integer += 26 ** (length - i)
    
    return integer

def encode(integer: int) -> str:
    """
    Convert an integer into an alphabetical string.
    
    Parameters
    ----------
    integer
        A positive integer or 0 to convert into a
        string.
    
    Returns
    -------
    An uppercase alphabetical string.
    """
    if not isinstance(integer, int):
        raise TypeError(f"expected {int!r}, got {type(integer)!r}")
    
    if integer < 0:
        raise EncodeError(f"expected a positive integer or 0, got {integer}")
    
    string = ""
    initial = True
    
    while initial or integer > 0:
        if not initial:
            integer -= 1
        
        initial = False
        
        value = integer % 26
        string = chr(value + ord("A")) + string
        integer //= 26
    
    return string

