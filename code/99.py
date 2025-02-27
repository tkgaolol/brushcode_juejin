def solution(n, m, a):
    # 模拟分发每个糖果
    for candy in range(m):
        # 创建临时数组来存储当前糖果分配状态
        current = a.copy()
        pos = 0
        
        while pos < n:
            # 给当前小朋友添加糖果
            current[pos] += 1
            
            # 检查是否需要传递给下一个小朋友
            if pos < n - 1:  # 不是最后一个小朋友
                if current[pos] > current[pos + 1]:
                    pos += 1  # 传递给下一个小朋友
                else:
                    # 当前小朋友可以保留糖果
                    if candy == m - 1:  # 如果是最后一颗糖果
                        return pos + 1  # 返回1-based索引
                    # 更新实际的糖果数组
                    a[pos] = current[pos]
                    break
            else:  # 是最后一个小朋友
                # 最后一个小朋友的糖果一定传给小U，因为小U的糖果数可以认为是无限大
                if candy == m - 1:  # 如果是最后一颗糖果
                    return n + 1  # 给小U
                break
        
        # 如果糖果传递完整个队列或传给了最后一个小朋友
        if pos == n - 1:
            if candy == m - 1:  # 如果是最后一颗糖果
                return n + 1  # 返回小U的位置
        elif pos < n - 1:
            # 更新数组状态
            a[pos] = current[pos]
    
    return 0  # 这行代码实际上不会执行到


if __name__ == "__main__":
    # Add your test cases here
    print(solution(4, 3, [1, 2, 3, 4]) == 1)
    print(solution(4, 2, [4, 3, 2, 3]) == 5)
