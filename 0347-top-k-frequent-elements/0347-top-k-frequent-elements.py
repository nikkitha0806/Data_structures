class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using bucket sort concept:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1): # -1 for printing in reverse order
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res