def solution(width):
    if width == 0:
        return []
    n = width
    # 初始化矩阵，全部为0
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    val = 1

    if n == 2:
        return [[1, 1], [0, 1]]
    # 层数k，从0开始
    for k in range((n) // 2):
        # 填充顶行：从左到右
        for col in range(left - 1, right + 1):
            matrix[top][col] = val
        # 填充右列：从上到下（排除顶行）
        for row in range(top + 1, bottom + 1):
            matrix[row][right] = val
        # 填充底行：从右到左（排除右列）
        if top != bottom - 1:
            for col in range(right - 1, left - 1, -1):
                matrix[bottom][col] = val
        # 填充左列：从下到上（排除底行和顶行）
        if left != right:
            for row in range(bottom - 1, top + 1, -1):
                matrix[row][left] = val
        top += 2
        bottom -= 2
        left += 2
        right -= 2
        if left > right:
            break
        if top > bottom:
            break
    return matrix

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(5) == [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])
    print(solution(8) == [[1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,1],[1,1,1,1,1,1,0,1],[1,0,0,0,0,1,0,1],[1,0,1,0,0,1,0,1],[1,0,1,1,1,1,0,1],[1,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1]])
    print(solution(2) == [[1, 1],[0, 1]])