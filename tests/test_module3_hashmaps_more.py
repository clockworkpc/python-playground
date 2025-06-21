import pytest
from code.module3.hashmaps import Hashmaps

def test_get_value():
    assert Hashmaps.get_value({'a': 1}, 'a') == 1

def test_has_key():
    assert Hashmaps.has_key({'a': 1}, 'a') == True

def test_invert_dict():
    assert Hashmaps.invert_dict({'a': 1}) == {1: 'a'}

def test_merge_dicts():
    assert Hashmaps.merge_dicts({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}

def test_dict_keys():
    assert Hashmaps.dict_keys({'a': 1}) == ['a']
