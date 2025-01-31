#include <iostream>
#include <algorithm>


int solution(int m, int w, int p, int n) {
    long long cakes = 0;
    int days = 0;
    int min_days = (n + m * w - 1) / (m * w); // Initial estimate of days

    while (cakes < n) {
        // Calculate the number of days needed to afford at least one more machine or worker
        if (cakes < p) {
            int days_to_wait = (p - cakes + m * w - 1) / (m * w);
            cakes += static_cast<long long>(days_to_wait) * m * w;
            days += days_to_wait;
        }

        // Calculate the maximum number of machines or workers we can buy
        long long total_units = cakes / p;
        cakes %= p;

        // Balance machines and workers
        if (m < w) {
            int to_add = static_cast<int>(std::min(total_units, static_cast<long long>(w - m)));
            m += to_add;
            total_units -= to_add;
        } else {
            int to_add = static_cast<int>(std::min(total_units, static_cast<long long>(m - w)));
            w += to_add;
            total_units -= to_add;
        }

        // If there are still units left, distribute them evenly
        long long half = total_units / 2;
        m += static_cast<int>(half);
        w += static_cast<int>(total_units - half);

        // Produce cakes for the day
        cakes += static_cast<long long>(m) * w;
        days++;

        // Update the minimum days required
        min_days = std::min(min_days, days + static_cast<int>((n - cakes + m * w - 1) / (m * w)));
    }

    return min_days;
}

int main() {
    //  You can add more test cases here
    std::cout << (solution(3, 1, 2, 12) == 3) << std::endl;
    std::cout << (solution(10, 5, 30, 500) == 8) << std::endl;
    std::cout << (solution(3, 5, 30, 320) == 14) << std::endl;

    return 0;
}