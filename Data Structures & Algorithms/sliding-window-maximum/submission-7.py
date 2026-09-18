class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        r = k - 1
        # initialise first window
        negNums = [(-nums[i], i) for i in range(k)]
        heapq.heapify(negNums)

        # get max of first window
        maxLst = [-negNums[0][0]]

        # starting at second window to end
        for r in range(k, len(nums)):
            # push incoming number, index
            heapq.heappush(negNums, (-nums[r], r))

            # pop out-of-bounds
            while negNums[0][1] < r - k + 1:
                heapq.heappop(negNums)

            # record window max
            maxLst.append(-negNums[0][0])

        return maxLst