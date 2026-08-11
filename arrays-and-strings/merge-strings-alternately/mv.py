# Merge Strings Alternately
# Pattern: Two Pointers
# Time: O(n)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        1. Two pointers starting at each word
        2. Go through word1 and word2 appending letters to merged
        3. If you reach the end of a word, finish out merged w/ other word
        """
        merged = ""
        i, j = 0, 0
        word1_len, word2_len = len(word1), len(word2)

        while i < word1_len and j < word2_len:
            merged += word1[i]
            merged += word2[j]

            i += 1
            j += 1

        if i >= word1_len and j < word2_len:
            merged += word2[j:]

        if j >= word2_len and i < word1_len:
            merged += word1[i:]

        return merged


def test():
    sol = Solution()
    print(sol.mergeAlternately("abc", "pqr"))
    print(sol.mergeAlternately("ab", "pqrs"))
    print(sol.mergeAlternately("abcd", "pq"))


if __name__ == "__main__":
    test()
