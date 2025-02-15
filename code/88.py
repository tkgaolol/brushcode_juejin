def solution(n, b, sequence):
    # Count the number of contiguous subsequences with sum divisible by b
    count = 0
    
    # For each starting position
    for i in range(n):
        current_sum = 0
        # Try all possible ending positions
        for j in range(i, n):
            current_sum += sequence[j]
            # If the sum is divisible by b, increment count
            if current_sum % b == 0:
                count += 1
    
    return count

if __name__ == "__main__":
    #  You can add more test cases here
    sequence = [1, 2, 3]
    print(solution(3, 3, sequence) == 3)