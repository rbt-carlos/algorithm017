"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 递归法
        # res = []
        # def helper(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     for child in root.children:
        #         helper(child)
        # helper(root)
        # return res

        # 迭代法：
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res
