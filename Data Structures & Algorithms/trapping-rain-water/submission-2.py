class Solution:
    def trap(self, height: List[int]) -> int:
        # airArea = 0
        # wallIdx = [i for i, h in enumerate(height) if h != 0]
        # for i in range(len(wallIdx) - 1):
        #     heightDiff = height[wallIdx[i]] - height[wallIdx[i+1]]
        #     if heightDiff != 0:
        #         print(abs(wallIdx[i] - wallIdx[i+1]) * abs(heightDiff))
        #         airArea += abs(wallIdx[i] - wallIdx[i+1]) * abs(heightDiff)        
        # totalArea = len(height) * max(height)
        # wallArea = sum(height)
        # wtrArea = totalArea - wallArea - airArea
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        wtr = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                wtr += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                wtr += right_max - height[right]
                right -= 1
        return wtr