def solution(n, max, array):
    # Edit your code here

    count = {}
    for num in array:
        count[num] = count.get(num, 0) + 1
    
    # 找出所有出现3次或以上的数字
    three_cards = [num for num, freq in count.items() if freq >= 3]
    # 找出所有出现2次或以上的数字
    two_cards = [num for num, freq in count.items() if freq >= 2]
    
    # 如果没有足够的牌组成葫芦，返回[0, 0]
    if not three_cards or len(two_cards) < (2 if len(three_cards) == 1 else 1):
        return [0, 0]
    
    result = [0, 0]
    max_three = 0
    max_two = 0

    # 遍历所有可能的组合
    def compare_with_one_as_largest(a, b):
        if a == 1 and b != 1:
            return 1
        if b == 1 and a != 1:
            return -1
        return a - b

    # 遍历所有可能的组合
    for three in three_cards:
        for two in two_cards:
            # 跳过相同的数字
            if three == two:
                # 确保有足够的相同牌
                if count[three] < 5:
                    continue
            # 计算总和
            total = three * 3 + two * 2
            if total <= max:
                # 根据规则比较大小
                current_better = False
                if compare_with_one_as_largest(three, max_three) > 0:
                    current_better = True
                elif three == max_three and compare_with_one_as_largest(two, max_two) > 0:
                    current_better = True
                
                if current_better:
                    max_three = three
                    max_two = two
                    result = [three, two]
    return result


if __name__ == "__main__":
    # Add your test cases here

    print(solution(9, 34, [6, 6, 6, 8, 8, 8, 5, 5, 1]) == [8, 5])
    print(solution(9, 37, [9, 9, 9, 9, 6, 6, 6, 6, 13]) == [6, 9])
    print(solution(31, 42, [3,3,11,12,12,2,13,5,13,1,13,8,8,1,8,13,12,9,2,11,3,5,8,11,1,11,1,5,4,2,5]) == [1,13])
