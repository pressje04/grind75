#include <stdio.h>
#include <stdlib.h>

// Maximum Depth of Binary Tree
// Pattern: Binary Tree / Recursion
// Time: O(n)
// Space: O(h)

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

// Logic: get the depth of the left and right subtree and return the max
int maxDepth(struct TreeNode* root) {
    if (root == NULL) {
        return 0;
    }

    int left = maxDepth(root->left) + 1;
    int right = maxDepth(root->right) + 1;

    return left > right ? left : right;
}


void test() {
    //         3
    //        / \
    //       9  20
    //          / \
    //         15  7

    struct TreeNode n9 = {9, NULL, NULL};
    struct TreeNode n15 = {15, NULL, NULL};
    struct TreeNode n7 = {7, NULL, NULL};
    struct TreeNode n20 = {20, &n15, &n7};
    struct TreeNode n3 = {3, &n9, &n20};

    printf("%d\n", maxDepth(&n3));
}


int main() {
    test();
    return 0;
}
