class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        low = 0
        high = rows * columns - 1

        while(low <= high):
            mid = (low + high) // 2

            mid_row = mid // columns
            mid_column = mid % columns

            print(matrix[mid_row][mid_column])

            if matrix[mid_row][mid_column] == target:
                return True

            elif matrix[mid_row][mid_column] < target:
                low = mid + 1

            elif matrix[mid_row][mid_column] > target:
                high = mid - 1

        return False
        