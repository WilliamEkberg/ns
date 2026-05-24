class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        count = 0

        for num in nums:
            if num-1 not in numSet:
                count = 1
                val = num
                while count>0:
                    val +=1
                    if val in numSet:
                        count += 1
                    else:
                        if count > longest:
                            longest = count
                        count = 0
        return longest






