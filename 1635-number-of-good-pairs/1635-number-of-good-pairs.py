class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # using counters to count the numbers in the list:
        count = Counter(nums)
        res = 0
        for i, c in count.items():
            res+= c*(c-1)//2
        return res