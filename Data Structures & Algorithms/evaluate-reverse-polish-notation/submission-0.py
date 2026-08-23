class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                v2 = stack.pop()
                v1 = stack.pop()
                if token == "+":
                    stack.append(v1 + v2)
                elif token == "-":
                    stack.append(v1 - v2)
                elif token == "*":
                    stack.append(v1 * v2)
                else:
                    stack.append(int(v1 / v2))  # Truncates toward zero
            else:
                stack.append(int(token))
                
        return stack[0]