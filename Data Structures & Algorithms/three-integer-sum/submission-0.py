class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threeSumLst = []
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                TwoSum = nums[j] + nums[k]
                if nums[i] == -TwoSum:
                    threeSumNums = [nums[i], nums[j], nums[k]]
                    if threeSumNums not in threeSumLst:
                        threeSumLst.append(threeSumNums)
                    j += 1
                    k -= 1
                if nums[i] < -TwoSum:
                    j += 1
                if nums[i] > -TwoSum:
                    k -= 1
        return threeSumLst

            
