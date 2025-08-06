class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> list[str]:
        result = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return result


# example: ['Hello World', 'and', 'hello', 'every', 'one']
# encode: 11#Hello World3#and5#hello5#every3#one
# decode: ['Hello World', 'and', 'hello', 'every', 'one']