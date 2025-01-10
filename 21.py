def solution(n: int, a: list) -> int:
    max_contribution = 0
    
    # Check all possible pairs of indices
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate shortest distance in circular array
            # For circular array, distance is min of:
            # 1. Direct distance: j - i
            # 2. Distance going through the wrap-around: n - (j - i)
            distance = min(j - i, n - (j - i))
            
            # Calculate contribution using the formula
            contribution = (a[i] + a[j]) * distance
            
            # Update maximum contribution if current is larger
            max_contribution = max(max_contribution, contribution)
    
    return max_contribution

if __name__ == '__main__':
    print(solution(n = 3, a = [1, 2, 3]) == 5)
    print(solution(n = 4, a = [4, 1, 2, 3]) == 12)
    print(solution(n = 5, a = [1, 5, 3, 7, 2]) == 24)