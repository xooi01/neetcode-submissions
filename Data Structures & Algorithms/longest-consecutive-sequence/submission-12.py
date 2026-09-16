class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            consectNum = [1] * len(nums)
            setNums = list(sorted(set(nums)))
            print(setNums)
            ConsIdx = 0;
            for i in range(len(setNums) - 1):
                if setNums[i] + 1 == setNums[i+1]:
                    isConsecutive = True
                    consectNum[ConsIdx] += 1
                else:
                    ConsIdx += 1
            return max(consectNum)
        