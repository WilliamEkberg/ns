class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        n = len(nums)

        for i in range(n):
            if nums[i]>0:
                break

            if i !=0 and nums[i-1]==nums[i]:
                continue
            a = i
            b = i+1
            c = n-1
            while b<c:
                val = nums[a] + nums[b] + nums[c]
                if val>0:
                    c -= 1
                elif val<0:
                    b += 1
                else:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while nums[b-1] == nums[b] and b<c:
                        b+=1
        return res


