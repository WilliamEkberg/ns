class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Two pointers
        # Need to ignore spaces
        L = 0
        R = len(s)-1
        while R>L:
            V_R = s[R].lower()
            V_L = s[L].lower()
            if not V_R.isalnum():
                R -=1
            elif not V_L.isalnum():
                L += 1
            elif V_R != V_L:
                return False
            else:
                L += 1
                R -= 1
        return True


        
        