def solution(s: str) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    n = len(s)
    # Create a palindrome by mirroring the first half
    t = list(s[:(n + 1) // 2] + s[:n // 2][::-1])
    
    if ''.join(t) < s:
        return ''.join(t)
    
    # Try to adjust the palindrome
    for i in range((n - 1) // 2, -1, -1):
        if t[i] > 'a':
            t[i] = chr(ord(t[i]) - 1)
            t[n - i - 1] = t[i]
            for j in range(i + 1, (n + 1) // 2):
                t[j] = 'z'
                t[n - j - 1] = 'z'
            if ''.join(t) < s:
                return ''.join(t)
    
    return '-1'
if __name__ == '__main__':
    print(solution("abc") == 'aba')
    print(solution("cba") == 'cac')
    print(solution("aaa") == '-1')