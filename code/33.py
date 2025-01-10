def solution(n: int, a: list, b: list) -> int:
    MOD = 10**9 + 7
    
    # 使用动态规划，dp[i][j]表示前i张卡片选择后，和除以3的余数为j的方案数
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[0][0] = 1  # 初始状态
    
    # 对每张卡片
    for i in range(n):
        # 对于当前的所有余数状态
        for j in range(3):
            # 选择正面
            remainder_a = (j + a[i]) % 3
            dp[i + 1][remainder_a] = (dp[i + 1][remainder_a] + dp[i][j]) % MOD
            
            # 选择背面
            remainder_b = (j + b[i]) % 3
            dp[i + 1][remainder_b] = (dp[i + 1][remainder_b] + dp[i][j]) % MOD
    
    # 返回最终和能被3整除的方案数
    return dp[n][0]

if __name__ == '__main__':
    print(solution(n = 3, a = [1, 2, 3], b = [2, 3, 2]) == 3)
    print(solution(n = 4, a = [3, 1, 2, 4], b = [1, 2, 3, 1]) == 6)
    print(solution(n = 5, a = [1, 2, 3, 4, 5], b = [1, 2, 3, 4, 5]) == 32)