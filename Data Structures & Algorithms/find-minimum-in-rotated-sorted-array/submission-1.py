class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Find where the left element is bigger then the right one.?

        n = len(nums)
        L = 0
        R = n-1
        M = R//2

        while L != M:

            if nums[R]>nums[M]:
                R = M
                M = L + (R-L)//2
            else:
                L = M+1
                M = L + (R-L)//2

        return min(nums[L],nums[R])

        
        