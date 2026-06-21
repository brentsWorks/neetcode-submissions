class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Store character counts in respective hash maps
        # compare each map at the end


        if len(s) != len(t): return False

        countS, countT = {}, {}

        # s and t must be same length so we can just pick one to pass thru
        for i in range(len(s)):
            # initialize count to 0 if needed, and add 1 to count
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT