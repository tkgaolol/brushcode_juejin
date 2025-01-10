def solution(array):
    # Initialize candidate and count
    candidate = None
    count = 0
    
    # Phase 1: Find a candidate
    for num in array:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    # Phase 2: Verify the candidate
    if array.count(candidate) > len(array) // 2:
        return candidate
    else:
        return None


if __name__ == "__main__":
    # Add your test cases here

    print(solution([1, 3, 8, 2, 3, 1, 3, 3, 3]) == 3)
