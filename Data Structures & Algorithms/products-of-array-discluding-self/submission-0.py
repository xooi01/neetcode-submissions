class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodLst = [1] * len(nums)
        leftProd = [1] * (len(nums))
        rightProd = [1] * (len(nums))
        for i in range(len(nums)-1):
            leftProd[i+1] = nums[i]*leftProd[i]
        
        for j in range(len(nums) -1):
            rightProd[len(nums)-j-2] = nums[len(nums)-j-1]*rightProd[len(nums)-j-1]

        for k in range(len(nums)):
            prodLst[k] = leftProd[k] * rightProd[k]
            
        return prodLst
