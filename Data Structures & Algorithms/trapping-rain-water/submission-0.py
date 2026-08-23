class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        run = 0
        for i in range(n):                    # prefix max, left to right
            run = max(run, height[i])
            prefix[i] = run

        run = 0
        for i in range(n - 1, -1, -1):        # suffix max, right to left
            run = max(run, height[i])
            suffix[i] = run

        total = 0
        for i in range(n):                    # water at each position
            total += min(prefix[i], suffix[i]) - height[i]
        return total