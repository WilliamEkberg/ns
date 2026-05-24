class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Small to left or right?
        # Smaller or Bigger?

        n = len(nums)
        R = n-1
        L = 0
        M = R//2

        while L<=R:
            M = (R+L)//2
            if target == nums[M]:
                return M

            # Left side is sorted
            if nums[L] <= nums[M]:
                if target < nums[M] and nums[L]<= target:
                    R = M-1
                else:
                    L=M+1
            # Right side is sorted
            else:
                if target > nums[M] and nums[R]>= target:
                    L = M+1
                else:
                    R = M-1
        return -1




        