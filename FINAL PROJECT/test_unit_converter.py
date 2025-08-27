from unit_converter import convert_unit
from pytest import approx
import pytest

def test_convert_length():
    assert convert_unit('meter', 'centimeter', 1) == approx(100, abs=0.001)
    assert convert_unit('meter', 'millimeter', 1) == approx(1000, abs=0.001)
    assert convert_unit('kilofermi', 'centifermi', 100) == approx(10000000, abs=0.001)
    assert convert_unit('parsec', 'hectoparsec', 2) == approx(0.020, abs=0.001)
    assert convert_unit('nautical_mile', 'kilonautical_mile', 100) == approx(0.100, abs=0.001)


def test_convert_mass():
    assert convert_unit('kilogram', 'gram', 2) == approx(2000, abs=0.001)
    assert convert_unit('kiloproton_mass', 'centiproton_mass', 2) == approx(200000, abs=0.001)
    assert convert_unit('carat', 'centicarat', 5) == approx(500, abs=0.001)
    assert convert_unit('kilometric_ton', 'millimetric_ton', 2) == approx(2000000, abs=0.001)
    assert convert_unit('gram', 'carat', 1) == approx(5, abs=0.001)


def test_convert_time():
    assert convert_unit('second', 'minute', 60) == approx(1, abs=0.001)
    assert convert_unit('year', 'week', 1) == approx(52.179, abs=0.001)
    assert convert_unit('week', 'second', 1) == approx(604800, abs=0.001)
    assert convert_unit('year', 'month', 1) == approx(12, abs=0.001)
    assert convert_unit('leap_year', 'day', 1) == approx(366, abs=0.001)
    
def test_convert_speed():
    assert convert_unit('kilometer/hour', 'meter/second', 36) == approx(10, abs=0.001)
    assert convert_unit('meter_per_second', 'kilometer_per_second', 1) == approx(0.001, abs=0.001)
    assert convert_unit('speed_of_light', 'kilometer_per_second', 1) == approx(299792.458, abs=0.001)
    assert convert_unit('knot', 'mile_per_hour', 1) == approx(1.151, abs=0.001)
    assert convert_unit('foot_per_second', 'knot', 1) == approx(0.592, abs=0.001)


pytest.main(["-v", "--tb=line", "-rN", __file__])   
