# type: ignore[arg-type]

from basic_ops.strings import Strings
import pytest

def test_vowel_remover():
    assert Strings.vowel_remover("education") == "dctn"
    assert Strings.vowel_remover() == ""
    with pytest.raises(TypeError): Strings.vowel_remover(12345)
    
def test_reverse_words():
    assert Strings.reverse_words("hello world") == "dlrow olleh"
    assert Strings.reverse_words("") == ""
    with pytest.raises(TypeError): Strings.reverse_words(12345)

def test_initials_extractor():
    assert Strings.initials_extractor("John Ronald Reuel Tolkien") == "JRRT"
    assert Strings.initials_extractor("") == ""
    with pytest.raises(TypeError): Strings.reverse_words(12345)

def test_duplicate_separator():
    assert Strings.duplicate_separator("abc") == "aabbcc"
    assert Strings.duplicate_separator("") == ""
    with pytest.raises(TypeError): Strings.duplicate_separator(12345)

def test_title_casing():
    assert Strings.title_casing("this is a test") == "This Is A Test"
    assert Strings.title_casing("") == ""
    with pytest.raises(AttributeError): Strings.title_casing(12345)

