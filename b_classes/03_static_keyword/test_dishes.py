import math

from dishes import Cup


def test_calc_volume():
    height = 4
    width = 3
    volume = Cup.calc_volume()
    assert volume == (height * (math.pi * (width/2)))
