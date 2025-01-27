#include <cmath>
#include <iostream>
#include <string>
std::string solution(int n) {
  // Please write your code here
  if (n == 1)
    return "1.00000";
  double prob = floor((n + 1) / 2.0) / n;

  // Format result to exactly 5 decimal places
  char buffer[32];
  sprintf(buffer, "%.5f", prob);
  return buffer;
}

int main() {
  //  You can add more test cases here
  std::cout << (solution(2) == "0.50000") << std::endl;
  std::cout << (solution(931) == "0.50054") << std::endl;
  std::cout << (solution(924) == "0.50000") << std::endl;
  std::cout << (solution(545) == "0.50092") << std::endl;

  return 0;
}