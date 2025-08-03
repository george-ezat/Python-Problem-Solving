class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_dict = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in prev_dict:
                return [prev_dict[diff], i]

            prev_dict[num] = i