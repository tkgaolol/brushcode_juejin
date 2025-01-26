#include <iostream>
#include <vector>
#include <climits>
int solution(int n, int m, int s, std::vector<int> like) {
    // 输入验证
    if (n <= 0 || m < 0 || s <= 0 || like.size() != n) {
        return 0;
    }

    // dp[i][j][k] represents number of ways to achieve sum i
    // using j magic wands and considering first k desserts
    std::vector<std::vector<std::vector<long long>>> dp(
        s + 1,
        std::vector<std::vector<long long>>(
            m + 1,
            std::vector<long long>(n + 1, 0)
        )
    );
    
    // Base case: empty sum is possible with 0 wands and 0 desserts
    dp[0][0][0] = 1;
    
    // Helper function to calculate factorial
    auto factorial = [](int x) -> long long {
        if (x > 20) return LLONG_MAX; // Prevent excessive calculations
        long long result = 1;
        for(int i = 2; i <= x; i++) {
            result *= i;
            if (result > LLONG_MAX) return LLONG_MAX; // 如果已经超过目标和，提前返回
        }
        return result;
    };
    
    // For each dessert
    for(int k = 0; k < n; k++) {
        // For each possible sum
        for(int i = 0; i <= s; i++) {
            // For each number of wands
            for(int j = 0; j <= m; j++) {
                if(dp[i][j][k] == 0) continue;
                
                // Don't use this dessert
                if (dp[i][j][k+1] + dp[i][j][k] >= LLONG_MAX) {
                    dp[i][j][k+1] = LLONG_MAX;
                } else {
                    dp[i][j][k+1] += dp[i][j][k];
                }
                
                // Use this dessert without magic wand
                if(i + like[k] <= s) {
                    if (dp[i + like[k]][j][k+1] + dp[i][j][k] >= LLONG_MAX) {
                        dp[i + like[k]][j][k+1] = LLONG_MAX;
                    } else {
                        dp[i + like[k]][j][k+1] += dp[i][j][k];
                    }
                }
                
                // Use this dessert with magic wand
                if(j < m) {
                    long long factorial_value = factorial(like[k]);
                    if(factorial_value <= s && i + factorial_value <= s) {
                        if (dp[i + factorial_value][j+1][k+1] + dp[i][j][k] >= LLONG_MAX) {
                            dp[i + factorial_value][j+1][k+1] = LLONG_MAX;
                        } else {
                            dp[i + factorial_value][j+1][k+1] += dp[i][j][k];
                        }
                    }
                }
            }
        }
    }
    
    // Sum up all ways to achieve target sum s using any number of wands
    long long result = 0;
    for(int j = 0; j <= m; j++) {
        if (result + dp[s][j][n] >= INT_MAX) {
            return 0;  // 如果结果超过 INT_MAX，返回0
        }
        result += dp[s][j][n];
    }
    return static_cast<int>(result);
}

int main() {
    //  You can add more test cases here
    std::vector<int> like1 = {1, 2, 3};
    std::vector<int> like2 = {1, 1, 1};
    std::vector<int> like3 = {18,18,8,15,8,15};

    std::cout << (solution(3, 2, 6, like1) == 5) << std::endl;
    std::cout << (solution(3, 1, 1, like2) == 6) << std::endl;
    std::cout << (solution(6, 14, 24, like3) == 0) << std::endl;
    return 0;
}