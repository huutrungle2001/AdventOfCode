#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const vector<pair<int, int>> DIRECTIONS = {
    {0, 1},   // right
    {0, -1},  // left
    {1, 0},   // down
    {-1, 0},  // up
    {1, 1},   // down right
    {1, -1},  // down left
    {-1, 1},  // up right
    {-1, -1}  // up left
};

class Solution {
   private:
    vector<string> grid;
    int numRows;
    int numCols;

   public:
    Solution(vector<string> grid) {
        this->grid = grid;
        numRows = grid.size();
        numCols = grid.front().size();
    }

    void solve() {
        size_t sum = 0;
        for (int i = 0; i < numRows; i++) {
            size_t num = 0;
            bool isValid = false;
            for (int j = 0; j < numCols; j++) {
                if (isDigit(grid[i][j])) {
                    num = num * 10 + toInt(grid[i][j]);
                    if (!isValid) {
                        isValid = isAdjacent(i, j);
                    }
                } else {
                    if (isValid) {
                        cout << num << endl;
                        sum += num;
                    }
                    num = 0;
                    isValid = false;
                }
            }

            if (isValid) {
                cout << num << endl;
                sum += num;
            }
        }

        cout << "Total: " << sum << endl;
    }

    bool isDigit(char c) {
        return c >= '0' && c <= '9';
    }

    int toInt(char c) {
        return c - '0';
    }

    bool isValidPos(int x, int y) {
        return x >= 0 && x < numRows &&
               y >= 0 && y < numCols;
    }

    bool isAdjacent(int x, int y) {
        for (auto dir : DIRECTIONS) {
            int newX = x + dir.first;
            int newY = y + dir.second;
            if (isValidPos(newX, newY) &&
                !isDigit(grid[newX][newY]) &&
                grid[newX][newY] != '.') {
                return true;
            }
        }
        return false;
    }
};

int main() {
    ifstream input("input.txt");
    vector<string> grid;
    string line;
    while (getline(input, line)) {
        grid.push_back(line);
    }

    Solution solution(grid);
    solution.solve();

    return 0;
}