def solution(s: str, k: int) -> str:
    # Create transformation rules using a dictionary
    rules = {
        'a': 'bc',
        'b': 'ca',
        'c': 'ab'
    }
    
    # Perform the transformation k times
    for _ in range(k):
        # Transform each character and join them together
        s = ''.join(rules[c] for c in s)
    
    return s

if __name__ == '__main__':
    print(solution("abc", 2) == 'caababbcbcca')
    print(solution("abca", 3) == 'abbcbccabccacaabcaababbcabbcbcca')
    print(solution("cba", 1) == 'abcabc')