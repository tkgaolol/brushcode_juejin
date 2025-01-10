def solution(n: int, a: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here.
    count = 0
    for i in a:
        b = str(i)
        count += len(b)
        if b.count(str(0)) > 0:
            count -= b.count(str(0))
    return count

if __name__ == '__main__':
    print(solution(5, [10, 13, 22, 100, 30]) == 7)
    print(solution(3, [5, 50, 505]) == 4)
    print(solution(4, [1000, 1, 10, 100]) == 4)