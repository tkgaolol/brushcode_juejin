#include <iostream>
#include <vector>
#include <algorithm>

int solution(int number, std::vector<int> heroes) {
    // Please write your code here
    int ans = 0; // 记录总数
    // 先对英雄的能力值进行排序
    sort(heroes.begin(), heroes.end());
    int j = 0;
    for(int i = 0; i < number; i++) {
        for(; j < number; j++) {
            if(heroes[j] > i + 1) {
                ans++;
                j++;
                break;
            }
        }
    }
    
    return ans;
}


int main() {
    //  You can add more test cases here
    std::vector<int> heroes1 = {10,1,1,1,5,5,3};
    std::vector<int> heroes2 = {1,1,1,1,1};
    std::vector<int> heroes3 = {1,2,3,4,5,6,7,8,9,10};

    std::cout << (solution(7, heroes1) == 4) << std::endl;
    std::cout << (solution(5, heroes2) == 0) << std::endl;
    std::cout << (solution(10, heroes3) == 9) << std::endl;

    return 0;
}