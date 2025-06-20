from base import Base

class StringOps(Base):
    def __init__(self, value: str):
        self.value = value

    @staticmethod
    @Base.safe_transform_string
    def vowel_remover(s: str) -> str:
        """Removes all vowels (a, e, i, o, u, y) from the input string."""
        vowels = set('aeiouy')
        return ''.join(ch for ch in s if ch.lower() not in vowels)

    @staticmethod
    @Base.safe_transform_string
    def reverse_words(s: str) -> str:
        """Reverses the entire string character by character."""
        chars = list(reversed(list(s)))
        return "".join(chars)

    @staticmethod
    @Base.safe_transform_string
    def initials_extractor(s: str) -> str:
        """Extracts the first letter of each word and concatenates them."""
        words = s.split()
        return "".join([word[0] for word in words])

    @staticmethod
    @Base.safe_transform_string
    def duplicate_separator(s: str) -> str:
        """Duplicates every character in the input string."""
        return ''.join([val + val for val in list(s)])

    @staticmethod
    @Base.safe_transform_string
    def title_casing(s: str) -> str:
        """Converts the string to title case (capitalizes each word)."""
        return s.title()

