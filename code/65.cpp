#include <iostream>
#include <vector>
#include <algorithm>

int solution(int k, int p, std::vector<std::vector<int>> target) {
    // Please write your code here
    std::vector<std::vector<int>> sorted_target = target;
    std::sort(sorted_target.begin(), sorted_target.end());
    int shootcount = 0;
    int shootstart = sorted_target[0][0];
    int shootend = sorted_target[0][1];
    int i = 0;
    while(i < sorted_target.size()) {
        if(sorted_target[i][0] >= shootstart and sorted_target[i][1] <= shootend) {
            shootstart = sorted_target[i][0];
            shootend = sorted_target[i][1];
        } else if(sorted_target[i][0] <= shootend and sorted_target[i][1] >= shootend) {
            shootstart = sorted_target[i][0];
        } else {
            shootstart = sorted_target[i][0];
            shootend = sorted_target[i][1];
            shootcount++;
        }
        i++;
    }
    shootcount++;
    return shootcount%p;

}

int main() {
    //  You can add more test cases here
    std::vector<std::vector<int>> testTarget1 = {
        {10, 26, 3},
        {4, 8, 29},
        {1, 5, 8},
        {9, 9, 9}
    };
    std::vector<std::vector<int>> testTarget2 = {
        {10, 26, 3},
        {4, 8, 29},
        {1, 5, 8}
    };
    std::vector<std::vector<int>> testTarget3 = {
        {13, 20, 2},
        {15, 39, 3},
        {34, 89, 6},
        {2, 10, 1},
        {0, 87, 2},
        {23, 49, 3},
        {2, 45, 9},
        {9, 98, 0},
        {3, 12, 9},
        {35, 45, 21},
        {51, 67, 23},
        {37, 42, 54},
        {55, 76, 7},
        {2, 13, 6},
        {29, 31, 9},
        {10, 32, 1}
    };

    std::cout << (solution(4, 100, testTarget1) == 3) << std::endl;
    std::cout << (solution(3, 100, testTarget2) == 2) << std::endl;
    std::cout << (solution(16, 100, testTarget3) == 5) << std::endl;

    return 0;
}