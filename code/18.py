def solution(m: int, n: int, a: list) -> int:
    # 定义方向：上、下、左、右
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    max_steps = [0]  # 使用列表存储最大步数，便于在递归中修改
    
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n
    
    def dfs(x, y, prev_height, is_up_next, steps):
        max_steps[0] = max(max_steps[0], steps)
        
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            
            if (is_valid(next_x, next_y) and 
                (next_x, next_y) not in visited):
                
                curr_height = a[next_x][next_y]
                # 检查是否符合上坡/下坡的要求
                if (is_up_next and curr_height > prev_height) or \
                   (not is_up_next and curr_height < prev_height):
                    visited.add((next_x, next_y))
                    dfs(next_x, next_y, curr_height, not is_up_next, steps + 1)
                    visited.remove((next_x, next_y))
    
    # 从每个点开始尝试
    for i in range(m):
        for j in range(n):
            visited.add((i, j))
            # 尝试从当前点开始向上走
            dfs(i, j, a[i][j], True, 0)
            # 尝试从当前点开始向下走
            dfs(i, j, a[i][j], False, 0)
            visited.remove((i, j))
    
    return max_steps[0]

if __name__ == '__main__':
    print(solution(2, 2, [[1, 2], [4, 3]]) == 3)
    print(solution(3, 3, [[10, 1, 6], [5, 9, 3], [7, 2, 4]]) == 8)
    print(solution(4, 4, [[8, 3, 2, 1], [4, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]) == 11)