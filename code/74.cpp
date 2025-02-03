#include <iostream>
#include <string>
#include <vector>

std::string solution(std::vector<int> &plates, int n) {
    std::string result;
    int start = 0;
    
    while (start < n) {
        // Find consecutive sequence
        int end = start;
        while (end + 1 < n && plates[end + 1] == plates[end] + 1) {
            end++;
        }
        
        // Add to result based on sequence length
        if (end - start >= 2) {  // Sequence of 3 or more
            if (!result.empty()) {
                result += ",";
            }
            result += std::to_string(plates[start]) + "-" + std::to_string(plates[end]);
        } else {  // Individual numbers or pairs
            for (int i = start; i <= end; i++) {
                if (!result.empty()) {
                    result += ",";
                }
                result += std::to_string(plates[i]);
            }
        }
        
        start = end + 1;
    }
    
    return result;
}

int main() {
  //  You can add more test cases here
  std::vector<int> plates1 = {-3, -2, -1, 2, 10, 15, 16, 18, 19, 20};
  std::cout << (solution(plates1, 10) == "-3--1,2,10,15,16,18-20") << std::endl;

  std::vector<int> plates2 = {-6, -3, -2, -1, 0,  1,  3,  4,  5,  7,
                              8,  9,  10, 11, 14, 15, 17, 18, 19, 20};
  std::cout << (solution(plates2, 20) == "-6,-3-1,3-5,7-11,14,15,17-20")
            << std::endl;

  std::vector<int> plates3 = {1, 2, 7, 8, 9, 10, 11, 19};
  std::cout << (solution(plates3, 8) == "1,2,7-11,19") << std::endl;

  return 0;
}
