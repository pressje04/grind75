class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Logic: sort each word and add it to a dictionary, if a word
               is already in the dictionary, add it to it's array
        """
        
        anagrams = {} # key = sorted word, val = [array of words]

        for s in strs:
            sorted_word = "".join(sorted(s))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(s)
            else:
                anagrams[sorted_word] = [s]

        return list(anagrams.values())



