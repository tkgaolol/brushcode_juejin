#include <iostream>
#include <string>

int solution(std::string rgb) {
    int r = 0, g = 0, b = 0;
    size_t pos = 4; // 跳过"rgb("
    
    // 解析红色值
    while (rgb[pos] != ',') {
        if (isdigit(rgb[pos])) {
            r = r * 10 + (rgb[pos] - '0');
        }
        pos++;
    }
    
    // 跳过", "
    pos += 2;
    
    // 解析绿色值
    while (rgb[pos] != ',') {
        if (isdigit(rgb[pos])) {
            g = g * 10 + (rgb[pos] - '0');
        }
        pos++;
    }
    
    // 跳过", "
    pos += 2;
    
    // 解析蓝色值
    while (rgb[pos] != ')') {
        if (isdigit(rgb[pos])) {
            b = b * 10 + (rgb[pos] - '0');
        }
        pos++;
    }
    
    return (r << 16) + (g << 8) + b;
}

int main() {
    //  You can add more test cases here
    std::cout << (solution("rgb(192, 192, 192)") == 12632256) << std::endl;
    std::cout << (solution("rgb(100, 0, 252)") == 6553852) << std::endl;
    std::cout << (solution("rgb(33, 44, 55)") == 2174007) << std::endl;
    return 0;
}