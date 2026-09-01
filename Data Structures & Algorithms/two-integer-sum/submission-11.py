class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # subtract nums[0] from target and see if in the list. if yes, get the index.
        # if no, subtract nums[1] from target and see if in the list, etc.
        smallIdx = 0
        notFound = True
        while notFound:
            opp = target - nums[smallIdx]
            if opp in nums[smallIdx + 1 :]:
                notFound = False
                comp = nums.index(opp, smallIdx+1)
                return [smallIdx, comp]
            else:
                smallIdx += 1