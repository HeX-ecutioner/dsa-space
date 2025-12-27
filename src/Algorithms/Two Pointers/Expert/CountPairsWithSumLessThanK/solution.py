# (This file kept for compatibility but merged above) Simple wrapper demonstrating usage
# It's recommended to use the combined file CountPairsLessThanK_ProductOrSum for real implementations.
from typing import List

def count_pairs_sum(nums: List[int], k: int) -> int:
    from CountPairsLessThanK_ProductOrSum import count_pairs_with_sum_less_than  # conceptual import
    return count_pairs_with_sum_less_than(nums, k)
