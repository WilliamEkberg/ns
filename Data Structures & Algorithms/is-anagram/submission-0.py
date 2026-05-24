class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = {}
        l2 = {}

        for i in s:
            if i in l1:
                l1[i] += 1
            else:
                l1[i] = 1
        
        for i in t:
            if i in l2:
                l2[i] += 1
            else:
                l2[i] = 1

        return l1==l2
            

        