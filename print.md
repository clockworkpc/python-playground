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
  18:     def flatten_2d(nested: List[List[int]]) -> List[int]:
  19:         return [item for sublist in nested for item in sublist]
  20: 
  21:     @staticmethod
  22:     def transpose(matrix: List[List[int]]) -> List[List[int]]:
  23:         return list(map(list, zip(*matrix)))
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
   6:         self.value = value
   7: 
   8:     @staticmethod
   9:     def has_pair_with_sum(nums: List[int], target: int) -> bool:
  10:         seen = set()
  11:         for num in nums:
  12:             if (target - num) in seen:
  13:                 return True
  14:             seen.add(num)
  15:         return False
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

