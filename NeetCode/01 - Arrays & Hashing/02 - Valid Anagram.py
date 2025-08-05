class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_cnt = {x: 0 for x in s}
        t_cnt = {x: 0 for x in t}

        for i in range(len(s)):
            s_cnt[s[i]] += 1
            t_cnt[t[i]] += 1

        return s_cnt == t_cnt


# Another Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


# Another Solution: (Using 'Counter' from collections Module)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = Counter(s)
        t_cnt = Counter(t)

        return s_cnt == t_cnt