//Problem        : Expecto Palindronum
//Language       : C++
//Compiled Using : g++
//Version        : GCC 4.9.1
//Input for your program will be provided from STDIN
//Print out all output from your program to STDOUT

#include <iostream>
#include <string>
#include <algorithm>
#include <climits> 

using namespace std;

bool is_palindrome(string word) {
    int i = 0;
    int j = word.size()-1;
    while (i < j) {
        if (word[i] != word[j]) {
            return false;
        }
        ++i;
        --j;
    }
    return true;
}

int main() {
    string word;
    cin >> word;
    int length = word.size();
    if (length == 1) {
        cout << 1 << endl;
        exit(0);
    }
    int max_pal = 1;
    for (int i = 1; i < length-1; ++i) {
        int j = i-1;
        int k = i+1;
        int current = 1;
        while (j >= 0 && k < length && word[j] == word[k]) {
            current += 2;
            --j;
            ++k;
        }
        if (current > max_pal && j == -1) {
            max_pal = current;
        }
    }
    cout << length + (length - max_pal) << endl;
    return 0;
}
