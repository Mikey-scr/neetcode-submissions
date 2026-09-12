class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for num in sett:
            if num - 1 in sett:
                continue

            start = num

            while num + 1 in sett:
                num += 1

            length = num - start + 1

            longest = max(longest, length)

        return longest