def solution(cards):
    # Edit your code here
    unique_number = 0
    for card in cards:
        unique_number ^= card
    return unique_number


if __name__ == "__main__":
    # Add your test cases here

    print(solution([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)
    print(solution([0, 1, 0, 1, 2]) == 2)