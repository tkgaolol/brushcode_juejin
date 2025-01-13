def solution(expression):
    def calculate(s, i):
        stack = []
        num = 0
        sign = '+'
        
        while i < len(s):
            c = s[i]
            
            if c.isdigit():
                num = num * 10 + int(c)
            
            if c == '(':
                num, next_i = calculate(s, i + 1)
                i = next_i
            
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # 处理负数除法
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(-prev // num))
                    else:
                        stack.append(prev // num)
                
                sign = c
                num = 0
                
                if c == ')':
                    return sum(stack), i
            
            i += 1
        
        return sum(stack), i
    
    result, _ = calculate(expression, 0)
    return result

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("1+1") == 2)
    print(solution("3+4*5/(3+2)") == 7)
    print(solution("4+2*5-2/1") == 12)
    print(solution("(1+(4+5+2)-3)+(6+8)") == 23)