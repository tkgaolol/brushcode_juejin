def solution(N, M, data):
    # 使用集合存储可以到达终点的位置
    safe = set()
    # 找到终点位置
    for i in range(N):
        for j in range(M):
            if data[i][j] == 'O':
                safe.add((i, j))
                break
    
    # 记录上一次的安全位置数量
    prev_size = -1
    # 当没有新的安全位置被添加时停止
    while prev_size != len(safe):
        prev_size = len(safe)
        # 检查每个位置
        for i in range(N):
            for j in range(M):
                if (i, j) in safe:
                    continue
                    
                # 检查从当前位置是否可以到达任何安全位置
                can_reach_safe = False
                
                # 如果是传送器，只能传送到指定方向
                if data[i][j] in ['U', 'D', 'L', 'R']:
                    ni, nj = i, j
                    if data[i][j] == 'U' and i > 0:
                        ni = i - 1
                    elif data[i][j] == 'D' and i < N-1:
                        ni = i + 1
                    elif data[i][j] == 'L' and j > 0:
                        nj = j - 1
                    elif data[i][j] == 'R' and j < M-1:
                        nj = j + 1
                    
                    if 0 <= ni < N and 0 <= nj < M and (ni, nj) in safe:
                        can_reach_safe = True
                
                # 如果是普通地板，可以向四个方向移动
                elif data[i][j] == '.':
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M and (ni, nj) in safe:
                            can_reach_safe = True
                            break
                
                if can_reach_safe:
                    safe.add((i, j))
    
    # 返回危险位置的数量
    return N * M - len(safe)


if __name__ == "__main__":
    # Add your test cases here
    pattern = [
        [".",  ".", ".", ".", "."],
        [".",  "R", "R", "D", "."],
        [".", "U", ".", "D", "R"],
        [".", "U", "L", "L", "."],
        [".", ".", ".", ".", "O"]
    ]
    print(solution(5, 5, pattern) == 10)