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

int main() {


    // list<int> requestTimes;
    // const int size = 5;
    // int nums [size] = { 10, 20, 30, 40, 50 };

    // for (int i = 0; i < size; i++) {
    //     requestTimes.push_back(nums[i]);
    // }
    
    // list<int>::iterator itr;
    // for(itr = requestTimes.begin(); itr != requestTimes.end(); ++itr)
    //     std::cout << *itr << " ";

    // int newNum = 25;
    // for(itr = requestTimes.begin(); itr != requestTimes.end(); ++itr)
    //     if ( *itr > newNum) {
    //         requestTimes.insert(itr, newNum);
    //         break;
    //     }

    // for(itr = requestTimes.begin(); itr != requestTimes.end(); ++itr)
    //     std::cout << *itr << " ";

    string name, num;
    while (cin >> name >> num) {
        cout << name << " " << num << endl;
    }




    return 0;
}