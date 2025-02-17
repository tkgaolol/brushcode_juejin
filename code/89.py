def solution(n, k, sequence):
    count = 0
    # 遍历所有可能的子序列起点
    for start in range(n):
        curr_max = float('-inf')
        curr_min = float('inf')
        # 从每个起点开始，尝试扩展子序列
        for end in range(start, n):
            # 更新当前子序列的最大值和最小值
            curr_max = max(curr_max, sequence[end])
            curr_min = min(curr_min, sequence[end])
            # 检查是否是迷人数列
            if curr_max - curr_min <= k:
                count += 1
            else:
                break
    return count

if __name__ == "__main__":
    #  You can add more test cases here
    sequence1 = [3, 1, 2, 4]
    sequence2 = [7, 3, 5, 1, 9]
    sequence3 = [2, 2, 3, 1, 1, 2]

    print(solution(4, 2, sequence1) == 8)
    print(solution(5, 3, sequence2) == 6)
    print(solution(6, 1, sequence3) ==12)