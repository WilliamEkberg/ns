class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            w = r-l +1
            c = max(count.values())

            while not (w - c <= k):
                count[s[l]] -=1
                l+=1

                w = r-l -1
                c = max(count.values())
            
            res = max(res, w)
        return res
                





            

            





        