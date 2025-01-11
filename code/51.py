def solution(n, sums):
    total_sum = sum(sums)

    # Check if total_sum is divisible by (n-1)
    if total_sum % (n - 1) != 0:
        return "Impossible"

    ans = [0] * n
    sums.sort()

    # Iterate from -abs(sums[0]) to abs(sums[0])
    for i in range(-abs(sums[0]), abs(sums[0]) + 1):
        ans[0] = i
        p = {s: sums.count(s) for s in sums}  # Create a frequency map for sums
        idx = 1

        for k in p.keys():
            if p[k] == 0:
                continue
            while p[k] > 0:
                ans[idx] = k - ans[0]

                # Check how many previous indices can create the sum with ans[idx]
                t = 0
                while t < idx:
                    # If combination exists, decrement its count
                    if p.get(ans[idx] + ans[t], 0):
                        p[ans[idx] + ans[t]] -= 1
                    else:
                        break
                    t += 1

                # If all previous pairs were valid
                if t == idx:
                    idx += 1
                else:
                    break

        # If all n elements were successfully filled, break the loop
        if idx == n:
            break

    # Create the result string
    return " ".join(map(str, ans[:-1])) + " " + str(ans[-1])

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, [1269, 1160, 1663]) == "383 777 886")
    print(solution(3, [1, 1, 1]) == "Impossible")
    print(solution(5, [226, 223, 225, 224, 227, 229, 228, 226, 225, 227]) == "111 112 113 114 115")
    print(solution(5, [-1, 0, -1, -2, 1, 0, -1, 1, 0, -1]) == "-1 -1 0 0 1")
    print(solution(5, [79950, 79936, 79942, 79962, 79954, 79972, 79960, 79968, 79924, 79932]) == "39953 39971 39979 39983 39989")