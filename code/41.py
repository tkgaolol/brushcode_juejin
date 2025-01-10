def solution(input):
    n = len(input)
    target_freq = n // 4  # 每个字符应该出现的次数
    
    # 统计每个字符的出现次数
    freq = {'A': 0, 'S': 0, 'D': 0, 'F': 0}
    for c in input:
        freq[c] += 1
    
    # 如果所有字符出现次数都相等，返回0
    if all(f == target_freq for f in freq.values()):
        return 0
    
    # 计算需要替换的最小次数
    changes_needed = 0
    for count in freq.values():
        if count != target_freq:
            changes_needed += abs(count - target_freq)

    return changes_needed // 2
if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("ADDF") == 1 )
    print(solution("ASAFASAFADDD") == 3)