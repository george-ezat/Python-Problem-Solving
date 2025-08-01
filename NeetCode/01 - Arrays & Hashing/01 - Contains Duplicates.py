class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums_dict = {x: 0 for x in nums}
        # create a dict with nums' elements as keys and 0 as their values

        for i in nums:
            nums_dict[i] += 1
        # count the occurrences of each number

        for i in nums_dict.values():
            if i > 1:
                return True

        return False



# Another Solution

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
    # easy and direct solution
