class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(min(len(word) for word in strs)):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return prefix

            prefix += strs[0][i]

        return prefix