def solution(dna_sequence):
    n = len(dna_sequence)
    # 将原始序列复制一遍，方便处理循环
    doubled = dna_sequence + dna_sequence
    min_seq = dna_sequence
    
    # 尝试从每个位置开始的序列
    for i in range(n):
        # 获取长度为n的子串
        current = doubled[i:i+n]
        # 如果当前序列字典序更小，则更新结果
        if current < min_seq:
            min_seq = current
            
    return min_seq

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("ATCA") == "AATC")
    print(solution("CGAGTC") == "AGTCCG")
    print(solution("TCATGGAGTGCTCCTGGAGGCTGAGTCCATCTCCAGTAG") == "AGGCTGAGTCCATCTCCAGTAGTCATGGAGTGCTCCTGG")