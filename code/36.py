def solution(s: str, a: list, m: int, k: int) -> int:
    n = len(s)
    if k > n:  # 如果需要选择的菜品数量大于总菜品数量
        return -1
    
    # 创建包含价格和是否含蘑菇信息的菜品列表
    dishes = [(a[i], int(s[i])) for i in range(n)]
    dishes.sort()  # 按价格排序
    
    # 尝试所有可能的k个菜品组合
    min_total = float('inf')
    from itertools import combinations
    
    for combo in combinations(range(n), k):
        total_price = 0
        mushroom_count = 0
        for idx in combo:
            total_price += dishes[idx][0]  # 加上价格
            mushroom_count += dishes[idx][1]  # 统计蘑菇数量
        
        if mushroom_count <= m:  # 如果蘑菇数量符合要求
            min_total = min(min_total, total_price)
    
    return min_total if min_total != float('inf') else -1

if __name__ == '__main__':
    print(solution("001", [10, 20, 30], 1, 2) == 30)
    print(solution("111", [10, 20, 30], 1, 2) == -1)
    print(solution("0101", [5, 15, 10, 20], 2, 3) == 30)