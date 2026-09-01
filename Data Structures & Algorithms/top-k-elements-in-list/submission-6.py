class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort the numbers in order of appearance
        # output i to k numbers in list
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        num_dict_sort = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
        return list(num_dict_sort)[:k]
