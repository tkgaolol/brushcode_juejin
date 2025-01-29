#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

std::string solution(std::vector<int> nums, int k) {
  // 使用哈希表统计每个数字的频率
  std::unordered_map<int, int> freq;
  for (int num : nums) {
    freq[num]++;
  }

  // 创建桶，index为频率，value为具有该频率的数字列表
  std::vector<std::vector<int>> bucket(nums.size() + 1);
  for (const auto &pair : freq) {
    bucket[pair.second].push_back(pair.first);
  }

  // 收集前k个高频元素
  std::vector<int> result;
  for (int i = bucket.size() - 1; i >= 0 && result.size() < k; i--) {
    if (!bucket[i].empty()) {
      // 对同频率的数字进行排序
      std::sort(bucket[i].begin(), bucket[i].end());
      result.insert(result.end(), bucket[i].begin(),
                    bucket[i].begin() + std::min((int)bucket[i].size(),
                                                 k - (int)result.size()));
    }
  }

  // 对结果进行排序
  std::sort(result.begin(), result.end());

  // 构建返回字符串
  std::string ans;
  for (int i = 0; i < result.size(); i++) {
    ans += std::to_string(result[i]);
    if (i < result.size() - 1) {
      ans += ",";
    }
  }

  return ans;
}

int main() {
  //  You can add more test cases here
  std::vector<int> nums1 = {1, 1, 1, 2, 2, 3};
  std::vector<int> nums2 = {1};

  std::cout << (solution(nums1, 2) == "1,2") << std::endl;
  std::cout << (solution(nums2, 1) == "1") << std::endl;

  return 0;
}