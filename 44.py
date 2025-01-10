def solution(x: int, y: int) -> int:
    # 计算射击点到原点的距离（使用勾股定理）
    distance = (x*x + y*y) ** 0.5
    
    # 向上取整，得到点所在的环数
    ring = int(distance + 0.99999)
    
    # 如果环数大于10，返回0分
    if ring > 10:
        return 0
        
    # 否则返回 11-ring 分
    return 11 - ring

if __name__ == '__main__':
    print(solution(1, 0) == 10)
    print(solution(1, 1) == 9)
    print(solution(0, 5) == 6)
    print(solution(3, 4) == 6)