class Solution:
    def isPalindrome(self, s: str) -> bool:
        LettersOnly = "".join([char for char in s if char.isalnum()])
        LettersOnly = LettersOnly.lower()
        isPal = True
        for i in range(len(LettersOnly)): 
            print([LettersOnly[i], LettersOnly[len(LettersOnly) - i - 1]])               
            if LettersOnly[i] == LettersOnly[len(LettersOnly) - i - 1]:
                isPal = True
            else:
                return False
        return isPal