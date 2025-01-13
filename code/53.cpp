#include <iostream>
#include <vector>
using namespace std;

const long long MOD = 202220222022LL;

string solution(int n) {
    n += 3;
    vector<long long> old_dp(21, 0); // optimized space from a large array to only up to score 20
    old_dp[0] = 1;
    
    for (int i = 1; i <= n; ++i) {
        int MaxScore = 20 * i;
        vector<long long> new_dp(MaxScore + 1, 0);
        for (int j = 0; j <= MaxScore; ++j) {
            for (int k = 0; k <= 20; ++k) {
                if (j - k >= 0 && j - k <= (i - 1) * 20) {
                    new_dp[j] = (new_dp[j] + old_dp[j - k]) % MOD;
                } else if (j - k < 0) {
                    break;
                }
            }
        }
        old_dp = new_dp;
    }

    long long ans = 0;
    for (int i = 12 * n; i <= 20 * n; ++i) {
        ans = (ans + old_dp[i]) % MOD;
    }
    return to_string(ans);
}


int main() {
    // You can add more test cases here
    cout << (solution(3) == "19195617") << endl;
    cout << (solution(6) == "135464411082") << endl;
    cout << (solution(49) == "174899025576") << endl;
    cout << (solution(201) == "34269227409") << endl;
    cout << (solution(888) == "194187156114") << endl;

    return 0;
}