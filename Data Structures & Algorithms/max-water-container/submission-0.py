class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find maxArea using area between two bars
        
        # i, j = 0, len(heights) - 1
        # maxFound = 0
        # area = min(heights[i], heights[j]) * (j - i + 1)
        # compare area & maxFound

        # when do we move pointers? what is bottleneck?
        # move the smaller height bar inward to try and look for larger area pair


        i, j = 0, len(heights) - 1
        maxFound = 0

        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            if area > maxFound:
                maxFound = area
            
            # move ptrs
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxFound

            


