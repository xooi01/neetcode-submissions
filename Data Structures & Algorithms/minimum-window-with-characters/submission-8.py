class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        l = 0
        countS = {}
        validSub = s
        found = False
        need = len(countT)
        have = 0
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0) + 1
            if s[r] in countT:
                if countS[s[r]] == countT[s[r]]:
                    have += 1
                while have == need:
                    found = True
                    if len(validSub) >= len(s[l:r+1]):
                        validSub = s[l:r+1]
                    if s[l] in countT:
                        if countS[s[l]] == countT[s[l]]:
                            have -= 1
                        countS[s[l]] = countS.get(s[l], 0) - 1
                    l += 1
        return validSub if found else ""
        # 33:12, needed some help debugging but general outline was there
        # Time complexity: O(M+N) 
        # Space complexity: O(K)