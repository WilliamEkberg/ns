class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        if t == '':
            return res

        # Prepare
        T = {}
        Window = {}
        need = 0
        res_l = float('inf')


        for i in t:
            if i in T:
                T[i] += 1
            else:
                T[i] = 1
                Window[i] = 0
                need += 1

        L = 0
        have = 0
        for R in range(len(s)):
            if s[R] in Window:
                Window[s[R]] += 1

                # update have
                if Window[s[R]] == T[s[R]]:
                    have += 1

                while have == need:
                    # add as new res if smaller
                    if R-L +1 < res_l:
                        res = s[L:R + 1]
                        res_l = R-L +1

                    # reduce
                    if s[L] in Window:
                        Window[s[L]] -= 1

                        # update have
                        if Window[s[L]] < T[s[L]]:
                            have -= 1

                    # step
                    L += 1
        return res

        
                

                    
                

            
            
                


