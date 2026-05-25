class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        L = 0
        longest=0

        for R in range(len(s)):
            while s[R] in d:
                d.remove(s[L])
                L+=1
            
            d.add(s[R])

            longest = max(longest, R-L + 1)

        return longest



                    

    
            

            
        