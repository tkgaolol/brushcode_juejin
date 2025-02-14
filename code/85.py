def solution(n: int, m: int, k: int, a: list[int], b: list[int]) -> int:
    min_diff = float('inf')
    k_squared = k * k
    
    # 遍历所有可能的 a[i] 和 b[j] 组合
    for i in range(n):
        for j in range(m):
            # 计算 (a[i]-b[j])²
            diff_squared = (a[i] - b[j]) * (a[i] - b[j])
            # 计算 |(a[i]-b[j])² - k²|
            current_diff = abs(diff_squared - k_squared)
            # 更新最小值
            min_diff = min(min_diff, current_diff)
            
            # 如果找到差值为0，可以直接返回
            if min_diff == 0:
                return 0
                
    return min_diff

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(5, 5, 1, [5, 3, 4, 1, 2], [0, 6, 7, 9, 8]) == 0)
    print(solution(5, 5, 0, [5, 3, 4, 1, 2], [0, 6, 7, 9, 8]) == 1)
    print(solution(5, 6, 3, [5, 3, 4, 1, 2], [0, 6, 7, 9, 8, 11]) == 0)
