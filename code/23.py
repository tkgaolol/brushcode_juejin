def solution(stones):
    # Handle single stone case
    if len(stones) == 1:
        return 0
    
    # Sort the stones
    stones.sort()
    n = len(stones)
    
    # Calculate maximum possible moves
    max_moves = max(stones[n-1] - stones[1], stones[n-2] - stones[0]) - (n-2)
    
    # Calculate minimum moves using sliding window
    min_moves = float('inf')
    j = 0
    
    for i in range(n):
        # Ensure window contains at most n stones
        while j < n and stones[j] - stones[i] + 1 <= n:
            j += 1
            
        # Special case: if window contains n-1 stones and gap is 1
        already_in_place = j - i
        if already_in_place == n - 1 and stones[j-1] - stones[i] + 1 == n - 1:
            min_moves = min(min_moves, 2)
        else:
            min_moves = min(min_moves, n - already_in_place)
    
    return max_moves

if __name__ == '__main__':
    print(solution(stones=[7, 4, 9]) == 2)
    print(solution(stones=[6, 5, 4, 3, 10]) == 3)
    print(solution(stones=[1, 2, 3, 4, 5]) == 0)