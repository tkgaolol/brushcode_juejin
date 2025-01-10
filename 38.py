def solution(m: int, n: int, p: list[list[int]]) -> int:
    # Initialize a list to store the minimum cost to reach each day
    dp = [float('inf')] * (m + 1)
    dp[0] = 0  # Starting point, no cost on day 0

    # Iterate over each day
    for i in range(1, m + 1):
        # Check each supply station
        for j in range(n):
            day, cost = p[j]
            if day <= i:
                # Calculate the cost if we buy food from this station
                dp[i] = min(dp[i], dp[day] + (i - day) * cost)

    return dp[m]


if __name__ == "__main__":
    # Add your test cases here

    print(solution(5, 4, [[0, 2], [1, 3], [2, 1], [3, 2]]) == 7)
