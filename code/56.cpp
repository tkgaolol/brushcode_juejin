#include <iostream>
#include <vector>

int solution(int n, std::vector<int> cats_levels) {
    // Please write your code here
    std::vector<int> candies(n, 1);

    // 从左向右遍历，确保等级高的猫比左边的猫获得更多鱼干
    for (int i = 1; i < n; i++) {
        if (cats_levels[i] > cats_levels[i-1]) {
            candies[i] = candies[i-1] + 1;
        }
    }

    // 从右向左遍历，确保等级高的猫比右边的猫获得更多鱼干
    for (int i = n-2; i >= 0; i--) {
        if (cats_levels[i] > cats_levels[i+1]) {
            candies[i] = std::max(candies[i], candies[i+1] + 1);
        }
    }

    // 计算总和
    int total = 0;
    for (int candy : candies) {
        total += candy;
    }

    return total;
}

int main() {
  std::vector<int> catsLevels1 = {1, 2, 2};
  std::vector<int> catsLevels2 = {6, 5, 4, 3, 2, 16};
  std::vector<int> catsLevels3 = {1, 2, 2, 3, 3, 20, 1, 2, 3, 3,
                                  2, 1, 5, 6, 6, 5,  5, 7, 7, 4};
  std::cout << (solution(3, catsLevels1) == 4) << std::endl;
  std::cout << (solution(6, catsLevels2) == 17) << std::endl;
  std::cout << (solution(20, catsLevels3) == 35) << std::endl;
  return 0;
}