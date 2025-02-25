def solution(n, k, inp):
    left = 0
    right = 0
    max_length = 0
    count = {}

    while right < n:
        if inp[right] not in count:
            count[inp[right]] = 0
        count[inp[right]] += 1
        
        # Check if we need to modify characters
        while len(count) > 2:
            check = sum(sorted(count.values(), reverse=True)[2:])
            if check <= k:
                break
            count[inp[left]] -= 1
            if count[inp[left]] == 0:
                del count[inp[left]]
            left += 1
        
        # Calculate the number of modifications needed
        total_chars = right - left + 1
        max_count = max(count.values())
        modifications_needed = total_chars - max_count
        
        max_length = max(max_length, total_chars)
        
        right += 1

    return max_length


if __name__ == "__main__":
    # Add your test cases here

    print(solution(6, 1, "ABCBAD") == 5)
    print(solution(5, 1, "AEABD") == 4)
    print(solution(24, 15, "EORIAXEJDVSBGODQXQIRAZFI") == 19)
