from base import Base

class Strings(Base):
    def __init__(self, value: str):
        self.value = value

    @staticmethod
    @Base.safe_transform_string
    def vowel_remover(s: str) -> str:
        vowels = set('aeiouy')
        return ''.join(ch for ch in s if ch.lower() not in vowels)

    @staticmethod
    @Base.safe_transform_string
    def reverse_words(s: str) -> str:
        chars = list(reversed(list(s)))
        return "".join(chars)

    @staticmethod
    @Base.safe_transform_string
    def initials_extractor(s: str) -> str:
        words = s.split()
        return "".join([word[0] for word in words])

    @staticmethod
    @Base.safe_transform_string
    def duplicate_separator(s: str) -> str:
        return ''.join([val + val for val in list(s)])

    @staticmethod
    @Base.safe_transform_string
    def title_casing(s: str) -> str:
        return s.title()

