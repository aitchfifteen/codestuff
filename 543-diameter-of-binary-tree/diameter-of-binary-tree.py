class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        height = {}
        maxDiameter = 0

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                leftHeight = height.get(node.left, 0)
                rightHeight = height.get(node.right, 0)

                maxDiameter = max(
                    maxDiameter,
                    leftHeight + rightHeight
                )

                height[node] = 1 + max(leftHeight, rightHeight)

            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return maxDiameter