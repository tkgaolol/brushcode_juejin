def solution(n: int, u: list) -> int:
    if len(set(u)) == 1:
        return 0
    
    min_level = min(u)
    min_level_count = u.count(min_level)
    
    return n - min_level_count

if __name__ == '__main__':
    print(solution(n = 5, u = [1, 2, 3, 1, 2]) == 3)
    print(solution(n = 4, u = [100000, 100000, 100000, 100000]) == 0)
    print(solution(n = 6, u = [1, 1, 1, 2, 2, 2]) == 3)