"""
1261. Find Elements in a Contaminated Binary Tree

Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
 

Example 1:


Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
Example 2:


Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
Example 3:


Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 

Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 104]
Total calls of find() is between [1, 104]
0 <= target <= 106
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.values = set()

        def reconstruct(node):
            if node.left != None:
                node.left.val = 2 * node.val + 1
                self.values.add(node.left.val)
                reconstruct(node.left)
            if node.right != None:
                node.right.val = 2 * node.val + 2
                self.values.add(node.right.val)
                reconstruct(node.right)

        root.val = 0
        self.values.add(0)
        reconstruct(root)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.values


def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i, node in enumerate(nodes):
        if node:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(nodes):
                node.left = nodes[left_index]
            if right_index < len(nodes):
                node.right = nodes[right_index]
    return nodes[0]


root1 = build_tree([-1, None, -1])
obj1 = FindElements(root1)
print(obj1.find(1) == False)
print(obj1.find(2) == True)

root2 = build_tree([-1, -1, -1, -1, -1])
obj2 = FindElements(root2)
print(obj2.find(1) == True)
print(obj2.find(3) == True)
print(obj2.find(5) == False)

root3 = build_tree([-1, None, -1, -1, None, -1])
obj3 = FindElements(root3)
print(obj3.find(2) == True)
print(obj3.find(3) == False)
print(obj3.find(4) == False)
print(obj3.find(5) == True)
