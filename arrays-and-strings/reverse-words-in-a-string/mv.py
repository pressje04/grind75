# Reverse Words in a String
# Pattern: String Traversal
# Time: O(n)


class Solution:
    # Logic: add each word into an array and return a string of the reversed array
    def reverseWords(self, s: str) -> str:
        arr = []
        str_builder = ""

        for c in s.strip():
            if c == ' ':
                if str_builder:
                    arr.append(str_builder)
                    str_builder = ""
            else:
                str_builder += c

        arr.append(str_builder)

        return " ".join(reversed(arr))


def test():
    sol = Solution()

    print(sol.reverseWords("the sky is blue"))
    print(sol.reverseWords("  hello world  "))
    print(sol.reverseWords("a good   example"))


if __name__ == "__main__":
    test()
