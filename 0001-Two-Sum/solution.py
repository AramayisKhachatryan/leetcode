class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            delta = target - n
            if delta in d.keys():
                return [i, d[delta]]
            d[n] = i
