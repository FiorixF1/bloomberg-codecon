//Problem        : Finals Spring 2015 - Ring of Fungi
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
#include <map>
#include <set>

using namespace std;

void fill(vector<vector<long>> &bin, long H, long W, long start_i, long start_j, long old_char, long new_char, bool doScan, vector<long> &mySet) {
    if (bin[start_i][start_j] != old_char) {
        if (doScan) {
            mySet.push_back(start_i);
            mySet.push_back(start_j);
        }
        return;
    }
    bin[start_i][start_j] = new_char;

    // sopra
    if (start_i != 0)
        fill(bin, H, W, start_i-1, start_j, old_char, new_char, doScan, mySet);
    // alto destra
    if (start_i != 0 && start_j != W-1)
        fill(bin, H, W, start_i-1, start_j+1, old_char, new_char, doScan, mySet);
    // destra
    if (start_j != W-1)
        fill(bin, H, W, start_i, start_j+1, old_char, new_char, doScan, mySet);
    // basso destra
    if (start_i != H-1 && start_j != W-1)
        fill(bin, H, W, start_i+1, start_j+1, old_char, new_char, doScan, mySet);
    // sotto
    if (start_i != H-1)
        fill(bin, H, W, start_i+1, start_j, old_char, new_char, doScan, mySet);
    // basso sinistra
    if (start_i != H-1 && start_j != 0)
        fill(bin, H, W, start_i+1, start_j-1, old_char, new_char, doScan, mySet);
    // sinistra
    if (start_j != 0)
        fill(bin, H, W, start_i, start_j-1, old_char, new_char, doScan, mySet);
    // alto sinistra
    if (start_j != 0 && start_i != 0)
        fill(bin, H, W, start_i-1, start_j-1, old_char, new_char, doScan, mySet);
}

int main() {
    long H, W, N;
    cin >> H >> W >> N;
    
    vector<vector<long>> bin;
    for (long h = 0; h < H; ++h) {
        vector<long> row;
        for (long w = 0; w < W; ++w) {
            row.push_back(0);
        }
        bin.push_back(row);
    }
    
    for (long n = 0; n < N; ++n) {
        long R, C;
        cin >> R >> C;
        bin[R][C] = 1;
    }
    
    vector<long> empty;

    for (long w = 0; w < W; ++w) {
        fill(bin, H, W, 0, w, 0, -1, false, empty);
        fill(bin, H, W, H-1, w, 0, -1, false, empty);
    }

    for (long h = 0; h < H; ++h) {
        fill(bin, H, W, h, 0, 0, -1, false, empty);
        fill(bin, H, W, h, W-1, 0, -1, false, empty);
    }

    for (long h = 0; h < H; ++h) {
        for (long w = 0; w < W; ++w) {
            if (bin[h][w] == 0) {
                vector<long> coppia;
                fill(bin, H, W, h, w, 0, -1, true, coppia);
                long sostituisci = bin[coppia[0]][coppia[1]];
                fill(bin, H, W, coppia[0], coppia[1], sostituisci, sostituisci+1, false, empty);
                coppia.clear();
            }
        }
    }

    vector<long> sizes;
    for (long h = 0; h < H; ++h) {
        for (long w = 0; w < W; ++w) {
            if (bin[h][w] != -1) {
                sizes.push_back(bin[h][w]-1);
                fill(bin, H, W, h, w, bin[h][w], -1, false, empty);
            }
        }
    }

    sort(sizes.begin(), sizes.end());

    for (long i : sizes)
        cout << i << ' ';

    return 0;
}

