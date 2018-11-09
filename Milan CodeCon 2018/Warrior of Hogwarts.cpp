//Problem        : Warrior Of Hogwarts
//Language       : C++14
//Compiled Using : g++
//Version        : GCC 4.9.1
//Input for your program will be provided from STDIN
//Print out all output from your program to STDOUT

#include <iostream>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

unsigned long ans = 10'000'000'000;

void divide(unsigned long N, unsigned long level = 0) {
    if (level > ans) return;
    
    if (N == 1) {
        ans = level;
        return;
    }
    
    if (N % 3 == 0) {
        divide(N/3, level+1);
    }
    
    if (N % 2 == 0) {
        divide(N/2, level+1);
    }
    
    divide(N-1, level+1);
}

int main() {
    unsigned long N;
    cin >> N;
    divide(N);
    cout << ans << endl;
    return 0;
}