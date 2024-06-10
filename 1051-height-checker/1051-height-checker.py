class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = 0
        for a, b in zip(heights, sorted(heights)):
            if a != b:
                cnt += 1
        return cnt