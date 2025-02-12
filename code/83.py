def solution(Q, V, ships):
    # Initialize a list to store the maximum cargo capacity for each budget value
    dp = [0] * (V + 1)
    
    # Iterate over each type of ship
    for m, v, w in ships:
        # For each ship type, consider renting up to m ships
        for _ in range(m):
            # Update the dp array in reverse to avoid overwriting results
            for j in range(V, v - 1, -1):
                dp[j] = max(dp[j], dp[j - v] + w)
    
    # The maximum cargo capacity within the budget V is stored in dp[V]
    return dp[V]

if __name__ == "__main__":
    #  You can add more test cases here
    ships = [[2, 3, 2], [3, 2, 10]]
    ships2 = [[30, 141, 47], [9, 258, 12], [81, 149, 13], [91, 236, 6], [27, 163, 74], [34, 13, 58], [61, 162, 1], [80, 238, 29], [36, 264, 28], [36, 250, 2], [70, 214, 31], [39, 116, 39], [83, 287, 4], [61, 269, 94], [23, 187, 46], [78, 33, 29], [46, 151, 2], [71, 249, 1], [67, 76, 85], [72, 239, 17], [61, 256, 49], [48, 216, 73], [39, 49, 74]]
    print(solution(2, 10, ships) == 32)
    print(solution(23, 400, ships2) == 1740)