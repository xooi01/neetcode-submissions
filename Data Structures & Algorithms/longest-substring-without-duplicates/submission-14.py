class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictChar = {}
        maxLen = 0
        startSubstring = 0
        if len(s) == 0:
            return 0
        for idx, char in enumerate(s):
            if char not in dictChar:
                dictChar[char] = idx
            else:
                if dictChar[char] >= startSubstring:
                    startSubstring = dictChar[char]+ 1
                dictChar[char] = idx
            maxLen = max(maxLen, idx - startSubstring + 1)
        return maxLen
            