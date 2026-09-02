class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair positions and speeds, then sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            time = (target - p) / s
            stack.append(time)
            # If the current car arrives faster or at the same time as the fleet ahead,
            # it merges into the fleet ahead (pop it off the stack).
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)