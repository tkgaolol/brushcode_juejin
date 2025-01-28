#include <iostream>
#include <vector>

int solution(int d, int w, std::vector<int> position, std::vector<int> supply) {
    // Please write your code here
    int n = position.size();
    int curr_pos = 0;  // 当前位置
    int water = w;     // 当前水量
    int refills = 0;   // 补给次数
    int i = 0;         // 当前考虑的补给站索引
    
    // 如果初始水量就足够到达终点，直接返回0
    if (w >= d) return 0;
    
    while (curr_pos + water < d) {
        int max_supply = -1;
        int chosen_idx = -1;
        
        // 在当前水量可以到达的范围内寻找供水量最大的补给站
        while (i < n && position[i] <= curr_pos + water) {
            if (supply[i] > max_supply) {
                max_supply = supply[i];
                chosen_idx = i;
            }
            i++;
        }
        
        // 如果找不到可以到达的补给站，返回-1
        if (chosen_idx == -1) return -1;
        
        // 移动到选中的补给站
        water -= (position[chosen_idx] - curr_pos);
        curr_pos = position[chosen_idx];
        water += max_supply;
        refills++;
    }
    
    return refills;
}

int main() {
    //  You can add more test cases here
    std::vector<int> testPosition = {170, 192, 196, 234, 261, 269, 291, 404, 1055, 1121, 1150, 1234, 1268, 1402, 1725, 1726, 1727, 1762, 1901, 1970};
    std::vector<int> testSupply = {443, 185, 363, 392, 409, 358, 297, 70, 189, 106, 380, 130, 126, 411, 63, 186, 36, 347, 339, 50};

    std::cout << (solution(10, 4, std::vector<int>{1, 4, 7}, std::vector<int>{6, 3, 5}) == 1) << std::endl;
    std::cout << (solution(2000, 200, testPosition, testSupply) == 5) << std::endl;

    return 0;
}