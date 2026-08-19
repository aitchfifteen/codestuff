from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]

        if originalColor == color:
            return image

        queue = deque([(sr, sc)])

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        while queue:
            row, col = queue.popleft()

            if image[row][col] != originalColor:
                continue

            image[row][col] = color

            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc

                if (
                    0 <= newRow < len(image)
                    and 0 <= newCol < len(image[0])
                    and image[newRow][newCol] == originalColor
                ):
                    queue.append((newRow, newCol))

        return image