class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       # sort the array
       # if num[i] = num[i+1], true. else, false
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        
        return False
        