def solution(dna1, dna2):
    m, n = len(dna1), len(dna2)
    # 创建DP表，dp[i][j]表示将dna1的前i个字符转换为dna2的前j个字符所需的最小操作次数
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 初始化第一行和第一列
    for i in range(m + 1):
        dp[i][0] = i  # 删除操作
    for j in range(n + 1):
        dp[0][j] = j  # 插入操作
    
    # 填充DP表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i-1] == dna2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # 如果字符相同，不需要操作
            else:
                # 取三种操作中的最小值：
                # 替换：dp[i-1][j-1] + 1
                # 删除：dp[i-1][j] + 1
                # 插入：dp[i][j-1] + 1
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    return dp[m][n]

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("AGT", "AGCT") == 1)
    print(solution("", "ACGT") == 4)
    print(solution("GCTAGCAT", "ACGT") == 5)