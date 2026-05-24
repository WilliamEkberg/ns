class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Create dictionary of dictionaries
        # dict outside index and dictionary

        # Go throgh and group the same once

        # Create dictonary and a list. Add the nex one and check if it is in there, if so it is an anagram. Else add it.
        # If same add index to dictionary.
        def create_key(s):
            count = [0]*26
            
            for i in s:
                count[ord(i) - ord('a')] += 1
            return tuple(count)

        d_map = {}

        for index, string in enumerate(strs):
            d = create_key(string)

            if d in d_map:
                d_map[d].append(string)
            else: 
                d_map[d] = [string]
        r = []

        for i in d_map:
            r.append(d_map[i])

        return r


        
        
        


        
