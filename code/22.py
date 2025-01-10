def solution(S: str) -> int:
    # 统计每个字符的出现次数
    char_count = {}
    for c in S:
        char_count[c] = char_count.get(c, 0) + 1
    
    # 计算需要的操作次数
    operations = 0
    total_pairs = 0
    
    # 统计有多少对重复字符需要处理
    for count in char_count.values():
        # 对于每个字符，计算可以形成多少对
        pairs = count // 2
        total_pairs += pairs
    
    # 每次操作处理一对重复字符，并添加一个新字符
    # 如果新添加的字符造成了新的重复，那么在下一轮中会继续处理
    return total_pairs

if __name__ == '__main__':
    print(solution(S = "abab") == 2)
    print(solution(S = "aaaa") == 2)
    print(solution(S = "abcabc") == 3)