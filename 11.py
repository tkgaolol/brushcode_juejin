def solution(values: list) -> int:
    max_score = 0
    max_i_value = values[0]  # Initialize with the first element's value + index (0)
    
    for j in range(1, len(values)):
        # Calculate the score for the current pair (i, j)
        max_score = max(max_score, max_i_value + values[j] - j)
        
        # Update max_i_value for the next iteration
        max_i_value = max(max_i_value, values[j] + j)
    
    return max_score

if __name__ == '__main__':
    print(solution(values=[8, 3, 5, 5, 6]) == 11)
    print(solution(values=[10, 4, 8, 7]) == 16)
    print(solution(values=[1, 2, 3, 4, 5]) == 8)