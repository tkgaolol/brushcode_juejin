def solution(n: int, H: int, A: int, h: list, a: list) -> int:
    # 创建怪物属性列表，每个元素包含 (血量, 攻击力, 原始索引)
    monsters = [(h[i], a[i], i) for i in range(n)]
    
    # 筛选出可以被初始状态击败的怪物
    valid_monsters = [m for m in monsters if m[0] < H and m[1] < A]
    if not valid_monsters:
        return 0
        
    # 按血量和攻击力排序，确保都是严格递增
    dp = [1] * len(valid_monsters)  # dp[i] 表示以第i个怪物结尾的最长序列长度
    
    for i in range(len(valid_monsters)):
        for j in range(i):
            if (valid_monsters[i][0] > valid_monsters[j][0] and 
                valid_monsters[i][1] > valid_monsters[j][1]):
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp) if dp else 0

if __name__ == '__main__':
    print(solution(3, 4, 5, [1, 2, 3], [3, 2, 1]) == 1)
    print(solution(5, 10, 10, [6, 9, 12, 4, 7], [8, 9, 10, 2, 5]) == 2)
    print(solution(4, 20, 25, [10, 15, 18, 22], [12, 18, 20, 26]) == 3)