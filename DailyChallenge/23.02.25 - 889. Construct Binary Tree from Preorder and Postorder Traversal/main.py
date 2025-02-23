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
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        left_root_val = preorder[1]
        left_size = postorder.index(left_root_val) + 1

        left_preorder = preorder[1 : left_size + 1]
        right_preorder = preorder[left_size + 1 :]

        left_postorder = postorder[:left_size]
        right_postorder = postorder[left_size:-1]

        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)

        return root


root_1 = TreeNode(
    1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
)
root_2 = TreeNode(1)

sol = Solution()


def are_trees_equal(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    return (
        node1.val == node2.val
        and are_trees_equal(node1.left, node2.left)
        and are_trees_equal(node1.right, node2.right)
    )


print(
    are_trees_equal(
        sol.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]), root_1
    )
)
print(are_trees_equal(sol.constructFromPrePost([1], [1]), root_2))
