// class Computer {
//     public:
//         int MPL;
//         int time = 0;
//         Job *jobs;
//         int jobCount = 0; 
//         int diskAccessCount = 0;

//         // core  - what is the core working on
//         // core ready queu  - is something 'ready' waiting for core
//         // disk
//         // disk que
//         // spool
//         // spool que

//         void SetTime(int newTime) {time = newTime;}
//         void addTime(int moreTime) {time += moreTime;}
//         void SetMPL(int _mpl) {
//             MPL = _mpl;
//             jobs = new Job[MPL];
//         } 
//         void addJob(int id, string req) {
//             if (jobCount < MPL) {
//                 jobs[jobCount].setId(id);
//                 jobs[jobCount].setRequest(req);
//                 jobCount++;
//                 cout << "Job with id " << id << " added.\n";
//             }
//             else {cout << "Can't add job '"<< id << "'. MPL limit reached\n";}
//         }
//         void Print();
// };
#include <iostream>
#include <fstream>
#include <string>
#include <list> 
using namespace std;



void changeArr(int *arr, int size) {       
    double avg;          

    for (int i = 0; i < size; ++i) {
        arr[i] = i;
    }

}


void middleMan(int *arr, int size) {
    changeArr(arr, size);
}


int main() {


    // list<int> requestTimes;
    const int size = 5;
    int nums [size] = { 10, 20, 30, 40, 50 };

    // changeArr(nums, size);
    middleMan(nums, size);

    for (int i = 0; i < size; ++i) {
        cout << nums[i] << endl;
    }

    


    string name, num;



    return 0;
}