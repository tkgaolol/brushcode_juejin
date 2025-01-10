def solution(n: int, s: list, x: list) -> list:
    # 创建字典来统计每个人的总金额
    total_amounts = {}
    for i, name in enumerate(s):
        total_amounts[name] = total_amounts.get(name, 0) + x[i]
    
    # 创建包含名字和总金额的元组列表，使用第一次出现的索引
    name_amounts = [(name, total_amounts[name], i) for i, name in enumerate(total_amounts.keys())]
    # 按总金额降序排序，金额相同时按首次出现的索引升序排序
    name_amounts.sort(key=lambda x: (-x[1], x[2]))
    # 返回排序后的名字列表
    return [name for name, _, _ in name_amounts]

if __name__ == '__main__':
    print(solution(4, ["a", "b", "c", "d"], [1, 2, 2, 1]) == ['b', 'c', 'a', 'd'])
    print(solution(3, ["x", "y", "z"], [100, 200, 200]) == ['y', 'z', 'x'])
    print(solution(5, ["m", "n", "o", "p", "q"], [50, 50, 30, 30, 20]) == ['m', 'n', 'o', 'p', 'q'])