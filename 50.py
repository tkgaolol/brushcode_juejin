import sys

def solution(distance, n, gasStations):
    maxCapacity = 400
    inf = sys.maxsize
 
    # 按照加油站位置升序排序
    gasStations.sort(key=lambda x: x[0])
 
    # 计算每个加油站之间的距离
    dis = [gasStations[0][0]]
    for i in range(1, len(gasStations)):
        dis.append(gasStations[i][0] - gasStations[i-1][0])
 
    # 初始化 dp 数组
    dp = [[inf] * (maxCapacity + 1) for _ in range(n + 2)]
    dp[0][200] = 0  # 初始状态，容量为200，花费为0
 
    # 动态规划计算最小花费
    for i in range(1, n + 1):
        for j in range(maxCapacity + 1):
            for k in range(maxCapacity + 1):
                if j + dis[i-1] - k >= 0 and k >= dis[i-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + (j + dis[i-1] - k) * gasStations[i-1][1])
 
    # 判断是否可以到达终点
    remaining_fuel = 200 + distance - gasStations[n-1][0]
 
    if remaining_fuel > maxCapacity or remaining_fuel < 0:
        return -1
    
    result = inf
    for i in range(remaining_fuel, maxCapacity + 1):
        result = min(result, dp[n][i])
 
    if result == inf:
        return -1
    
    return result



if __name__ == "__main__":
    #  You can add more test cases here
    gas_stations1 = [(100, 1), (200, 30), (400, 40), (300, 20)]
    gas_stations2 = [(100, 999), (150, 888), (200, 777),
                     (300, 999), (400, 1009), (450, 1019), (500, 1399)]
    gas_stations3 = [(101,), (100, 100), (102, 1)]
    gas_stations4 = [(34, 1), (105, 9), (9, 10), (134, 66), (215, 90), (999, 1999), (49, 0), (10, 1999), (200, 2),
                     (300, 500), (12, 34), (1, 23), (46, 20), (80, 12), (1, 1999), (90, 33), (101, 23), (34, 88), (103, 0), (1, 1)]

    print(solution(500, 4, gas_stations1) == 4300)
    print(solution(500, 7, gas_stations2) == 410700)
    print(solution(500, 3, gas_stations3) == -1)
    print(solution(100, 20, gas_stations4) == 0)
    print(solution(100, 0, []) == -1)
