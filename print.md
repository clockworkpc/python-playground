### code/module1/array_ops.py

```python
   1: from base import Base
   2: from typing import List
   3: 
   4: class ArrayOps(Base):
   5:     def __init__(self, value: int):
   6:         self.value = value    
   7: 
   8:     @staticmethod
   9:     @Base.safe_transform_numeric
  10:     def array_doubler(nums: List[int]) -> List[int]:
  11:         """Return a new list where each element is doubled from the input list."""
  12:         return [val * 2 for val in nums]
  13: 
  14:     @staticmethod
  15:     @Base.safe_transform_numeric
  16:     def even_filter(nums: List[int]) -> List[int]:
  17:         """Return a list containing only even numbers from the input list."""
  18:         return [val for val in nums if val % 2 == 0]
  19: 
  20:     @staticmethod
  21:     @Base.safe_transform_numeric
  22:     def every_other_element(nums: List[int]) -> List[int]:
  23:         """Return every other element from the input list, starting with index 0."""
  24:         return [val for i, val in enumerate(nums) if i % 2 == 0]
  25: 
  26:     @staticmethod
  27:     @Base.safe_transform_numeric
  28:     def last_digit_extractor(nums: List[int]) -> List[int]:
  29:         """Extract and return the last digit of each number in the input list."""
  30:         return [abs(num) % 10 for num in nums]
  31: 
  32:     @staticmethod
  33:     @Base.safe_transform_numeric
  34:     def index_parity_mask(nums: List[int]) -> List[int]:
  35:         """Negate elements at even indices, leave odd-indexed elements unchanged."""
  36:         return [val * -1 if i % 2 == 0 else val for i, val in enumerate(nums)]
  37: 
```
<div style="page-break-after: always;"></div>

### code/module1/module1.py

```python
   1: from base import Base
   2: from typing import List
   3: 
   4: class Module1(Base):
   5:     @staticmethod
   6:     def concatenate_strings(a: str, b: str) -> str:
   7:         return f"{a} {b}"
   8: 
   9:     @staticmethod
  10:     def uppercase(a:str) -> str:
  11:         return a.upper()
  12: 
  13:     @staticmethod
  14:     def strip_whitespace(a: str) -> str:
  15:         return a.strip()
  16: 
  17:     @staticmethod
  18:     def find_substring(a: str, b: str) -> int:
  19:         return a.find(b)
  20: 
  21:     @staticmethod
  22:     def replace_substring(a: str, b: str, c: str) -> str:
  23:         return a.replace(b, c)
  24: 
  25:     @staticmethod
  26:     def add(a: int, b: int) -> int:
  27:         return a + b
  28: 
  29:     @staticmethod
  30:     def divide(a: int, b: int) -> float:
  31:         return a / b
  32: 
  33:     @staticmethod
  34:     def modulus(a: int, b: int) -> int:
  35:         return a % b
  36: 
  37:     @staticmethod
  38:     def add_floats(a: float, b: float) -> float:
  39:         return a + b
  40: 
  41:     @staticmethod
  42:     def power(a: int, b: int) -> int:
  43:         return a ** b
  44: 
  45:     @staticmethod
  46:     def append_to_list(a: list, b: int) -> list:
  47:         a.append(b)
  48:         return a
  49: 
  50:     @staticmethod
  51:     def extend_list(a: list, b: list) -> list:
  52:         return a + b
  53: 
  54:     @staticmethod
  55:     def pop_from_list(a: list) -> int:
  56:         return a.pop()
  57: 
  58:     @staticmethod
  59:     def remove_from_list(a: list, b: int) -> list:
  60:         a.remove(2)
  61:         return a
  62: 
  63:     @staticmethod
  64:     def sort_list(a: list) -> list:
  65:         a.sort(reverse=False)
  66:         return a
  67:     
  68:     @staticmethod
  69:     def reverse_list(a: list) -> list:
  70:         a.sort(reverse=True)
  71:         return a
  72: 
  73:     @staticmethod
  74:     def index_of_element(a: List[str], b: str) -> int:
  75:         return a.index(b)
  76: 
  77:     @staticmethod
  78:     def slice_list(a: List[int], start: int, length: int) -> List[int]:
  79:         return a[start:length]
  80: 
  81:     @staticmethod
  82:     def double_elements(a: List[int]) -> List[int]:
  83:         return [n * 2 for n in a]
  84: 
  85:     @staticmethod
  86:     def sum_list(a: List[int]) -> int:
  87:         return sum(a)
```
<div style="page-break-after: always;"></div>

### code/module1/number_ops.py

```python
   1: from base import Base
   2: from typing import List
   3: 
   4: class NumberOps(Base):
   5:     def __init__(self, value: int):
   6:         self.value = value    
   7: 
   8:     @staticmethod
   9:     @Base.safe_transform_numeric
  10:     def increment_by_index(nums: List[int]) -> List[int]:
  11:         """Adds the index to each corresponding element in the list."""
  12:         return [val + i for i, val in enumerate(nums)]
  13: 
  14:     @staticmethod
  15:     @Base.safe_transform_numeric
  16:     def modulo_alternator(nums: List[int]) -> List[int]:
  17:         """Converts each number to 0 or 1 by applying modulo 2 (even/odd check)."""
  18:         return [val % 2 for val in nums]
  19: 
  20:     @staticmethod
  21:     @Base.safe_transform_numeric
  22:     def running_total(nums: List[int]) -> List[int]:
  23:         """Returns a list where each element is the cumulative sum up to that point."""
  24:         total = 0
  25:         result = []
  26:         for val in nums:
  27:             total += val
  28:             result.append(total)
  29:         return result
  30: 
  31:     @staticmethod
  32:     @Base.safe_transform_numeric
  33:     def double_negatives(nums: List[int]) -> List[int]:
  34:         """Doubles each negative number in the list; leaves others unchanged."""
  35:         return [val * 2 if val < 0 else val for val in nums]
  36: 
  37:     @staticmethod
  38:     @Base.safe_transform_numeric
  39:     def absolute_shift(nums: List[int]) -> List[int]:
  40:         """Adds the absolute value of the previous element to each item (starting from the second)."""
  41:         new_nums = []
  42:         for i, val in enumerate(nums):
  43:             addend = abs(nums[i-1]) if i > 0 else 0
  44:             new_nums.append(val + addend)
  45:         return new_nums
  46: 
```
<div style="page-break-after: always;"></div>

### code/module1/string_ops.py

```python
   1: from base import Base
   2: 
   3: class StringOps(Base):
   4:     def __init__(self, value: str):
   5:         self.value = value
   6: 
   7:     @staticmethod
   8:     @Base.safe_transform_string
   9:     def vowel_remover(s: str) -> str:
  10:         """Removes all vowels (a, e, i, o, u, y) from the input string."""
  11:         vowels = set('aeiouy')
  12:         return ''.join(ch for ch in s if ch.lower() not in vowels)
  13: 
  14:     @staticmethod
  15:     @Base.safe_transform_string
  16:     def reverse_words(s: str) -> str:
  17:         """Reverses the entire string character by character."""
  18:         chars = list(reversed(list(s)))
  19:         return "".join(chars)
  20: 
  21:     @staticmethod
  22:     @Base.safe_transform_string
  23:     def initials_extractor(s: str) -> str:
  24:         """Extracts the first letter of each word and concatenates them."""
  25:         words = s.split()
  26:         return "".join([word[0] for word in words])
  27: 
  28:     @staticmethod
  29:     @Base.safe_transform_string
  30:     def duplicate_separator(s: str) -> str:
  31:         """Duplicates every character in the input string."""
  32:         return ''.join([val + val for val in list(s)])
  33: 
  34:     @staticmethod
  35:     @Base.safe_transform_string
  36:     def title_casing(s: str) -> str:
  37:         """Converts the string to title case (capitalizes each word)."""
  38:         return s.title()
  39: 
```
<div style="page-break-after: always;"></div>

### code/module2/array_ops.py

```python
   1: from base import Base
   2: from typing import List, Union, Any
   3: from itertools import chain
   4: import re
   5: 
   6: class ArrayOps(Base):
   7:     def __init__(self, value: int):
   8:         self.value = value    
   9: 
  10:     @staticmethod
  11:     def double_array(nums: List[int]) -> List[int]:
  12:         """Returns a new list where each integer is multiplied by 2."""
  13:         return [n * 2 for n in nums]
  14: 
  15:     @staticmethod
  16:     def reverse_array(data: Union[List[int], List[List[int]]]) -> List[int]:
  17:         """Reverses the order of elements in a 1D or 2D list."""
  18:         return data[::-1]
  19: 
  20:     @staticmethod
  21:     def concat_arrays(a: List[Any], b: List[Any]) -> List[Any]:
  22:         """Concatenates two lists into one."""
  23:         return a + b
  24: 
```
<div style="page-break-after: always;"></div>

### code/module2/module2.py

```python
   1: from typing import List
   2: 
   3: class Module2:
   4:     @staticmethod
   5:     def repeat_string(a: str, b: int) -> str:
   6:         return a * 3
   7: 
   8:     @staticmethod
   9:     def is_palindrome(a: str) -> bool:
  10:         return a == a[::-1]
  11: 
  12:     @staticmethod
  13:     def string_length(a: str) -> int:
  14:         return len(a)
  15: 
  16:     @staticmethod
  17:     def capitalize_words(words: str) -> str:
  18:         ary = [word.capitalize() for word in words.split()] 
  19:         return ' '.join(ary)
  20: 
  21:     @staticmethod
  22:     def join_with_dash(chars: List[str]) -> str:
  23:         return '-'.join(chars)
  24: 
  25:     @staticmethod
  26:     def multiply(a: int, b: int) -> int:
  27:         return a * b
  28: 
  29:     @staticmethod
  30:     def is_even(a: int) -> bool:
  31:         return a % 2 == 0
  32: 
  33:     @staticmethod
  34:     def floor_divide(a: int, b: int) -> int:
  35:         return a // b
  36: 
  37:     @staticmethod
  38:     def round_to_int(a: float) -> int:
  39:         return round(a)
  40: 
  41:     @staticmethod
  42:     def abs_value(a: int) -> int:
  43:         return abs(a)
  44: 
  45:     @staticmethod
  46:     def merge_lists(a: List[int], b: List[int]) -> List[int]:
  47:         return a + b
  48: 
  49:     @staticmethod
  50:     def list_difference(a: List[int], b: List[int]) -> List[int]:
  51:         return list(set(a) - set(b))
  52: 
  53:     @staticmethod
  54:     def list_intersection(a: List[int], b: List[int]) -> List[int]:
  55:         return list(set(a) & set(b))
  56: 
  57:     @staticmethod
  58:     def list_max(a: List[int]) -> int:
  59:         return max(a)
  60: 
  61:     @staticmethod
  62:     def list_min(a: List[int]) -> int:
  63:         return min(a)
  64: 
  65:     @staticmethod
  66:     def unique_elements(a: List[int]) -> List[int]:
  67:         return list(set(a))
  68: 
  69:     @staticmethod
  70:     def filter_even(nums: List[int]) -> List[int]:
  71:         return [num for num in nums if num % 2 == 0]
  72: 
  73:     @staticmethod
  74:     def count_occurrences(nums: List[int], e: int) -> int:
  75:         return len([num for num in nums if num == e])
  76: 
  77:     @staticmethod
  78:     def list_to_string(nums: List[int]) -> str:
  79:         return ','.join([str(num) for num in nums])
  80: 
  81:     @staticmethod
  82:     def list_length(a: List[int]) -> int:
  83:         return len(a)
  84: 
  85: 
```
<div style="page-break-after: always;"></div>

### code/module2/number_ops.py

```python
   1: from base import Base
   2: from typing import List
   3: from itertools import chain
   4: import re
   5: 
   6: class NumberOps(Base):
   7:     def __init__(self, value: int):
   8:         self.value = value    
   9: 
  10:     @staticmethod
  11:     @Base.safe_transform_binary_numeric
  12:     def add_numbers(a: int, b: int) -> int:
  13:         """Returns the sum of two integers."""
  14:         return a + b
  15: 
  16:     @staticmethod
  17:     @Base.safe_transform_unary_list
  18:     def split_digits(a: int) -> List[int]:
  19:         """Splits an integer into its individual digits and returns them as a list."""
  20:         return [int(digit) for digit in str(a)]
  21: from base import Base
```
<div style="page-break-after: always;"></div>

### code/module2/string_ops.py

```python
   1: from base import Base
   2: from typing import List
   3: from itertools import chain
   4: import re
   5: 
   6: class StringOps(Base):
   7:     def __init__(self, value: int):
   8:         self.value = value    
   9: 
  10:     @staticmethod
  11:     @Base.safe_transform_multiple_strings
  12:     def split_words(*args: str) -> List[str]:
  13:         if len(args) == 1:
  14:             return args[0].split()
  15:         else:
  16:             clean = lambda x: re.sub(r'[^A-Za-z0-9]', '', x)
  17:             cleaned = [clean(s) for s in args if s]
  18:             return list(chain.from_iterable(cleaned))
  19:     
  20:     @staticmethod
  21:     def compare_strings(a: str, b:str) -> bool:
  22:         return a == b
  23: 
  24:     @staticmethod
  25:     def concat_strings(a: str, b: str) -> str:
  26:         return a + b
  27:     
  28:     @staticmethod
  29:     def reverse_string(a: str) -> str:
  30:         return a[::-1]
  31: 
  32: 
```
<div style="page-break-after: always;"></div>

### code/module3/array_merging.py

```python
   1: from base import Base
   2: from typing import List, Union, Any, Optional
   3: from itertools import chain
   4: import re
   5: 
   6: class ArrayMerging(Base):
   7:     @staticmethod
   8:     def merge_sorted_arrays(a: List[int], b: List[int]) -> List[int]:
   9:         """Merge two sorted arrays."""
  10:         i, j = 0, 0
  11:         merged = []
  12:         while i < len(a) and j < len(b):
  13:             if a[i] < b[j]:
  14:                 merged.append(a[i])
  15:                 i += 1
  16:             else:
  17:                 merged.append(b[j])
  18:                 j += 1
  19:         merged.extend(a[i:])
  20:         merged.extend(b[j:])
  21:         return merged
  22: 
  23:     @staticmethod
  24:     def interleave_arrays(a: List[int], b: List[int]) -> List[int]:
  25:         """Interleave two arrays element by element."""
  26:         zipped_pairs = list(zip(a, b))
  27:         merged = [item for pair in zipped_pairs for item in pair]
  28:         merged.extend(a[len(b):])
  29:         merged.extend(b[len(a):])
  30:         return merged
```
<div style="page-break-after: always;"></div>

### code/module3/composed_list_ops.py

```python
   1: from base import Base
   2: from code.module3.list_ops import ListOps
   3: from typing import List, Union, Any, Optional
   4: from itertools import chain
   5: import re
   6: 
   7: class ComposedListOps(Base):
   8:     @staticmethod
   9:     def process_and_filter(nums: List[int]) -> List[int]:
  10:         """Filter even numbers and then double each of them."""
  11:         filtered = ListOps.filter_evens(nums)
  12:         return ListOps.double_normal(filtered)
  13: 
  14:     @staticmethod
  15:     def filter_and_square_evens(nums: List[int]) -> List[int]:
  16:         """Filter even numbers and then square each of them."""
  17:         filtered = ListOps.filter_evens(nums)
  18:         return ListOps.square_return(filtered)
```
<div style="page-break-after: always;"></div>

### code/module3/hashmaps.py

```python
   1: from base import Base
   2: from typing import List, Dict
   3: from collections import Counter
   4: 
   5: class Hashmaps(Base):
   6:     def __init__(self, value: str):
   7:         self.value = value
   8: 
   9:     @staticmethod
  10:     def count_frequencies(items: List[str]) -> Dict[str, int]:
  11:         """Counts how many times each string appears in the input list and returns a frequency dictionary."""
  12:         return dict(Counter(items))
  13: 
  14:     @staticmethod
  15:     def invert_dict(d: Dict[str, str]) -> Dict[str, str]:
  16:         """Inverts the keys and values of the input dictionary (assumes values are unique)."""
  17:         inverted_dict = {}
  18:         for k, v in d.items():
  19:             inverted_dict[v] = k
  20:         return inverted_dict
  21:     
  22:     @staticmethod
  23:     def get_value(hash: dict, key: str) -> int:
  24:         return hash[key]
  25: 
  26:     @staticmethod
  27:     def has_key(d: dict, key: str) -> bool:
  28:         return key in d.keys()
  29:     
  30:     @staticmethod
  31:     def merge_dicts(a: dict, b: dict) -> dict:
  32:         for k,v in b.items():
  33:             a[k] = v
  34:         return a
  35: 
  36:     @staticmethod
  37:     def dict_keys(d: dict) -> List[str]:
  38:         return list(d.keys())
  39: 
  40: 
```
<div style="page-break-after: always;"></div>

### code/module3/list_ops.py

```python
   1: from base import Base
   2: from typing import List, Union, Any, Optional
   3: from itertools import chain
   4: import re
   5: 
   6: class ListOps(Base):
   7:     @staticmethod
   8:     def filter_evens(nums: List[int]) -> List[int]:
   9:         """Keep only even numbers."""
  10:         return [n for n in nums if n % 2 == 0]
  11: 
  12:     @staticmethod
  13:     def double_normal(nums: List[int]) -> List[int]:
  14:         """Double all non-zero values."""
  15:         return [n * 2 for n in nums if n]
  16: 
  17:     @staticmethod
  18:     def square_return(nums: List[int]) -> List[int]:
  19:         """Square all non-zero values."""
  20:         return [n * n for n in nums if n]
```
<div style="page-break-after: always;"></div>

### code/module3/matrix_ops.py

```python
   1: from base import Base
   2: from typing import List, Union, Any, Optional
   3: from itertools import chain
   4: import re
   5: 
   6: class MatrixOps(Base):
   7:     def __init__(self, value: str):
   8:         self.value = value
   9: 
  10:     _rotation_registry = {}
  11: 
  12:     @staticmethod
  13:     @Base.enforce_types
  14:     def sum_nested_matrix(matrix: List[List[int]]) -> int:
  15:         return sum(sum(row) for row in matrix)
  16: 
  17:     @staticmethod
  18:     def flatten_2d(matrix: List[List[int]]) -> List[int]:
  19:         ary = []
  20:         for row in matrix:
  21:             for cell in row:
  22:                 ary.append(cell)
  23:         return ary
  24:     
  25:     @staticmethod
  26:     def flatten_2d(matrix: List[List[int]]) -> List[int]:
  27:         return [cell for row in matrix for cell in row]
  28: 
  29:     @staticmethod
  30:     def transpose(matrix: List[List[int]]) -> List[List[int]]:
  31:         return list(map(list, zip(*matrix)))
  32: 
  33: 
```
<div style="page-break-after: always;"></div>

### code/module3/rotate_matrix.py

```python
   1: from base import Base
   2: from typing import List, Union, Any, Optional
   3: from itertools import chain
   4: import re
   5: 
   6: # Internal registry to map rotation methods by name
   7: _rotation_registry = {}
   8: 
   9: # Decorator to register rotation methods in the internal registry
  10: def register_rotation(name):
  11:     def decorator(fn):
  12:         _rotation_registry[name] = fn
  13:         return fn
  14:     return decorator
  15: 
  16: class RotateMatrix(Base):
  17:     def __init__(self, value: str):
  18:         self.value = value
  19: 
  20:     # Rotate 90° clockwise: transpose and then reverse each row
  21:     @staticmethod
  22:     @register_rotation("rotate_90_clockwise")
  23:     def rotate_90_clockwise(matrix: List[List[int]]) -> List[List[int]]:
  24:         return [list(reversed(col)) for col in zip(*matrix)]
  25: 
  26:     # Rotate 90° anticlockwise: reverse rows, then transpose
  27:     @staticmethod
  28:     @register_rotation("rotate_90_anticlockwise")
  29:     def rotate_90_anticlockwise(matrix: List[List[int]]) -> List[List[int]]:
  30:         return [list(col) for col in zip(*reversed(matrix))]
  31: 
  32:     # Rotate 180° clockwise (same as 180° anticlockwise): reverse both rows and columns
  33:     @staticmethod
  34:     @register_rotation("rotate_180_clockwise")
  35:     def rotate_180_clockwise(matrix: List[List[int]]) -> List[List[int]]:
  36:         return [row[::-1] for row in matrix[::-1]]
  37: 
  38:     # Rotate 180° anticlockwise reuses the clockwise method
  39:     @staticmethod
  40:     @register_rotation("rotate_180_anticlockwise")
  41:     def rotate_180_anticlockwise(matrix: List[List[int]]) -> List[List[int]]:
  42:         return Matrices.rotate_180_clockwise(matrix)  # Fixed: was incorrectly referencing Arrays
  43: 
  44:     # Rotate 270° clockwise is same as 90° anticlockwise
  45:     @staticmethod
  46:     @register_rotation("rotate_270_clockwise")
  47:     def rotate_270_clockwise(matrix: List[List[int]]) -> List[List[int]]:
  48:         return Matrices.rotate_90_anticlockwise(matrix)  # Fixed: was incorrectly referencing Arrays
  49: 
  50:     # Rotate 270° anticlockwise is same as 90° clockwise
  51:     @staticmethod
  52:     @register_rotation("rotate_270_anticlockwise")
  53:     def rotate_270_anticlockwise(matrix: List[List[int]]) -> List[List[int]]:
  54:         return Matrices.rotate_90_clockwise(matrix)  # Fixed: was incorrectly referencing Arrays
  55: 
  56:     # General-purpose rotation dispatcher
  57:     @staticmethod
  58:     def call(degrees: int, clockwise: bool, matrix: List[List[int]]) -> List[List[Optional[int]]]:
  59:         """
  60:         Rotates a matrix by 90, 180, or 270 degrees in the specified direction.
  61:         Pads rows with None values to ensure rectangular shape before rotating.
  62: 
  63:         :param degrees: The degree of rotation (must be 90, 180, or 270)
  64:         :param clockwise: Direction of rotation; True for clockwise, False for anticlockwise
  65:         :param matrix: A 2D list representing the matrix
  66:         :return: The rotated matrix
  67:         """
  68:         if not matrix or not any(matrix):
  69:             raise Exception("Matrix must be provided")
  70: 
  71:         # Normalize row lengths by padding with None
  72:         max_len = max(len(row) for row in matrix)
  73:         padded = [row + [None] * (max_len - len(row)) for row in matrix]
  74: 
  75:         if degrees not in [90, 180, 270]:
  76:             raise Exception("Degrees must be one of 90, 180, 270")
  77: 
  78:         method_name = f"rotate_{degrees}_{'clockwise' if clockwise else 'anticlockwise'}"
  79:         rotation_fn = _rotation_registry.get(method_name)
  80: 
  81:         if not rotation_fn:
  82:             raise Exception(f"No registered rotation method for {method_name}")
  83: 
  84:         return rotation_fn(padded)
  85: 
  86: 
```
<div style="page-break-after: always;"></div>

### code/module3/subtasks.py

```python
   1: from typing import List, Dict, Any
   2: import math
   3: from itertools import count
   4: 
   5: 
   6: class Subtask:
   7:     def sum_range(a: int, b: int) -> int:
   8:         return sum(list(range(a, b + 1)))
   9: 
  10:     def fibonacci(a: int) -> int:
  11:         if a < 0:
  12:             raise ValueError("Input should be a non-negative integer.")
  13:         elif a == 0:
  14:             return 0
  15:         elif a == 1:
  16:             return 1
  17: 
  18:         # Initialize the first two Fibonacci numbers
  19:         ary = [0, 1]
  20: 
  21:         # Generate Fibonacci numbers up to the a-th index
  22:         for x in range(2, a + 1):  # Start from 2 to a
  23:             next_fib = ary[x - 1] + ary[x - 2]  # Sum of the last two numbers
  24:             ary.append(next_fib)
  25: 
  26:         return ary[a]
  27: 
  28:     def factorial(n: int) -> int:
  29:         return math.prod(list(range(1, n + 1)))
  30: 
  31:     def greatest_common_divisor(a: int, b: int) -> int:
  32:         if a == b:
  33:             return a
  34: 
  35:         smaller_num = a if a < b else b
  36:         ary = []
  37:         for x in list(range(1, smaller_num + 1)):
  38:             common_divisor = a % x == 0 and b % x == 0
  39:             if common_divisor:
  40:                 ary.append(x)
  41: 
  42:         return max(ary)
  43: 
  44:     def least_common_multiple(a: int, b: int) -> int:
  45:         smaller = a if a < b else b
  46:         for i in count(start=smaller, step=smaller):
  47:             match = i % b == 0
  48:             print(f"{i} % {b} == 0 ? {match}")
  49:             if match:
  50:                 return i
```
<div style="page-break-after: always;"></div>

### code/module4/abstract_data_types.py

```python
   1: from base import Base
   2: from typing import List
   3: 
   4: 
   5: class AbstractDataTypes(Base):
   6:     @staticmethod
   7:     def stack_operations(cmds: List[str]) -> List[int]:
   8:         counter = 1
   9:         ary = []
  10:         for cmd in cmds:
  11:             if cmd in ["push", "enqueue"]:
  12:                 ary.append(counter)
  13:                 counter += 1
  14:             elif cmd in ["pop", "dequeue"]:
  15:                 ary.pop()
  16:                 counter -= 1
  17:         return ary
  18: 
  19:     @staticmethod
  20:     def queue_operations(cmds: List[str]) -> List[int]:
  21:         return AbstractDataTypes.stack_operations(cmds)
```
<div style="page-break-after: always;"></div>

### code/module4/coin_change.py

```python
   1: from base import Base
   2: from typing import List
   3: 
   4: class CoinChange(Base):
   5:     def __init__(self, value: str):
   6:         self.value = value
   7: 
   8:     @staticmethod
   9:     def min_coins(coins: List[int], amount: int) -> int:
  10:         """
  11:         Computes the minimum number of coins required to make up the given amount.
  12:         Uses bottom-up dynamic programming.
  13: 
  14:         :param coins: List of coin denominations.
  15:         :param amount: The target amount to reach.
  16:         :return: Minimum number of coins needed, or -1 if not possible.
  17:         """
  18:         dp = [float('inf')] * (amount + 1)
  19:         dp[0] = 0
  20: 
  21:         for coin in coins:
  22:             for x in range(coin, amount + 1):
  23:                 dp[x] = min(dp[x], dp[x - coin] + 1)
  24: 
  25:         return dp[amount] if dp[amount] != float('inf') else -1
  26: 
```
<div style="page-break-after: always;"></div>

### code/module4/divide_and_conquer_max_subarray.py

```python
   1: from base import Base
   2: from typing import List, Union, Any, Optional
   3: 
   4: class DivideAndConquerMaxSubarray(Base):
   5:     def __init__(self, value: List[int]):
   6:         # Store the input list as an instance variable
   7:         self.value = value
   8: 
   9:     @staticmethod
  10:     def has_pair_with_sum(nums: List[int], target: int) -> bool:
  11:         # Initialize an empty set to store previously seen numbers
  12:         seen = set()
  13: 
  14:         # Iterate through each number in the input list
  15:         for num in nums:
  16:             # Check if the complement (target - num) is already in the set
  17:             if (target - num) in seen:
  18:                 # If found, return True since a pair exists that sums to target
  19:                 return True
  20: 
  21:             # Otherwise, add the current number to the set
  22:             seen.add(num)
  23: 
  24:         # If no such pair was found after the loop, return False
  25:         return False
  26: 
```
<div style="page-break-after: always;"></div>

### code/module4/max_subarray.py

```python
   1: from base import Base
   2: from typing import List
   3: 
   4: class MaxSubarray(Base):
   5:     def __init__(self, arr: List[int]):
   6:         """Initialize with the input list of integers."""
   7:         self.arr = arr
   8: 
   9:     def max_crossing_sum(self, left: int, mid: int, right: int) -> int:
  10:         """
  11:         Finds the maximum subarray sum that crosses the midpoint.
  12:         """
  13:         left_sum = float('-inf')
  14:         total = 0
  15:         for i in range(mid, left - 1, -1):
  16:             total += self.arr[i]
  17:             left_sum = max(left_sum, total)
  18: 
  19:         right_sum = float('-inf')
  20:         total = 0
  21:         for i in range(mid + 1, right + 1):
  22:             total += self.arr[i]
  23:             right_sum = max(right_sum, total)
  24: 
  25:         return left_sum + right_sum
  26: 
  27:     def max_subarray_divide_conquer(self, left: int, right: int) -> int:
  28:         """
  29:         Recursively computes the maximum subarray sum using divide and conquer.
  30:         """
  31:         if left == right:
  32:             return self.arr[left]
  33: 
  34:         mid = (left + right) // 2
  35: 
  36:         return max(
  37:             self.max_subarray_divide_conquer(left, mid),
  38:             self.max_subarray_divide_conquer(mid + 1, right),
  39:             self.max_crossing_sum(left, mid, right)
  40:         )
  41: 
  42:     def max_subarray_sum(self) -> int:
  43:         """
  44:         Computes the maximum subarray sum for the entire list.
  45:         """
  46:         if not self.arr:
  47:             return 0
  48:         return self.max_subarray_divide_conquer(0, len(self.arr) - 1)
  49: 
```
<div style="page-break-after: always;"></div>

