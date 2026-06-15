class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # height[i] represents the height of a bar, which has width 1
        # each bar has width 1
        
        # if height lower between two bars, that is trapped water
        # water at each position = max wall on that side - height at that pos


        # idea is to track highest wall seen on each side
        # use two pointers to find these two walls

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 
        while l < r:
            # how do we accumulate our result?
            # pair of bars can only trap water up to a level that is
            # equal to the lesser of the two maximums on its l & r

            # we are accumulating one width at a time, 
            # not calculating all at once.
            # hence we work inward one index at a time from the limiting side
            # since we then know what our ceiling is for a given index
            if leftMax < rightMax:
                # we know leftMax is the limiting wall for height[l]
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                # the above difference is how many units of water is avail
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res

        # return max area of water that can be trapped between two bars
        