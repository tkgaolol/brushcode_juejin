def solution(n, k, nums):
    # 如果数组长度等于k，直接返回数组和
    if n == k:
        return sum(nums)
    
    max_sum = float('-inf')
    
    # 尝试删除每个位置的元素
    for i in range(n):
        # 创建删除i位置元素后的新数组
        temp = nums[:i] + nums[i+1:]
        
        # 计算所有长度为k的子数组和
        for j in range(len(temp) - k + 1):
            curr_sum = sum(temp[j:j+k])
            max_sum = max(max_sum, curr_sum)
    
    return max_sum


if __name__ == "__main__":
    # Add your test cases here
    print(solution(5, 3, [2, 1, 3, -1, 4]) == 8)
