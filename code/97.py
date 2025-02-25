def solution(n: int, arr: list[int]) -> list[int]:
    max_product = float('-inf')
    start_index = 0
    end_index = 0

    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= arr[j]
            if current_product > max_product:
                max_product = current_product
                start_index = i
                end_index = j
            elif current_product == max_product:
                if i < start_index or (i == start_index and j < end_index):
                    start_index = i
                    end_index = j

    return [start_index + 1, end_index + 1]


if __name__ == "__main__":
    # Add your test cases here
    print(solution(5, [1, 2, 4, 0, 8]) == [1, 3])
    print(solution(7, [1, 2, 4, 8, 0, 256, 0]) == [6, 6])
