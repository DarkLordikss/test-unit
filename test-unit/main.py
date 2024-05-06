from typing import List


class Solution:
    @staticmethod
    def can_partition(nums: List[int]) -> bool:
        if len(nums) < 1 or len(nums) > 100:
            raise KeyError

        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            next_dp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                next_dp.add(t + nums[i])
                next_dp.add(t)
            dp = next_dp
        return False
