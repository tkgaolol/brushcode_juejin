#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>

int solution(std::string data) {
    std::vector<int> numbers;
    std::stringstream ss(data);
    std::string token;
    
    // Parse the comma-separated string into numbers
    while (std::getline(ss, token, ',')) {
        numbers.push_back(std::stoi(token));
    }
    
    // Sort the numbers
    std::sort(numbers.begin(), numbers.end());
    
    // Calculate the 80th percentile position (round off)
    int position = static_cast<int>(std::round(numbers.size() * 0.8)) - 1;
    
    return numbers[position];
}

int main() {
    //  You can add more test cases here
    std::cout << (solution("10,1,9,2,8,3,7,4,6,5") == 8) << std::endl;
    std::cout << (solution("1,0,8,7,3,9,12,6,4,15,17,2,14,5,10,11,19,13,16,18") == 15) << std::endl;
    std::cout << (solution("76,100,5,99,16,45,18,3,81,65,102,98,36,4,2,7,22,66,112,97,68,82,37,90,61,73,107,104,79,14,52,83,27,35,93,21,118,120,33,6,19,85,49,44,69,53,67,110,47,91,17,55,80,78,119,15,11,70,103,32,9,40,114,26,25,87,74,1,30,54,38,50,8,34,28,20,24,105,106,31,92,59,116,42,111,57,95,115,96,108,10,89,23,62,29,109,56,58,63,41,77,84,64,75,72,117,101,60,48,94,46,39,43,88,12,113,13,51,86,71") == 96) << std::endl;
    return 0;
}