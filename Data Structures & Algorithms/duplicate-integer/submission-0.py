class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Store nums we havent seen into a hashset
        # If we have seen it, return true
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False