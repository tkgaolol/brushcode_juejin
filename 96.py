def solution(n, data):
    days = 0
    data = list(data)  # 将字符串转换为列表以便修改
    while True:
        new_data = data[:]  # 复制当前状态
        changed = False
        
        for i in range(n):
            # 检查当前学生与相邻学生的颜色
            if data[i] == data[(i - 1) % n] == data[(i + 1) % n]:
                new_data[i] = '1' if data[i] == '0' else '0'  # 颜色翻转
                changed = True
        
        days += 1
        data = new_data
        
        # 如果没有变化，达到稳定状态
        if not changed:
            break
        
        # 如果经过 n 次循环仍未稳定，返回 -1
        if days > n:
            return [-1, -1]
    
    # 计算“时尚达人”的数量
    fashionistas = sum(1 for i in range(n) if data[i] != data[(i - 1) % n] and data[i] != data[(i + 1) % n])
    
    return [days, fashionistas]


if __name__ == "__main__":
    # Add your test cases here
    print(solution(4, "0000") == [-1, -1])
    print(solution(4, "1110") == [2, 4])
