def solution(str1):
    n = len(str1)
    
    # 从长度1开始尝试所有可能的前缀
    for length in range(1, n + 1):
        prefix = str1[:length]
        current = prefix
        
        # 模拟追加操作
        while len(current) < n:
            # 尝试所有可能的K值
            found = False
            for k in range(len(current)):
                next_str = current + current[k:]
                if str1.startswith(next_str):
                    current = next_str
                    found = True
                    break
            
            # 如果没有找到有效的K值，说明当前前缀不可能是答案
            if not found:
                break
                
        # 如果生成的字符串等于目标字符串，我们找到了答案
        if current == str1:
            return prefix
            
    # 如果没有找到答案，返回原字符串
    return str1


if __name__ == "__main__":
    # Add your test cases here

    print(solution("abbabbbabb") == "ab")
    print(solution("abbbabbbb") == "ab")
    print(
        solution(
            "jiabanbananananiabanbananananbananananiabanbananananbananananbananananbanananan"
        )
        == "jiaban"
    )
    print(
        solution(
            "selectecttectelectecttectcttectselectecttectelectecttectcttectectelectecttectcttectectcttectectcttectectcttect"
        )
        == "select"
    )
    print(
        solution(
            "discussssscussssiscussssscussssdiscussssscussssiscussssscussssiscussssscussss"
        )
        == "discus"
    )
