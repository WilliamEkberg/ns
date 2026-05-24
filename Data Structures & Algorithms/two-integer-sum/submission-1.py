class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Ugly dictionary. Put all in dictionary and then pich one and check if the remainder exists in the dict.

        # Full search also wokrs

        d = {}
        for i in range(len(nums)):
            value = nums[i]
            diff = target - value

            if diff in d:
                return sorted([i, d[diff]])
            else:
                d[value] = i