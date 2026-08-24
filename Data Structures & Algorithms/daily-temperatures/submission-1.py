class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stores tuples: [index, temp]

        for i, temp in enumerate(temperatures):
            # Resolve all colder days waiting in the stack
            while stack and temp > stack[-1][1]:
                stack_idx, stack_temp = stack.pop()
                res[stack_idx] = i - stack_idx
            
            # Push current day onto stack
            stack.append((i, temp))

        return res