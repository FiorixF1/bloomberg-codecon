//Problem        : Finals Spring 2015 - Maze Solver
//Language       : C++14
//Compiled Using : g++
//Version        : GCC 4.9.1
//Input for your program will be provided from STDIN
//Print out all output from your program to STDOUT

#include <iostream>
#include <string>
#include <algorithm>
#include <climits> 
#include <vector>

using namespace std;

struct coord {
    int x;
    int y;
};

vector<coord> ans;

bool find_path(vector<string> &maze, int R, int C, int curr_r, int curr_c) {
    if (curr_r == R-2 && curr_c == C-1) {
        maze[curr_r][curr_c] = '-';
        coord res;
        res.x = curr_r;
        res.y = curr_c;
        ans.push_back(res);
        return true;
    } else if (curr_r < 0 || curr_r >= R || curr_c < 0 || curr_c >= C || maze[curr_r][curr_c] == 'X') {
        return false;
    } else if (maze[curr_r][curr_c] == '-') {
        return false;
    } else {
        maze[curr_r][curr_c] = '-';
        coord res;
        res.x = curr_r;
        res.y = curr_c;
        ans.push_back(res);
        if (find_path(maze, R, C, curr_r-1, curr_c)) {
            return true;
        } else if (find_path(maze, R, C, curr_r, curr_c+1)) {
            return true;
        } else if (find_path(maze, R, C, curr_r+1, curr_c)) {
            return true;
        } else if (find_path(maze, R, C, curr_r, curr_c-1)) {
            return true;
        } else {
            maze[curr_r][curr_c] = '_';
            ans.pop_back();
            return false;
        }
    }
}

int main() {
    int R, C;
    cin >> R >> C;
    vector<string> maze;
    for (int i = 0; i < R; ++i) {
        string row;
        cin >> row;
        maze.push_back(row);
    }
    bool FOUND = find_path(maze, R, C, 1, 0);
    for (coord c : ans) {
        cout << c.x << ',' << c.y << endl;
    }
    return 0;
}

