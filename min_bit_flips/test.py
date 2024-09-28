import pytest
from min_bit_flips import Solution

def test_solution():
    assert Solution().minBitFlips(5, 10) == 4
    with pytest.raises(ValueError):
        Solution().minBitFlips(-1, (10 ** 9) + 1)
