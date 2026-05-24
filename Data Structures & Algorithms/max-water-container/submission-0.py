class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Move the smallest one inwards. Skip if not taller.
        # Save the max
        #
        max_val = 0
        n=len(heights)

        i = 0
        j = n-1
        while i<j:
            h1 = heights[i]
            h2 = heights[j]
            d = j-i

            if h1>=h2:
                h = h2
                j -= 1

            elif h1<h2:
                h = h1
                i += 1

            v = h*d

            max_val = max(v, max_val)
        return max_val


            


        