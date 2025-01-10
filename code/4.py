def solution(numbers):
    # Please write your code here
    digit_groups = []
    for num in numbers:
        # 将每个数字转为字符串，然后转为集合去重
        digit_groups.append(set(str(num)))
    
    # 递归函数来生成所有可能的组合
    def generate_combinations(groups, current_sum, index):
        if index == len(groups):
            # 如果已经处理完所有组，检查和是否为偶数
            return 1 if current_sum % 2 == 0 else 0
        
        count = 0
        # 遍历当前组中的所有数字
        for digit in groups[index]:
            # 递归处理下一组，累加当前数字
            count += generate_combinations(groups, current_sum + int(digit), index + 1)
        return count
    
    # 从第一组开始，初始和为0
    return generate_combinations(digit_groups, 0, 0)

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([123, 456, 789]) == 14)
    print(solution([123456789]) == 4)
    print(solution([14329, 7568]) == 10)