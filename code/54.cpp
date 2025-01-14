#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solution(int num) {
    // Please write your code here
    string s = to_string(num);
    int n = s.length();

    vector<int> dp(n+1, 0);
    dp[0] = 1;
    dp[1] = 1;

    for(int i = 2; i<=n; i++)
    {
        dp[i] = dp[i-1];

        int x = (s[i-2] - '0') * 10 + (s[i-1] - '0');
        if (x>=10 && x<=25)
            dp[i] += dp[i-2]; 
    }

    return dp[n];
}

int main() {
    // You can add more test cases here
    std::cout << (solution(12258) == 5) << std::endl;
    std::cout << (solution(1400112) == 6) << std::endl;
    std::cout << (solution(2110101) == 10) << std::endl;

    return 0;
}