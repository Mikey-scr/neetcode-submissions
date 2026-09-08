class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(a, b):
            c = []
            i = 0
            j = 0

            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    c.append(a[i])
                    i += 1
                else:
                    c.append(b[j])
                    j += 1

            while i < len(a):
                c.append(a[i])
                i += 1

            while j < len(b):
                c.append(b[j])
                j += 1

            return c

        def merge_sort(a):
            if len(a) <= 1:
                return a

            mid = len(a) // 2

            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:])

            return merge(left, right)

        return merge_sort(nums)