class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if the length of both the string are same:
        if len(s) != len(t):
            return False
        
        else:
            hashmap = dict(Counter(s))
            for i in range(len(t)):
                if t[i] not in hashmap or hashmap[t[i]]==0:
                   return False
                else:
                    if t[i] in hashmap and hashmap[t[i]] > 0:
                        hashmap[t[i]] -=1
            return True
        