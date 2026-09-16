class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer: look at left and right
        # the list is ordered from smallest to largest
        # add the l + r
        #       if l + r > target, go to next right idx
        #       if l + r < targer, go to next left idx
        if len(numbers) == 0:
            return []
        l_idx = 0
        r_idx = len(numbers) - 1
        for i in range(len(numbers)):
            addLR = numbers[l_idx] + numbers[r_idx]
            if addLR > target:
                r_idx -= 1
            elif addLR < target:
                l_idx += 1
            elif addLR == target:
                return [l_idx+1, r_idx+1]

            
