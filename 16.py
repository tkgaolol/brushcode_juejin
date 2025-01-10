def solution(n, array):
    # Edit your code here

    max_area = 0
    
    # 遍历所有可能的 k（连续元素个数）
    for k in range(1, n + 1):
        # 遍历所有可能的起始位置
        for i in range(n - k + 1):
            # 获取连续 k 个元素中的最小值
            min_height = min(array[i:i + k])
            # 计算当前矩形面积
            area = k * min_height
            # 更新最大面积
            max_area = max(max_area, area)
    
    return max_area


if __name__ == "__main__":
    # Add your test cases here

    print(solution(5, [1, 2, 3, 4, 5]) == 9)
