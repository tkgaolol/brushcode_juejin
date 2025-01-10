def solution(word: str) -> int:
    # 将所有字母替换为空格
    processed = ''.join(' ' if c.isalpha() else c for c in word)
    
    # 分割字符串获取所有数字部分
    numbers = processed.split()
    
    # 使用集合去重，同时将每个数字字符串转换为整数（这样会自动去除前导零）
    # 然后再转回字符串用于比较
    unique_numbers = {str(int(num)) for num in numbers}
    
    return len(unique_numbers)

if __name__ == '__main__':
    print(solution("a123bc34d8ef34") == 3)
    print(solution("t1234c23456") == 2)
    print(solution("a1b01c001d4") == 2)