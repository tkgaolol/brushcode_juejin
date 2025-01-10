def solution(n, k, data):
    # Edit your code here

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # 初始状态
    
    # 遍历每一天
    for i in range(n):
        # 遍历当前剩余的食物数量
        for j in range(k + 1):
            if dp[i][j] == float('inf'):
                continue
                
            # 遍历今天可以购买的食物数量
            for buy in range(k - j + 1):
                # 消耗一份食物后的剩余量
                remain = j + buy - 1
                if remain >= 0:
                    dp[i + 1][remain] = min(
                        dp[i + 1][remain],
                        dp[i][j] + data[i] * buy
                    )
    
    # 返回最后一天剩余食物为0的最小花费
    return dp[n][0]


if __name__ == "__main__":
    # Add your test cases here

    print(solution(5, 2, [1, 2, 3, 3, 2]) == 9)
