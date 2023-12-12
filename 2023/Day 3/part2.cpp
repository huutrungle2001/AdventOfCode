#include <fstream>
#include <iostream>
#include <map>
#include <set>
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
    map<pair<int, int>, vector<int>> gearsRatio;

   public:
    Solution(vector<string> grid) {
        this->grid = grid;
        numRows = grid.size();
        numCols = grid.front().size();
    }

    void solve() {
        for (int i = 0; i < numRows; i++) {
            size_t num = 0;
            set<pair<int, int>> neighborGears;
            for (int j = 0; j < numCols; j++) {
                if (isDigit(grid[i][j])) {
                    num = num * 10 + toInt(grid[i][j]);
                    for (auto &gear : getNeighborGears(i, j)) {
                        neighborGears.insert(gear);
                    }
                } else {
                    for (auto &gear : neighborGears) {
                        gearsRatio[gear].push_back(num);
                    }
                    num = 0;
                    neighborGears.clear();
                }
            }

            for (auto &gear : neighborGears) {
                gearsRatio[gear].push_back(num);
            }
        }

        int sum = 0;
        for (auto &[gear, ratio] : gearsRatio) {
            if (ratio.size() == 2) {
                sum += ratio.front() * ratio.back();
            }
        }

        cout << sum << endl;
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

    vector<pair<int, int>> getNeighborGears(int x, int y) {
        vector<pair<int, int>> neighbors;
        for (auto &dir : DIRECTIONS) {
            int newX = x + dir.first;
            int newY = y + dir.second;
            if (isValidPos(newX, newY) &&
                !isDigit(grid[newX][newY]) &&
                grid[newX][newY] != '.') {
                neighbors.push_back({newX, newY});
            }
        }
        return neighbors;
    }

    bool isAdjacent(int x, int y) {
        for (auto &dir : DIRECTIONS) {
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