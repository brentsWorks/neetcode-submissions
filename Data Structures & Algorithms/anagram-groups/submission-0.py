class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Idea is to create a dict which maps sorted strings (as keys)
        # to their original strings as values.
        anagrams = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in anagrams.keys():
                anagrams[sortedS] = [s]
            else:
                anagrams[sortedS].append(s)

        return list(anagrams.values())

        # If two strings are anagrams, they will have the same key sorted


        # output will be a list of sublists, 
        # each sublist containing anagrams of each other
