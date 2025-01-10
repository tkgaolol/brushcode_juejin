def solution(n: int, k: int) -> int:
    # 创建一个结果数组来存储我们选择的数
    result = []
    current = k  # 从k开始，因为所有数必须是k的倍数
    
    # 找到n个互不相同的k的倍数
    while len(result) < n:
        if current % k == 0:  # 如果当前数是k的倍数
            result.append(current)
        current += 1
            
    # 返回数组元素之和
    return sum(result)

if __name__ == '__main__':
    print(solution(n = 3, k = 1) == 6)
    print(solution(n = 2, k = 2) == 6)
    print(solution(n = 4, k = 3) == 30)