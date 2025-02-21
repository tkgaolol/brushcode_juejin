
#include <vector>
#include <iostream>

#include <cmath>
#include <algorithm>
 
using namespace std;
int solution(int n, int k, const std::vector<int>& b, const std::vector<int>& c) {
    // 动态规划数组
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    // 记录每个英雄达到目标所需要的升级次数
    vector<int> step(n + 1, 0);
    
    // 计算每个英雄的升级次数
    for (int i = 1; i <= n; i++) {
        double a_i = 1;
        int x = 1;
        while (a_i != b[i - 1]) {
            if (a_i + floor(a_i / x) <= b[i - 1]) {
                step[i]++;
                a_i = a_i + floor(a_i / x);
            } else if (a_i + floor(a_i / x) > b[i - 1]) {
                x++;
            }
        }
    }
 
    // 初始化DP数组
    for (int j = 0; j <= k; j++) {
        dp[0][j] = 0;
    }
    for (int z = 1; z <= n; z++) {
        if (step[z] == 0) {
            dp[z][0] = c[z - 1] + dp[z - 1][0];
        } else {
            dp[z][0] = dp[z - 1][0];
        }
    }
 
    // 动态规划计算最大奖励
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            if (j < step[i]) {
                dp[i][j] = dp[i - 1][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - step[i]] + c[i - 1]);
            }
        }
    }
 
    return dp[n][k];
}


int main() {
    // Add your test cases here
    std::cout << (solution(4, 4, {1, 7, 5, 2}, {2, 6, 5, 2}) == 9) << std::endl;
    std::cout << (solution(3, 0, {3, 5, 2}, {5, 4, 7}) == 0) << std::endl;
    return 0;
}
