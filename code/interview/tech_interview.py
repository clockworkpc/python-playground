from typing import List, Tuple, Literal, Dict, Any
import unicodedata


class TechInterview:
    STRING_CHECKS = {
        "alpha": lambda c: c.isalpha(),
        "alnum": lambda c: c.isalnum(),
        "digit": lambda c: c.isdigit(),
        "decimal": lambda c: c.isdecimal(),
        "space": lambda c: c.isspace(),
        "upper": lambda c: c.isupper(),
        "lower": lambda c: c.islower(),
        "punctuation": lambda c: unicodedata.category(c) == "Po",
        "printable": lambda c: c.isprintable(),
    }

    def sanitize_strings(
        s: str, allowed_characters: List[str] = [], case_sensitive: bool = False
    ) -> str:
        if allowed_characters:
            checks = [TechInterview.STRING_CHECKS[name] for name in allowed_characters]
            clean_s = "".join(c for c in s if any(check(c) for check in checks))
        else:
            clean_s = s[:]

        if not case_sensitive:
            clean_s = clean_s.lower()

        return clean_s

    def are_anagrams(
        a: str,
        b: str,
        allowed_characters: List[str] = [],
        case_sensitive: bool = False,
    ) -> bool:

        clean_a = TechInterview.sanitize_strings(a, allowed_characters, case_sensitive)
        clean_b = TechInterview.sanitize_strings(b, allowed_characters, case_sensitive)

        if not clean_a or not clean_b:
            return False

        def count_chars(s: str) -> Dict:
            my_dict = {}
            for c in s:
                my_dict[c] = my_dict.get(c, 0) + 1
            return my_dict

        dict_a = count_chars(clean_a)
        dict_b = count_chars(clean_b)

        return dict_a == dict_b

    def first_non_repeating_character(
        a: str,
        case_sensitive: bool = False,
        allowed_characters: List[str] = [],
        mode: Literal["char", "index"] = "char",
    ) -> Literal[str, int, None]:

        clean_a = TechInterview.sanitize_strings(a, allowed_characters, case_sensitive)
        print(f"clean_a = {clean_a}")

        freq = {}

        for ch in clean_a:
            freq[ch] = freq.get(ch, 0) + 1

        for i, ch in enumerate(clean_a):
            if freq[ch] == 1:
                return i if mode == "index" else ch

        return None

    def reverse_string(
        a: str,
        encoding: Literal["ascii, utf-8"] = "ascii",
    ) -> str:

        if encoding == "ascii":
            utf8_bytes = a.encode("utf-8")
            my_string = utf8_bytes.decode("utf-8", errors="ignore")
        else:
            my_string = a

        return my_string[::-1]

    def rotate_array(
        a: List[Any],
        k: int,
        direction: Literal["right", "left"] = "right",
    ) -> List[Any]:

        if not a:
            return []

        if k > len(a):
            k = k - len(a)

        if direction == "right":
            ary2 = a[: (k * -1)]
            ary1 = [x for x in a if x not in ary2]
        else:
            ary1 = a[k:]
            ary2 = [x for x in a if x not in ary1]

        return ary1 + ary2

    def longest_unique_substring(
        a: str,
        return_type: Literal["length", "substring"] = "substring",
    ) -> str | int:

        if not a:
            return "" if return_type == "substring" else 0

        start = 0
        max_len = 0
        max_start = 0
        seen = {}

        for i, char in enumerate(a):
            if char in seen and seen[char] >= start:
                start = seen[char] + i
            seen[char] = i

            window_len = i - start + 1
            if window_len > max_len:
                max_len = window_len
                max_start = start

        if return_type == "length":
            return max_len
        else:
            return a[max_start : max_start + max_len]
