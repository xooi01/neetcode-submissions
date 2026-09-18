class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        # initialise stack
        stack = deque()
        openPar = "[({"
        closePar = "])}"
        for char in s:
            if char in openPar:
                stack.append(char)
                print(stack)
            if char in closePar:
                if not stack or stack[-1] != openPar[closePar.index(char)]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False