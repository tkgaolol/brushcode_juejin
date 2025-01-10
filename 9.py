def solution(n: int, m: int, s: str, c: str) -> int:
    from collections import Counter
    
    # Count occurrences of each item in the shelf and customer's list
    shelf_count = Counter(s)
    customer_count = Counter(c)
    
    # Calculate the maximum number of items that can be sold
    max_sold = 0
    for item in customer_count:
        if item in shelf_count:
            max_sold += min(shelf_count[item], customer_count[item])
    
    return max_sold

if __name__ == '__main__':
    print(solution(3, 4, "abc", "abcd") == 3)
    print(solution(4, 2, "abbc", "bb") == 2)
    print(solution(5, 4, "bcdea", "abcd") == 4)