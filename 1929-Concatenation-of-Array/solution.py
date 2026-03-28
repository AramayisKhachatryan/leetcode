from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        res = [0] * (2 * nums_len)
        for i in range(nums_len):
            res[i] = res[i + nums_len] = nums[i]

        return res