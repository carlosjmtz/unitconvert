import pytest

from unitconvert.distance import miles_to_kilometers, kilometers_to_miles
from unitconvert.temperature import fahrenheit_to_celsius, celcius_to_fahrenheit
 

def test_fahrenheit_to_celsius():
    # some known results
    # temperature when F is 32 should be zero
    assert fahrenheit_to_celsius(32) == 0

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(1, 2)
        
def test_celcius_to_fahrenheit():
    # some known results
    # temperature when F is 32 should be zero
    assert celcius_to_fahrenheit(0) == 32

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        celcius_to_fahrenheit(1, 2)
        


def test_miles_to_kilometers():
    # some known results
    assert miles_to_kilometers(1) == 1.60934

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
         miles_to_kilometers(1, 2)
        
def test_kilometers_to_miles():
        # some known results
    assert kilometers_to_miles(1.60934) == 1

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
          kilometers_to_miles(1, 2)