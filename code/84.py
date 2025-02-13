def solution(n: int, k: int, num_str: str) -> int:
    # Please write your code here
    if k == 0:
        return int(num_str) % 1000000007
    new_str = []
    for i in range(len(num_str)):
        tempint = int(num_str[len(num_str)-i-1]) + 1
        if tempint < 10:
            new_str.append(str(tempint))
        else:
            new_str.append(str(tempint%10))
            new_str.append(str(tempint//10))
    new_str = new_str[::-1]
    new_str = ''.join(new_str)
    return solution(n, k-1, new_str)

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, 1, "798") == 8109)
    print(solution(3, 3, "798") == 103221)
