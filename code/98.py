def solution(n, k, p):
    # 计算第k次增殖后，第p个位置的数字
    
    # 计算第k次增殖后序列的长度
    def get_length(num, times):
        if times == 0:
            return 1
        length = 0
        for i in range(1, num + 1):
            length += get_length(i, times - 1)
        return length
    
    # 递归找到第p个位置的数字
    def find_number(num, times, pos):
        # 如果不需要增殖，直接返回数字
        if times == 0:
            return num if pos == 1 else -1
            
        # 计算当前位置之前的所有数字
        current_pos = 0
        for i in range(1, num + 1):
            # 计算当前数字i经过times-1次增殖后的长度
            length = get_length(i, times - 1)
            
            if current_pos + length >= pos:
                # 找到了包含目标位置的数字
                return find_number(i, times - 1, pos - current_pos)
            current_pos += length
            
        return -1
    
    return find_number(n, k, p)


if __name__ == "__main__":
    # Add your test cases here
    print(solution(4, 3, 19) == 3)
