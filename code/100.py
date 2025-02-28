def solution(A):
    n = len(A)
    liars = 0
    
    for i in range(n):
        # 统计小于等于当前分数的学生数量
        less_or_equal = sum(1 for x in A if x <= A[i])
        # 统计大于当前分数的学生数量
        greater = n - less_or_equal
        # 如果小于等于的数量大于大于的数量，则该学生说谎
        if less_or_equal > greater:
            liars += 1
            
    return liars


if __name__ == "__main__":
    # Add your test cases here
    print(solution([100, 100, 100]) == 3)
    print(solution([2, 1, 3]) == 2)
    print(solution([30, 1, 30, 30]) == 3)
    print(solution([19, 27, 73, 55, 88]) == 3)
    print(solution([19, 27, 73, 55, 88, 88, 2, 17, 22]) == 5)
