#include <stdio.h>
#include <string.h>

// Reverse Vowels of a String
// Pattern: Two Pointers
// Time: O(n)

int hasVowel(char c) {
    return c == 'A' || c == 'a' ||
           c == 'E' || c == 'e' ||
           c == 'I' || c == 'i' ||
           c == 'O' || c == 'o' ||
           c == 'U' || c == 'u';
}

// Logic: have a l and r pointer and keep going towards the middle
//	  if you reach a point where l and r are vowels, swap
char* reverseVowels(char* s) {
    int l = 0;
    int r = strlen(s) - 1;

    while (l < r) {
        if (!hasVowel(s[l])) {
            l++;
        }

        if (!hasVowel(s[r])) {
            r--;
        }

        if (hasVowel(s[l]) && hasVowel(s[r])) {
            char tmp = s[l];
            s[l] = s[r];
            s[r] = tmp;

            l++;
            r--;
        }
    }

    return s;
}


void test() {
    char s1[] = "hello";
    char s2[] = "leetcode";
    char s3[] = "IceCreAm";

    printf("%s\n", reverseVowels(s1));
    printf("%s\n", reverseVowels(s2));
    printf("%s\n", reverseVowels(s3));
}


int main() {
    test();
    return 0;
}
