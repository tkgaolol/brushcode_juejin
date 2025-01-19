#include <iostream>
#include <string>

#include <map>
#include <tuple>

// Helper function to implement memoized DFS
std::pair<std::string, int> dfs(const std::string& s, int flag, int a, int b, int c, 
    std::map<std::tuple<std::string, int>, std::pair<std::string, int>>& memo) {
    
    // Create key for memoization
    auto key = std::make_tuple(s, flag);
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }

    int res = 0;
    std::string final_s = s;

    for (int i = 0; i < s.length(); i++) {
        // Check for adjacent 1's
        if (i < s.length()-1 && s[i] == '1' && s[i+1] == '1' && flag != 2) {
            std::string new_s = s.substr(0, i) + s.substr(i+1);
            auto [ss, result] = dfs(new_s, 2, a, b, c, memo);
            if (res < result + b) {
                final_s = ss;
                res = result + b;
            }
        }
        // Check for adjacent 0's
        else if (i < s.length()-1 && s[i] == '0' && s[i+1] == '0' && flag != 1) {
            std::string new_s = s.substr(0, i) + s.substr(i+1);
            auto [ss, result] = dfs(new_s, 1, a, b, c, memo);
            if (res < result + a) {
                final_s = ss;
                res = result + a;
            }
        }
        // Check for single 0
        else if (s[i] == '0' && flag != 1) {
            std::string new_s = s.substr(0, i) + s.substr(i+1);
            auto [ss, result] = dfs(new_s, 1, a, b, c, memo);
            if (res < result - c) {
                final_s = ss;
                res = result - c;
            }
        }
    }

    memo[key] = {final_s, res};
    return {final_s, res};
}

int solution(int n, int a, int b, int c, std::string s) {
    std::map<std::tuple<std::string, int>, std::pair<std::string, int>> memo;
    auto [final_s, res] = dfs(s, -1, a, b, c, memo);
    std::cout << final_s << std::endl;
    return res;
}

int main() {
    //  You can add more test cases here
    std::cout << (solution(5, 2, 2, 1, "01101") == 3) << std::endl;
    std::cout << (solution(6, 4, 3, 5, "110001") == 11) << std::endl;
    std::cout << (solution(6, 3, 2, 1, "011110") == 4) << std::endl;
    return 0;
}