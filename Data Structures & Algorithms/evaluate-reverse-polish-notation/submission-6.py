class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = deque([int(tokens[0])])
        result = 0

        for char in tokens[1:]:
            if char in "+-*/":
                num2 = int(evalStack.pop())
                num1 = int(evalStack.pop())
                if char == "+":
                    result = num1 + num2
                if char == "-":
                    result = num1 - num2
                if char == "*":
                    result = num1 * num2
                if char == "/":
                    result = int(num1 / num2)
                evalStack.append(result)
            else:
                evalStack.append(int(char))
        return evalStack[-1]