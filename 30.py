def solution(s: str) -> int:
    # 将字符串转换为小写，方便统计
    s = s.lower()
    
    # 统计k和u的数量
    k_count = s.count('k')
    u_count = s.count('u')
    
    # 返回可以组成的"ku"对数（取决于k和u中数量较少的那个）
    return min(k_count, u_count)

if __name__ == '__main__':
    print(solution("AUBTMKAxfuu") == 1)
    print(solution("KKuuUuUuKKKKkkkkKK") == 6)
    print(solution("abcdefgh") == 0)