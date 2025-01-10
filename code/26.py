def solution(a: int, b: int) -> int:
    a_str = str(a)
    b_str = str(b)

    # Start with the smallest possible number, which is negative infinity
    max_number = -float('inf')

    # Try inserting b at every possible position in a
    for i in range(len(a_str) + 1):
        # Create a new number by inserting b at position i
        new_number = int(a_str[:i] + b_str + a_str[i:])
        # Update max_number if the new number is larger
        if new_number > max_number:
            max_number = new_number

    return max_number

if __name__ == '__main__':
    print(solution(76543, 4) == 765443)
    print(solution(1, 0) == 10)
    print(solution(44, 5) == 544)
    print(solution(666, 6) == 6666)