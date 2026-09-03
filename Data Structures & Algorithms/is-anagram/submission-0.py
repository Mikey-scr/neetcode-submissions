class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = [0] * 26

        for i in range(len(s)):
            frequency[ord(s[i]) - ord("a")] += 1

        for i in range(len(t)):
            frequency[ord(t[i]) - ord("a")] -= 1

        for value in frequency:
            if value != 0:
                return False

        return True