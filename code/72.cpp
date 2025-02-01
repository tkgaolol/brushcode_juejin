#include <iostream>
#include <string>
#include <vector>

std::string solution(int num, std::string data) {
    std::vector<int> forces(num, 0);

    // Apply forces from 'R'
    int force = 0;
    for (int i = 0; i < num; ++i) {
        if (data[i] == 'R') {
            force = num; // Start with a large force
        } else if (data[i] == 'L') {
            force = 0; // Reset force when 'L' is encountered
        } else {
            force = std::max(force - 1, 0); // Decrease force over distance
        }
        forces[i] += force;
    }

    // Apply forces from 'L'
    force = 0;
    for (int i = num - 1; i >= 0; --i) {
        if (data[i] == 'L') {
            force = num; // Start with a large force
        } else if (data[i] == 'R') {
            force = 0; // Reset force when 'R' is encountered
        } else {
            force = std::max(force - 1, 0); // Decrease force over distance
        }
        forces[i] -= force;
    }

    // Determine upright dominos
    std::vector<int> upright_positions;
    for (int i = 0; i < num; ++i) {
        if (forces[i] == 0) {
            upright_positions.push_back(i + 1); // Convert to 1-based index
        }
    }

    // Format the result
    std::string result = std::to_string(upright_positions.size());
    if (!upright_positions.empty()) {
        result += ":";
        for (size_t i = 0; i < upright_positions.size(); ++i) {
            result += std::to_string(upright_positions[i]);
            if (i < upright_positions.size() - 1) {
                result += ",";
            }
        }
    }

    return result;
}

int main() {
    //  You can add more test cases here
    std::cout << (solution(14, ".L.R...LR..L..") == "4:3,6,13,14") << std::endl;
    std::cout << (solution(5, "R....") == "0") << std::endl;
    std::cout << (solution(1, ".") == "1:1") << std::endl;

    return 0;
}