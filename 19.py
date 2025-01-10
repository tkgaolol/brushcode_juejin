def solution(n: int, k: int, s: str) -> str:
    # 将字符串转换为列表以便操作
    s = list(s)
    operations = k
    
    # 遍历字符串，尽可能将0移到前面
    for i in range(n):
        if operations == 0:
            break
            
        # 如果当前位置是1，寻找后面最近的0
        if s[i] == '1':
            # 查找从i位置开始最近的0
            for j in range(i + 1, min(i + operations + 1, n)):
                if s[j] == '0':
                    # 将这个0移动到位置i
                    for x in range(j, i, -1):
                        s[x], s[x-1] = s[x-1], s[x]
                    # 更新剩余操作次数
                    operations -= (j - i)
                    break
    
    return ''.join(s)

if __name__ == '__main__':
    print(solution(5, 2, "01010") == '00101')
    print(solution(7, 3, "1101001") == '0110101')
    print(solution(4, 1, "1001") == '0101')