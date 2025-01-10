def solution(m: int, s: str) -> int:
    n = len(s)
    dp = [[-1] * (m + 1) for _ in range(n + 1)] 
    dp[0][0] = 0 

    match_info = [[] for _ in range(n)] 
    for i in range(n):
        max_len = min(n - i, 3 + m) 
        dp_match = [[float('inf')] * (max_len + 1) for _ in range(4)] 
        dp_match[0][0] = 0
        for p in range(4):  
            for q in range(max_len + 1):  
                if dp_match[p][q] > m:  
                    continue
                if p < 3 and q < max_len:  
                    cost = 0 if s[i + q] == 'UCC'[p] else 1
                    dp_match[p + 1][q + 1] = min(dp_match[p + 1][q + 1], dp_match[p][q] + cost)
                if p < 3: 
                    dp_match[p + 1][q] = min(dp_match[p + 1][q], dp_match[p][q] + 1)
                if q < max_len: 
                    dp_match[p][q + 1] = min(dp_match[p][q + 1], dp_match[p][q] + 1)

        for q in range(max_len + 1):
            c = dp_match[3][q]
            match_info[i].append((c, q))  
 
    for i in range(n + 1):
        for e in range(m + 1):
            if dp[i][e] == -1:
                continue
            if i < n:  
                dp[i + 1][e] = max(dp[i + 1][e], dp[i][e]) 
                if e + 1 <= m:  
                    dp[i + 1][e + 1] = max(dp[i + 1][e + 1], dp[i][e])            
            if i < n and match_info[i]: 
                for c, l in match_info[i]:  
                    if e + c <= m and i + l <= n:
                        dp[i + l][e + c] = max(dp[i + l][e + c], dp[i][e] + 1)
 
    max_substrings = 0
    for e in range(m + 1):
        max_substrings = max(max_substrings, dp[n][e])
    return max_substrings


if __name__ == '__main__':
    print(solution(m=3, s="UCUUCCCCC") == 3)
    print(solution(m=6, s="U") == 2)
    print(solution(m=2, s="UCCUUU") == 2)