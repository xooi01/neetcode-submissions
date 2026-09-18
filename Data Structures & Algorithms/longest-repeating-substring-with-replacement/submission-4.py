class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        strDict = {}
        l = 0
        replace = 0
        for r in range(len(s)):
            if s[r] not in strDict:
                strDict[s[r]] = 1
            else:
                strDict[s[r]] += 1
            replace = (r - l + 1) - max(strDict.values())
            if replace > k:
                strDict[s[l]] -= 1
                l += 1
            lenSubLong = max(replace, r - l + 1)
        return lenSubLong
# 27:09 need more practise on sliding window problems
# Time complexity: O(N)
# Space complexity: O(1)