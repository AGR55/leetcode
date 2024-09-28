class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        if matrix and n <= 20:
            for i in range(n):
                for j in range(i, n):
                    if i != j:
                        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            left = 0
            right = n - 1
            while left < right:
                for index in range(n):
                    matrix[index][left], matrix[index][right] = matrix[index][right], matrix[index][left]
                left += 1
                right -= 1

            return matrix

        else: raise ValueError



def main():
    solution = Solution()
    print(solution.rotate([[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == '__main__':
    main()
