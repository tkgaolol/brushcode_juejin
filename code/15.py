def solution(S: str, T: str) -> int:
    # 如果S已经是T的前缀，直接返回0
    if T.startswith(S):
        return 0
    
    # 获取两个字符串的长度
    s_len = len(S)
    t_len = len(T)
    
    # 获取需要比较的长度（取较短的字符串长度）
    compare_len = min(s_len, t_len)
    
    # 计算需要修改的字符数
    changes = sum(1 for i in range(compare_len) if S[i] != T[i])
    
    # 如果S比T长，需要加上删除多余字符的操作次数
    if s_len > t_len:
        changes += s_len - t_len
    
    return changes

if __name__ == '__main__':
    print(solution("aba", "abb") == 1)
    print(solution("abcd", "efg") == 4)
    print(solution("xyz", "xy") == 1)
    print(solution("hello", "helloworld") == 0)
    print(solution("same", "same") == 0)