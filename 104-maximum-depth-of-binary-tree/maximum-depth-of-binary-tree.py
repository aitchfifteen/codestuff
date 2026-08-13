class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = 1
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()

            if not node:
                continue

            maxDepth = max(maxDepth, depth)

            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))

        return maxDepth

        