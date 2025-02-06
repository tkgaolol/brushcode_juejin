def solution(n, k, array_a):
    def count_quality_chapters(left, right):
        # 计算指定区间内的优质章节数
        if right - left < 2:  # 区间长度小于3时没有优质章节
            return 0
        count = 0
        for i in range(left + 1, right):
            # 优质章节需要比前后章节都多
            if array_a[i] > array_a[i-1] and array_a[i] > array_a[i+1]:
                count += 1
        return count

    max_quality = 0  # 最大优质章节数
    best_left = 0    # 最优区间左边界
    best_right = 0   # 最优区间右边界
    min_sum = float('inf')  # 最小总字数

    # 遍历所有可能的区间
    for left in range(n):
        curr_sum = 0
        for right in range(left, n):
            curr_sum += array_a[right]
            if curr_sum > k:  # 如果超过总字数限制，跳出内循环
                break

            quality_count = count_quality_chapters(left, right)

            # 更新最优解
            if (quality_count > max_quality or
                (quality_count == max_quality and curr_sum < min_sum) or
                    (quality_count == max_quality and curr_sum == min_sum and left < best_left)):
                max_quality = quality_count
                best_left = left
                best_right = right
                min_sum = curr_sum

    return f"{max_quality},{best_left + 1},{best_right + 1}"


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(8, 15000, [1000, 3000, 2000,
          4000, 3000, 2000, 4000, 2000]) == "2,1,5")
    print(solution(8, 15000, [2000, 5000, 2000,
          1000, 4000, 2000, 4000, 3000]) == "2,4,8")
