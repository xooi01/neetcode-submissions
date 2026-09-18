class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # if len(s) == 0:
        #     return 0
        # strDict = {}
        # for char in s:
        #     if char not in strDict:
        #         strDict[char] = 1
        #     else:
        #         strDict[char] += 1
        # secondLongest = 0
        # longest = 0
        # for key in strDict:
        #     if strDict[key] > longest:
        #         secondLongest = longest
        #         longest = strDict[key]
        #     elif strDict[key] > secondLongest and strDict[key] != longest or strDict[key] == longest:
        #         secondLongest = longest
        # if k <= secondLongest:
        #     lenSubLong = longest + k
        # else:
        #     lenSubLong = longest + secondLongest
        
        # sliding window
        strDict = {}
        l = 0
        replace = 0
        for r in range(len(s)):
            if s[r] not in strDict:
                strDict[s[r]] = 1
                replace = (r - l + 1) - max(strDict.values())
            else:
                strDict[s[r]] += 1
                replace = (r - l + 1) - max(strDict.values())
            if replace > k:
                strDict[s[l]] -= 1
                l += 1
                replace = (r - l + 1) - max(strDict.values())
            lenSubLong = max(replace, r - l + 1)
        return lenSubLong