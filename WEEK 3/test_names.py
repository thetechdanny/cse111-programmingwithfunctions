from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Kalu", "Daniel") == "Kalu; Daniel"
    assert make_full_name("Kalu", "Dan") == "Kalu; Dan"
    assert make_full_name("Kalu", "King-Daniel") == "Kalu; King-Daniel"

def test_extract_family_name():
    assert extract_family_name("Kalu; Daniel") == "Kalu"
    assert extract_family_name("Kalu; Dan") == "Kalu"
    assert extract_family_name("Kalu; King-Daniel") == "Kalu"

def test_extract_given_name():
    assert extract_given_name("Kalu; Daniel") == "Daniel"
    assert extract_given_name("Kalu; Dan") == "Dan"
    assert extract_given_name("Kalu; King-Daniel") == "King-Daniel"

pytest.main(["-v", "--tb=line", "-rN", __file__])