#include <iostream>
#include <ctime>
#include <ratio>
#include <chrono>

using namespace std::chrono;

int main() {
    const int n = 16;
    const int m = 1677721600;
    // const int m = 13421772800;
    srand(time(0));

    int M[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++){
            M[i][j] = 0;
        }
    }

    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    
    for (int input = 0; input < m; input++) { 
        int i = rand() % n + 1; //  1 ≤ i ≤ n
        int j = rand() % n + 1; //  1 ≤ j ≤ n
        int x = rand() % 1000;

        M[i][j] = M[i][j] + x;

    }

    high_resolution_clock::time_point t2 = high_resolution_clock::now();

    duration<double> time_span = duration_cast<duration<double>>(t2 - t1);

    std::cout << "It took " << time_span.count() << " seconds.";
    std::cout << std::endl;


    return 0;
}
