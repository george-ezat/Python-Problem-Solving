class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

# OR

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# OR

class Solution:
    def hammingWeight(self, n: int) -> int:
        return f"{n:b}".count('1')
