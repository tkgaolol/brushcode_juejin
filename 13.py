def solution(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        result.extend(range(n, i - 1, -1))
    return result

if __name__ == '__main__':
    print(solution(3) == [3, 2, 1, 3, 2, 3])
    print(solution(4) == [4, 3, 2, 1, 4, 3, 2, 4, 3, 4])
    print(solution(5) == [5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5])