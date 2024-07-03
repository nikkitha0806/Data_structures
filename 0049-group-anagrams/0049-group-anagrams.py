class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26 # because we have 26 letters
            for i in word:
                count[ord(i) - ord("a")] +=1 # based on the letter we add 1 to make a key
            res[tuple(count)].append(word)

        return res.values()


        