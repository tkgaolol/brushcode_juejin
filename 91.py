def solution(n: int, f: list[list[int]], L: int, R: int) -> int:
    count = 0

    def dfs(index: int, current_product: int):
        nonlocal count
        if index == n:
            if L <= current_product <= R:
                count += 1
            return
        for value in f[index]:
            new_product = current_product * value
            if new_product > R:
                continue  # Prune paths that exceed R
            dfs(index + 1, new_product)

    dfs(0, 1)
    return count


if __name__ == "__main__":
    # Add your test cases here
    print(solution(3, [[1, 2], [3, 4]], 1, 6) == 3)
