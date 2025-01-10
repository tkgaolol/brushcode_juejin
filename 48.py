def solution(s: str) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    result = ""
    for i in s:
        if i == 'a':
            result += '%100'
        else:
            result += i
    return result

if __name__ == '__main__':
    print(solution(s="abcdwa") == '%100bcdw%100')
    print(solution(s="banana") == 'b%100n%100n%100')
    print(solution(s="apple") == '%100pple')