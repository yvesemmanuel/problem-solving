from typing import Iterable

class Solution:
    def mergeArrays(self, nums1: Iterable[Iterable[int]], nums2: Iterable[Iterable[int]]):
        if not nums1:
            return nums2
        elif not nums2:
            return nums1
        else:
            (id1, val1), t1 = nums1[0], nums1[1:]
            (id2, val2), t2 = nums2[0], nums2[1:]

            if id1 < id2:
                return [(id1, val1)] + self.mergeArrays(t1, nums2)
            elif id2 < id1:
                return [(id2, val2)] + self.mergeArrays(nums1, t2)
            else:
                return [(id1, val1 + val2)] + self.mergeArrays(t1, t2)

solution = Solution()
nums1, nums2 = [[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]
print(solution.mergeArrays(nums1, nums2))