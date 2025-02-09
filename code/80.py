def solution(stocks):
    if not stocks or len(stocks) < 2:
        return 0
    
    n = len(stocks)
    # hold: 持有股票的最大收益
    # sold: 刚卖出股票（在冷冻期）的最大收益
    # rest: 不持有股票且不在冷冻期的最大收益
    hold = [-float('inf')] * n
    sold = [0] * n
    rest = [0] * n
    
    # 初始状态
    hold[0] = -stocks[0]  # 第一天买入
    
    for i in range(1, n):
        # 第i天持有股票：前一天就持有 或 前一天不持有且不在冷冻期时买入
        hold[i] = max(hold[i-1], rest[i-1] - stocks[i])
        # 第i天卖出股票：前一天持有股票时卖出
        sold[i] = hold[i-1] + stocks[i]
        # 第i天不持有股票且不在冷冻期：前一天不持有股票（包括冷冻期和非冷冻期）
        rest[i] = max(rest[i-1], sold[i-1])
    
    # 最后一天的最大收益是卖出或不持有的最大值
    return max(sold[n-1], rest[n-1])


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([1, 2]) == 1 )
    print(solution([2, 1]) == 0 )
    print(solution([1, 2, 3, 0, 2]) == 3 )
    print(solution([2, 3, 4, 5, 6, 7]) == 5 )
    print(solution([1, 6, 2, 7, 13, 2, 8]) == 12 )