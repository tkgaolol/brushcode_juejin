#include <iostream>
#include <vector>
#include <algorithm>
int solution(std::vector<std::vector<int>> inputArray) {
    // 如果数组为空，返回0
    if (inputArray.empty()) return 0;
    
    // 按照区间起始位置排序
    sort(inputArray.begin(), inputArray.end());
    
    // 存储合并后的区间
    std::vector<std::vector<int>> merged;
    merged.push_back(inputArray[0]);
    
    // 合并重叠区间
    for (int i = 1; i < inputArray.size(); i++) {
        if (merged.back()[1] >= inputArray[i][0]) {
            // 如果有重叠，更新当前区间的结束位置
            merged.back()[1] = std::max(merged.back()[1], inputArray[i][1]);
        } else {
            // 如果没有重叠，添加新区间
            merged.push_back(inputArray[i]);
        }
    }
    
    // 计算所有区间内的数字总数
    int total = 0;
    for (const auto& interval : merged) {
        total += interval[1] - interval[0] + 1;
    }
    
    return total;
}

int main() {
    //  You can add more test cases here
    std::vector<std::vector<int>> testArray1 = {{1, 4}, {7, 10}, {3, 5}};
    std::vector<std::vector<int>> testArray2 = {{1, 2}, {6, 10}, {11, 15}};

    std::cout << (solution(testArray1) == 9) << std::endl;
    std::cout << (solution(testArray2) == 12) << std::endl;

    return 0;
}