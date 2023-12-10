import math

# O(m * n) time | O(m * n) space
class Solution:
    def spiralOrder_1(self, matrix):
        LEFT_BORDER, RIGHT_BORDER = 0, len(matrix[0]) - 1
        TOP_BORDER, BOTTOM_BORDER = 0, len(matrix) - 1
        spirals_count = 0
        all_elements = []
        while LEFT_BORDER <= RIGHT_BORDER and TOP_BORDER <= BOTTOM_BORDER:
            for i in range(LEFT_BORDER, RIGHT_BORDER + 1):
                all_elements.append(matrix[spirals_count][i])
            for i in range(TOP_BORDER + 1, BOTTOM_BORDER + 1):
                all_elements.append(matrix[i][RIGHT_BORDER])
            if TOP_BORDER < BOTTOM_BORDER:
                for i in range(RIGHT_BORDER - 1, LEFT_BORDER - 1, -1):
                    all_elements.append(matrix[BOTTOM_BORDER][i])
            if LEFT_BORDER < RIGHT_BORDER:
                for i in range(BOTTOM_BORDER - 1, TOP_BORDER, -1):
                    all_elements.append(matrix[i][spirals_count])
            spirals_count += 1
            LEFT_BORDER += 1
            RIGHT_BORDER -= 1
            TOP_BORDER += 1
            BOTTOM_BORDER -= 1
        return all_elements

    def spiralOrder(self, matrix):
        left_bound, right_bound = 0, len(matrix[0]) - 1
        lower_bound, upper_bound = len(matrix) - 1, 0

        n_spirals = math.ceil(min(right_bound + 1, lower_bound + 1) / 2)
        result = []
        for i in range(n_spirals):
            for j in range(left_bound, right_bound + 1):
                result.append(matrix[upper_bound][j])
            upper_bound += 1

            for j in range(upper_bound, lower_bound + 1):
                result.append(matrix[j][right_bound])
            right_bound -= 1

            if lower_bound >= upper_bound:
                for j in range(right_bound, left_bound - 1, -1):
                    result.append(matrix[lower_bound][j])
            lower_bound -= 1

            if left_bound <= right_bound:
                for j in range(lower_bound, upper_bound - 1, -1):
                    result.append(matrix[j][left_bound])
            left_bound += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert solution.spiralOrder([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert solution.spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    assert solution.spiralOrder([[1, 2, 3]]) == [1, 2, 3]

