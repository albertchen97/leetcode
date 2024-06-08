# https://leetcode.com/problems/subarray-sum-equals-k/description/

def subarraySum(nums: List[int], k: int) -> int:
    # Brute Force
    n = len(nums)
    for gap in range(1, n - 1):


