class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(heights) - 1
        maxWtr = 0
        while leftPointer < rightPointer:
            currWidth = rightPointer - leftPointer
            currHeight = min(heights[leftPointer], heights[rightPointer])
            currArea = currWidth * currHeight
            maxWtr = max(maxWtr, currArea)

            if heights[leftPointer] < heights[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1
        return maxWtr