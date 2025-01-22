#include <iostream>
#include <vector>


int stepx[4] = {0, 1, 0, -1};
int stepy[4] = {1, 0, -1, 0};
 
int check(int x, int y, int row, int column) {
  if (x < 0 || x >= row || y < 0 || y >= column) {
    return 0;
  }
  return 1;
}
 
int solution(int row_n, int column_m, std::vector<std::vector<int>> seats,
             std::vector<int> patient) {
    // Please write your code here
    int now1[101][101] = {{0}};
    int now2[101][101] = {{0}};
    if (!check(patient[0], patient[1], row_n, column_m)) 
    {
        return 0;
    }
    if (row_n == 1 && column_m == 1) 
    {
        return 0;
    }
    now1[patient[0]][patient[1]] = 2;
    now2[patient[0]][patient[1]] = 2;
    int i = 0, j = 0, sum = 0, k = 0, tx = 0, ty = 0;
    while (true) 
    {
        sum++;
        for (i = 0; i < row_n; i++) 
        {
            for (j = 0; j < column_m; j++) 
            {
                if (now1[i][j] >= 2) 
                {
                    for (k = 0; k < 4; k++) 
                    {
                        tx = i + stepx[k];
                        ty = j + stepy[k];
                        if (check(tx, ty, row_n, column_m)) 
                        {
                            if (seats[tx][ty] == 0) 
                            {
                                now2[tx][ty] = 2;
                            } 
                            else if (seats[tx][ty] == 1) 
                            {
                                now2[tx][ty]++;
                            }
                        }
                    }
                }
            }
        }
        int a = 0;
        for (i = 0; i < row_n; i++) 
        {
            for (j = 0; j < column_m; j++) 
            {
                now1[i][j] = now2[i][j];
                if (now2[i][j] < 2) 
                {
                    a = 1;
                }
            }
        }
        if (!a) 
        {
            return sum;
        }
    }
}

int main() {
    //  You can add more test cases here
    std::vector<std::vector<int>> testSeats1 = {{0,1,1,1},{1,0,1,0},{1,1,1,1},{0,0,0,1}};
    std::vector<std::vector<int>> testSeats2 = {{0,1,1,1},{1,0,1,0},{1,1,1,1},{0,0,0,1}};
    std::vector<std::vector<int>> testSeats3 = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
    std::vector<std::vector<int>> testSeats4 = {{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,1}};
    std::vector<std::vector<int>> testSeats5 = {{1}};

    std::cout << (solution(4, 4, testSeats1, {2, 2}) == 6) << std::endl;
    std::cout << (solution(4, 4, testSeats2, {2, 5}) == 0) << std::endl;
    std::cout << (solution(4, 4, testSeats3, {2, 2}) == 4) << std::endl;
    std::cout << (solution(4, 4, testSeats4, {2, 2}) == 6) << std::endl;
    std::cout << (solution(1, 1, testSeats5, {0, 0}) == 0) << std::endl;

    return 0;
}