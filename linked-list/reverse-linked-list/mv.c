#include <stdio.h>
#include <stdlib.h>

// Reverse Linked List
// Pattern: Linked List / Iteration
// Time: O(n)
// Space: O(1)

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    struct ListNode *next;
};


// 1 -> 2 -> 3 -> 4 -> 5
//
// ln 1: 1, NULL
// ln 2: 2, ln1
// ln 3: 3, ln2
// ln 4: 4, ln3
// ln 5: 5, ln4 | h
// next = NULL
// prev = ln4

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* next;

    while (head != NULL) {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }

    return prev;
}


void test() {
    struct ListNode n5 = {5, NULL};
    struct ListNode n4 = {4, &n5};
    struct ListNode n3 = {3, &n4};
    struct ListNode n2 = {2, &n3};
    struct ListNode n1 = {1, &n2};

    struct ListNode* reversed = reverseList(&n1);

    while (reversed != NULL) {
        printf("%d", reversed->val);

        if (reversed->next != NULL) {
            printf(" -> ");
        }

        reversed = reversed->next;
    }

    printf("\n");
}


int main() {
    test();
    return 0;
}
