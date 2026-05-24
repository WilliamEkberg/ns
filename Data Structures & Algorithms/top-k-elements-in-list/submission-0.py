class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        l = {}
        for i in nums:
            if i in l:
                l[i] += 1
            else:
                l[i] = 1

        res = []
        for _ in range(k):
            mf = max(l, key=l.get)
            res.append(mf)
            del l[mf]
        return res
        

        


        