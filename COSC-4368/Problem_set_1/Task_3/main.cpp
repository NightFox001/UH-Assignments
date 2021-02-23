#include <iostream>
using namespace std;

int RecursiveDFS(int currentV) {
    if ( currentV is not in visitedSet ) {
        Add currentV to visitedSet
        "Visit" currentV
        for each vertex adjV adjacent to currentV
            RecursiveDFS(adjV)
    }
}

int main() {
    
    return 0;
}