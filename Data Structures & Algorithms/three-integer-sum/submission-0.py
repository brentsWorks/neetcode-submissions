class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all the triplets [nums[i], nums[j], nums[k]] 
        # where nums[i] + nums[j] + nums[k] == 0

        # array is not sorted, we handle this to be able to use
        # two ptr logic

        nums.sort()

        triplets = set()

        # make space for 3 ptrs
        for i in range(len(nums) - 2):
            j = i + 1 # 2nd number
            k = len(nums) - 1

            while j < k:
                potentialSum = nums[i] + nums[j] + nums[k]
                
                if potentialSum == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif potentialSum > 0:
                    k -= 1
                else:
                    j += 1
        
        # need to return a 2d array (list of lists containing ints)
        # so we convert each triplet tuple into a list and wrap it in an array

        return [list(triplet) for triplet in triplets]

            