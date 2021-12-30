class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        # https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
        """

        # Matrix rows and Colums are equal
        matrix_rows = len(matrix)
        matrix_cols = len(matrix[0])

        for i in range(matrix_rows // 2):
            for j in range(matrix_rows // 2 + matrix_rows % 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[matrix_rows - 1 - j][i]
                matrix[matrix_rows - 1 - j][i] = matrix[matrix_rows - 1 - i][matrix_rows - 1 - j]
                matrix[matrix_rows - 1 - i][matrix_rows - 1 - j] = matrix[j][matrix_rows - 1 - i]
                matrix[j][matrix_rows - 1 - i] = temp




