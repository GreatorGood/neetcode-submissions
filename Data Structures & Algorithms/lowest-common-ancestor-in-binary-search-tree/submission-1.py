# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self,node,visited,val,ans):
        if node.val == val:
            if node in visited and ans.val is None:
                ans.val = node
            else:
                visited.add(node)
            return True

        if node.left is None and node.right is None:
            return False
        
        left_ans = False
        right_ans = False
        if node.left is not None:
            left_ans = self.recur(node.left,visited,val,ans)
        
        if node.right is not None:
            right_ans = self.recur(node.right,visited,val,ans)

        if left_ans or right_ans:
            if node in visited and ans.val is None:
                ans.val = node
            else:
                visited.add(node)
            return True
        else:
            return False


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visited = set()
        ans = TreeNode(None,None,None)
        self.recur(root,visited,p.val,ans)
        self.recur(root,visited,q.val,ans)
        return ans.val