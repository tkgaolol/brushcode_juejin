from functools import lru_cache

def solution(N, familiar_matrix):
    @lru_cache(maxsize=None)
    def dp(mask):
        if mask == 0:
            return 0
        # 找到第一个未分组的成员
        first = 0
        while not (mask & (1 << first)):
            first += 1
        # 尝试所有可能的三人组合
        min_sum = float('inf')
        for j in range(first + 1, N):
            if mask & (1 << j):
                for k in range(j + 1, N):
                    if mask & (1 << k):
                        group_sum = (
                            familiar_matrix[first][j]
                            + familiar_matrix[first][k]
                            + familiar_matrix[j][k]
                        )
                        total = group_sum + dp(
                            mask ^ (1 << first) ^ (1 << j) ^ (1 << k)
                        )
                        min_sum = min(min_sum, total)
        return min_sum

    # 初始状态：所有成员未分组
    full_mask = (1 << N) - 1
    return dp(full_mask)

if __name__ == "__main__":
    #  You can add more test cases here
    familiar_matrix1 = [[100, 78, 97], [78, 100, 55], [97, 55, 100]]
    familiar_matrix2 = [[100, 56, 19, 87, 38, 61],
       [56, 100, 70, 94, 88, 94],
       [19, 70, 100, 94, 43, 95],
       [87, 94, 94, 100, 85, 11],
       [38, 88, 43, 85, 100, 94],
       [61, 94, 95, 11, 94, 100]]

    print(solution(3, familiar_matrix1) == 230 )
    print(solution(6, familiar_matrix2) == 299 )