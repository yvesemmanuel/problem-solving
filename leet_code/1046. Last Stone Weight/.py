from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sortedDescendingStones = sorted(stones, reverse=True)

        if len(sortedDescendingStones) == 0:
            return 0
        elif len(sortedDescendingStones) == 1:
            return sortedDescendingStones[0]
        else:
            s1, s2, rest = sortedDescendingStones[0], sortedDescendingStones[1], sortedDescendingStones[2:]
            if s1 == s2:
                return self.lastStoneWeight(rest)
            else:
                return self.lastStoneWeight(self.insertSortedDescending((s1 - s2), rest))

    def insertSortedDescending(self, x: int, l: List[int]) -> List[int]:
        if len(l) == 0:
            return [x]
        else:
            y, ys = l[0], l[1:]

            if x >= y:
                return [x, y] + ys
            else:
                return [y] + self.insertSortedDescending(x, ys)

solution = Solution()
print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))