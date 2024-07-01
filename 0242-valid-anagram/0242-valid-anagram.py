class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if the length of both the string are same:
        if len(s) != len(t):
            return False

        # without using counter:
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0) # to avoid the key error, we are adding 0 as default
        
        for c in countS:
            if countS[c] !=countT.get(c, 0):
                return False
        return True
        
        # else:
        #     hashmap = dict(Counter(s))
        #     for i in range(len(t)):
        #         if t[i] not in hashmap or hashmap[t[i]]==0:
        #            return False
        #         else:
        #             if t[i] in hashmap and hashmap[t[i]] > 0:
        #                 hashmap[t[i]] -=1
        #     return True
        