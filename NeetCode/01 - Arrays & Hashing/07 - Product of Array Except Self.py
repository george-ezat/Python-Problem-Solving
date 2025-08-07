class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            result[i] = prefix

        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i + 1]
            result[i] *= postfix

        return result

"""
Trace this example to understand:

prefix:   1  1  2  6
>> nums:  1  2  3  1
postfix:  6  3  1  1

result:   6  3  2  6  >> which equals (prefix * postfix) of the nums

solution steps:
1. we calc the prefix in the 'result' list
2. then we multiply the prefix(stored in the 'result') by the postfix
"""