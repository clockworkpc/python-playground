# type: ignore[arg-type]

from code.module1.string_ops import StringOps
import pytest

def test_vowel_remover():
    assert StringOps.vowel_remover("education") == "dctn"
    assert StringOps.vowel_remover() == ""
    with pytest.raises(TypeError): StringOps.vowel_remover(12345)
    
def test_reverse_words():
    assert StringOps.reverse_words("hello world") == "dlrow olleh"
    assert StringOps.reverse_words("") == ""
    with pytest.raises(TypeError): StringOps.reverse_words(12345)

def test_initials_extractor():
    assert StringOps.initials_extractor("John Ronald Reuel Tolkien") == "JRRT"
    assert StringOps.initials_extractor("") == ""
    with pytest.raises(TypeError): StringOps.reverse_words(12345)

def test_duplicate_separator():
    assert StringOps.duplicate_separator("abc") == "aabbcc"
    assert StringOps.duplicate_separator("") == ""
    with pytest.raises(TypeError): StringOps.duplicate_separator(12345)

def test_title_casing():
    assert StringOps.title_casing("this is a test") == "This Is A Test"
    assert StringOps.title_casing("") == ""
    with pytest.raises(AttributeError): StringOps.title_casing(12345)

