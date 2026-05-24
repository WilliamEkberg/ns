class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        words = []

        c=0
        temp = ''
        temp_2 = ''
        
        for i in s:
            if c==0:
                if i == '#':
                    c = int(temp)
                    temp = ''
                    if c==0:
                        words.append('')
                        temp = ''
                else:
                    temp += i
            else:
                temp_2 += i
                c -= 1
                if c==0:
                    words.append(temp_2)
                    temp_2 = ''
        
        return words
                





