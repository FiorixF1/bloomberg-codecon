//Problem        : Mug Color
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

int main() {
    int WHITE = 0;
    int BLACK = 0;
    int BLUE = 0;
    int RED = 0;
    int YELLOW = 0;
    long N;
    cin >> N;
    
    for (int i = 0; i < N; ++i) {
        string entry;
        cin >> entry;
        if (entry == "White") {
            ++WHITE;
        } else if (entry == "Black") {
            ++BLACK;
        } else if (entry == "Blue") {
            ++BLUE;
        } else if (entry == "Red") {
            ++RED;
        } else if (entry == "Yellow") {
            ++YELLOW;
        }
    }
    
    int color_counter[5] = {WHITE, BLACK, BLUE, RED, YELLOW};
    int index = 0;
    for (int i = 1; i < 5; ++i) {
        if (color_counter[i] < color_counter[index]) {
            index = i;
        }
    }
    
    string color[5] = {"White", "Black", "Blue", "Red", "Yellow"};
    cout << color[index] << endl;
    
    return 0;
}

