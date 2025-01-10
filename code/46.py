def solution(string1, string2):
    # 将两个大数字符串相加
    num1 = int(string1)
    num2 = int(string2)
    result = str(num1 + num2)
    
    # 如果结果中所有数字都相同，返回0
    if len(set(result)) == 1:
        return 0
        
    # 找出最大和最小数字
    max_digit = max(result)
    min_digit = min(result)
    
    # 获取最大数字和最小数字的所有位置
    max_positions = [i for i, d in enumerate(result) if d == max_digit]
    min_positions = [i for i, d in enumerate(result) if d == min_digit]
    
    # 计算最小位置差
    min_diff = float('inf')
    for max_pos in max_positions:
        for min_pos in min_positions:
            diff = abs(max_pos - min_pos) - 1
            min_diff = min(min_diff, diff)
    
    return min_diff

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("111", "222") == 0 )
    print(solution("111", "34") == 1)
    print(solution("5976762424003073", "6301027308640389") == 6)