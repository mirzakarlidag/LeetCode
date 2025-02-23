"""
889. Construct Binary Tree from Preorder and Postorder Traversal

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if preorder:
            root = TreeNode(preorder[0])
            left_sub_tree = []
            right_sub_tree = []

        for val in postorder:
            left_sub_tree.append(val)
            if not preorder:
                return None
            if val == preorder[1]:
                break


root = TreeNode(
    1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
)

sol = Solution()

print(
    sol.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
    == [1, 2, 3, 4, 5, 6, 7]
)
print(sol.constructFromPrePost([1], [1]) == [1])
