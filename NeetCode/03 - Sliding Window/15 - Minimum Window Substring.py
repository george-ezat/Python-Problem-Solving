class Solution:
    def check_counts(self, s, t):
        for n, cnt in s.items():
            if t[n] > cnt:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        if not (s and t):
            return ''

        s_count = {c: 0 for c in t}
        t_count = Counter(t)

        l = 0
        i, j = -1, -1
        result_len = float('inf')
        for r in range(len(s)):
            if s[r] in t:
                s_count[s[r]] += 1

            while self.check_counts(s_count, t_count):
                if result_len > r - l:
                    i = l
                    j = r
                    result_len = j - i

                if s[l] in t:
                    s_count[s[l]] -= 1

                l += 1

        return s[i:j + 1] if result_len != float('inf') else ''
