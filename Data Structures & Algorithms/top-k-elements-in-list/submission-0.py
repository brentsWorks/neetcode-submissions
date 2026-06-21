class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get count of each unique element in nums
        countNums = {}
        for num in nums:
            if num not in countNums:
                countNums[num] = 1
            else:
                countNums[num] += 1

        sortedFreqs = sorted(countNums, key=lambda x: countNums[x], reverse=True)
        topK = []
        for i in range(k):
            topK.append(sortedFreqs[i])

        return topK

        # sort numbers by count decreasing
        # return first k numbers as an array