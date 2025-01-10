def get_prime_factors(n):
    factors = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return factors

def solution(n: int, a: list) -> str:
    # 获取所有数的素因子
    all_factors = set()
    num_factors = []
    
    for num in a:
        if num == 1:  # 1没有素因子
            num_factors.append(set())
            continue
        factors = get_prime_factors(num)
        num_factors.append(factors)
        all_factors.update(factors)
    
    # 如果素因子种类总数大于数组长度，无法实现目标
    if len(all_factors) > n:
        return "No"
    
    # 检查每个数的素因子是否可以通过操作变成单一素因子
    for factors in num_factors:
        if len(factors) > 1:  # 如果某个数有多个素因子
            # 只要数组中有其他数，就可以通过操作转移素因子
            continue
            
    return "Yes"

if __name__ == '__main__':
    print(solution(4, [1, 2, 3, 4]) == "Yes")
    print(solution(2, [10, 12]) == "No")
    print(solution(3, [6, 9, 15]) == "Yes")