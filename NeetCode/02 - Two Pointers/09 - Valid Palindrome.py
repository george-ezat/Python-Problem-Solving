class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        return chars == chars[::-1]


# or


class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        return chars == list(reversed(chars))


# or


class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        i = 0
        j = len(chars) - 1

        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1

        return True
