def solution(V: int, W: int) -> str:
    n, m = V, W

    if n <= 5:
        return "YES"

    while m:
        remainder = m % n
        if remainder <= 2:
            m //= n
        elif remainder >= n - 2:
            m = m // n + 1
        else:
            return "NO"

    return "YES"



if __name__ == "__main__":
    # Add your test cases here
    print(solution(10, 9) == "YES")
    print(solution(200, 40199) == "YES")
    print(solution(108, 50) == "NO")