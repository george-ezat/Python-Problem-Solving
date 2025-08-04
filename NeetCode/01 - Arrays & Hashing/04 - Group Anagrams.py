class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = defaultdict(list)

        for s in strs:
            char_count = [0] * 26

            for char in s:
                char_count[ord(char) - ord('a')] += 1

            h_map[tuple(char_count)].append(s)

        return list(h_map.values())
