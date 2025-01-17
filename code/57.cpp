#include <iostream>
#include <vector>

int solution(std::vector<int> redpacks) {
    // Please write your code here
    int n = redpacks.size();
    if (n <= 3) 
    {
        return 0;
    }
    int left = 0;
    int right = n - 1;
    int result = 0;
    std::vector<int> dp(n+1, 0);
    for (int i = 0; i < n; i++)
    {
        dp[i+1] = dp[i] + redpacks[i];
    }

    for (int i = 0; i < n-2; i++)
    {
        for (int j = i; j < n-1; j++)
        {
            int first = dp[i+1];
            int third = dp[n] - dp[j+1];
            if (first == third)
            {
                result = std::max(result, first);
            }
        }
    }

    return result;

}

int main() {
    // You can add more test cases here
    std::vector<int> redpacks1 = {1, 3, 4, 6, 7, 14};
    std::vector<int> redpacks2 = {10000};
    std::vector<int> redpacks3 = {52, 13, 61, 64, 42, 26, 4, 27, 25};
    std::vector<int> redpacks4 = {2, 5, 50, 30, 60, 52, 26, 5, 74, 83, 34, 96, 6, 88, 94, 80, 64, 22, 97, 47, 46, 25, 24, 43, 76, 24, 2, 42, 51, 96, 97, 87, 47, 93, 11, 98, 41, 54, 18, 16, 11, 96, 34, 36, 87, 24, 32, 27, 62, 72, 54, 14, 67, 5, 21, 20, 44, 55, 3, 82, 19, 45, 1, 52, 14, 44, 46, 39, 83, 27, 30, 87, 61, 56, 59, 10, 83, 80, 42, 44, 75, 39, 43, 41, 23, 93, 73, 50, 94, 94, 82, 46, 87, 60, 94, 47, 52, 67, 22, 50, 49, 8, 9, 30, 62, 87, 13, 11};

    std::cout << (solution(redpacks1) == 14) << std::endl;
    std::cout << (solution(redpacks2) == 0) << std::endl;
    std::cout << (solution(redpacks3) == 52) << std::endl;
    std::cout << (solution(redpacks4) == 2627) << std::endl;

    return 0;
}