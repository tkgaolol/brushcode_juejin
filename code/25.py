def solution(dna1, dna2):
    m = len(dna1)
    n = len(dna2)
    
    # Create a matrix to store the minimum operations
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i  # deletion
    for j in range(n + 1):
        dp[0][j] = j  # insertion
    
    # Fill the dp matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i-1] == dna2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # no operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # deletion
                    dp[i][j-1],    # insertion
                    dp[i-1][j-1]   # replacement
                )
    
    return dp[m][n]

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("AGCTTAGC", "AGCTAGCT") == 2 )
    print(solution("AGCCGAGC", "GCTAGCT") == 4)