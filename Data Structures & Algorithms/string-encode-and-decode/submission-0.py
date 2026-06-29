class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # move j until we find '#'
            while s[j] != '#':
                j += 1

            # length of current word
            length = int(s[i:j])
        # extract the word
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # move i to the start of next encoded part
            i = j + 1 + length

        return result

