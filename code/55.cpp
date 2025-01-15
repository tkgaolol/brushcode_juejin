#include <iostream>
#include <string>

#include <bits/stdc++.h>

std::string solution(std::string binary1, std::string binary2) {
    // Please write your code here
    std::string result;
    int carry = 0;
    int i = binary1.size() - 1;
    int j = binary2.size() - 1;

    while( i>=0 || j>=0 || carry)
    {
        int sum = carry;


        if(i>=0)
        {
            sum += binary1[i] - '0';
            i--;
        }
        if(j>=0)
        {
            sum += binary2[j] - '0';
            j--;
        }
        carry= sum / 2;

        result.push_back((sum%2) + '0');
        

    }
    reverse(result.begin(), result.end());
    long long decimalSum = stoll(result, 0, 2);
    return std::to_string(decimalSum);

}

int main() {
    // You can add more test cases here
    std::cout << (solution("101", "110") == "11") << std::endl;
    std::cout << (solution("111111", "10100") == "83") << std::endl;
    std::cout << (solution("111010101001001011", "100010101001") == "242420") << std::endl;
    std::cout << (solution("111010101001011", "10010101001") == "31220") << std::endl;

    return 0;
}