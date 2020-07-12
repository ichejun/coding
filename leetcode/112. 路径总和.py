'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if root == None:
            return False

        '''
        假定从根节点到当前节点的值之和为 val，
        我们可以将这个大问题转化为一个小问题：
            是否存在从当前节点的子节点到叶子的路径，满足其路径和为 sum - val。
        ---->递归
        '''
        if not root.left and not root.right:#如果无子节点，即为叶子节点。返回是否等于余数。
            return root.val == sum
        '''
        递归处
        '''
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)




