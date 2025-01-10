def solution(x_position, y_position):
    # 如果起点等于终点，返回0
    if x_position == y_position:
        return 0
    
    # 计算需要移动的总距离
    distance = abs(y_position - x_position)
    
    # 从1开始尝试不同的步数
    steps = 1
    while True:
        # 计算使用当前步数能达到的最大距离
        max_distance = 0
        current_step = 1  # 第一步必须是1
        
        # 模拟每一步可能达到的最大距离
        for i in range(steps):
            max_distance += min(i + 1, steps - i)  # 考虑步长限制
            
        if max_distance >= distance:
            return steps
            
        steps += 1

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(12, 6) == 4 )
    print(solution(34, 45) == 6)
    print(solution(50, 30) == 8)