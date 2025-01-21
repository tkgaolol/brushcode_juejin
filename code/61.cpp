#include <iostream>
#include <vector>

#include <queue>
#include <climits>
int solution(std::vector<int> airports) {
    int n = airports.size();
    if (n <= 1) return 0;
    
    // 使用BFS查找最短路径
    std::vector<int> dist(n, INT_MAX);
    std::queue<int> q;
    
    // 从起点开始
    dist[0] = 0;
    q.push(0);
    
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        
        // 检查相邻机场
        for (int next = curr - 1; next <= curr + 1; next += 2) {
            if (next >= 0 && next < n && dist[next] == INT_MAX) {
                dist[next] = dist[curr] + 1;
                q.push(next);
            }
        }
        
        // 检查相同航空公司的机场
        for (int next = 0; next < n; next++) {
            if (next != curr && airports[next] == airports[curr] && dist[next] == INT_MAX) {
                dist[next] = dist[curr] + 1;
                q.push(next);
            }
        }
    }
    
    // 如果无法到达终点，返回-1
    return dist[n-1] == INT_MAX ? -1 : dist[n-1];
}

int main() {
    //  You can add more test cases here
    std::vector<int> airports1 = {10, 12, 13, 12, 14};
    std::vector<int> airports2 = {10, 11, 12, 13, 14};

    std::cout << (solution(airports1) == 3) << std::endl;
    std::cout << (solution(airports2) == 4) << std::endl;
    return 0;
}