"""
Module of weather-related functions.
"""

def comfort_level(temperature):
    """
    Given temperature in degrees Celsius, returns an indication of comfort
    level as a string ("COLD", "OK" or "HOT").
    """
    if temperature <= 15.0:
        return "COLD"
    elif temperature > 25.0:
        return "HOT"
    else:
        return "OK"


def test_cold():
    assert comfort_level(15) == "COLD"

def test_hot():
    assert comfort_level(25.1) == "HOT"

def test_ok():
    assert comfort_level(15.1) == "OK"
    assert comfort_level(25) == "OK"

print(test_cold())
print(test_hot())
print(test_ok())