class Solution:
    def topKFrequent(self, nums, k):

        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for num in frequency:
            buckets[frequency[num]].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                for num in buckets[i]:
                    result.append(num)

                    if len(result) == k:
                        return result