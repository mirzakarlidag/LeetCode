"""
1028. Recover a Tree From Preorder Traversal

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        stack = []
        i = 0
        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == "-":
                depth += 1
                i += 1
            
            val = 0
            while i < len(traversal) and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(val)
            
            if depth == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                while len(stack) > depth:
                    stack.pop()
                stack[-1].right = node
            
            stack.append(node)
        
        return stack[0]


root_1 = TreeNode(
    1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7))
)
root_2 = TreeNode(
    1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5, TreeNode(6, TreeNode(7)))
)
root_3 = TreeNode(1, TreeNode(401, TreeNode(349, TreeNode(90)), TreeNode(88)))

sol = Solution()

print(sol.recoverFromPreorder("1-2--3--4-5--6--7") == root_1)
print(sol.recoverFromPreorder("1-2--3---4-5--6---7") == root_2)
print(sol.recoverFromPreorder("1-401--349---90--88") == root_3)
