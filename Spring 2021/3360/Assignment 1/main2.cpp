#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>


using namespace std;

struct job{
    string instruction;
    int key; // instruction == CORE key == 50
    job(string jobinstruction, int timeTaken){
        instruction= jobinstruction;
        key = timeTaken;
    }
};

struct event{
    int key;
    string instruction;
    int index;
    event(int timeTaken, string jobinstruction, int ind) {
        key =timeTaken;
        instruction = jobinstruction;
        index = ind;
    }
    bool operator<(const event &other) const { return key < other.key; }
};


//print job table showing the current job running/blocked status
void printjobtable(int jobcount, int pid[], string jobtable[]) {
    bool isempty = true;

    cout << "Job Table:" <<endl;
    for (int i =0; i< jobcount; i++){
        cout << "Job " << pid[i] << " is"<< jobtable[i];
        isempty = false;}

    if (isempty == false) {
        cout << "There is no active jobs." << endl;
    }

}


void fetchjobstoram(string jobtable[], int pid[], int ind, int numberofjob,int mpl, int nextjob, int jobcount, int clock, vector <queue <job>> process_list) {
    while (numberofjob < mpl && nextjob < jobcount) {
        numberofjob +=1;
        ind = nextjob;
        nextjob +=1;
        cout << "Job " << pid[ind] << " is fetched at time "<< clock <<endl;
        printjobtable(jobcount, pid, jobtable); //print jobtable
        string request = process_list[0].front().instruction;
        int duration = process_list[0].front().key;   
        process_list[0].pop();//pop out the first instruction of the job
    } 
}

// core request
void core_request(int pid, int duration, int ind, bool corefree, int clock, int coretimes, string jobtable[], priority_queue <event> event_list, queue <event> readyQueue) {
    coretimes += duration;// to update and calcuate the core ult later in summary

    if (corefree == true){
        corefree = false;// set to false for the next job to fetch
        jobtable[ind] = "RUNNING";
        event curEvent(clock+duration, "CORE", ind);
        event_list.push(curEvent);
        //sorting event_list
        //using priority_queue so event_list is sorted at the time current Event is pushed to the queue
        //***************
    }
    else { //waiting to get process to the CORE
        jobtable[ind] = "READY";
        event curEvent(clock+duration, "CORE", ind);
        readyQueue.push(curEvent);
    }        
}// end core request

//disk request
void disk_request(int pid[], int duration, int ind, bool diskfree, int clock, int diskcount, string jobtable[],priority_queue <event> event_list, queue <event> diskQueue, int numberofjob,int mpl, int nextjob, int jobcount, vector <queue <job>> process_list) {
    
    if (duration == 0)  {
        fetchjobstoram(jobtable, pid, ind, numberofjob, mpl, nextjob, jobcount, clock, process_list);
    }
    else if (diskfree == true){
        diskfree = false;
        jobtable[ind] = "BLOCKED";
        diskcount += 1;
        event curEvent(clock+duration, "DISK", ind);
        event_list.push(curEvent);
    }
    else{
        jobtable[ind] = "BLOCKED";
        event curEvent(clock+duration, "DISK", ind);
        diskQueue.push(curEvent);
    }

}

//spooler request
void spooler_request(int pid[], int duration, int ind, bool spoolerfree, int clock, int diskcount, string jobtable[],priority_queue <event> event_list, queue <event> spoolerQueue) {
 if (spoolerfree == true){
        spoolerfree = false;
        jobtable[ind] = "BLOCKED";
        event curEvent(clock+duration, "SPOOLER", ind);
        event_list.push(curEvent);
    }
    else{
        jobtable[ind] = "BLOCKED";
        event curEvent(clock+duration, "SPOOLER", ind);
        spoolerQueue.push(curEvent);
    }
}

//core releasee
void core_release() {

}

//disk release
void disk_release(){

}

//spooler release
void spooler_release() {

}



int main() {
    string step;
    int mpl, arg, jobcount, max=0;
    // vector <queue <job>> process_list;
    int ind = 0;
    vector<int> pid;
    int count;
    jobcount=0;
    priority_queue <event> event_list;   
    queue <event> readyQueue;// store waiting core 
    queue <event> diskQueue;
    queue <event> spoolerQueue;
    vector<string> jobtable;
    bool corefree = true;// check if core is free
    bool diskfree = true;// check if disk is free
    bool spoolerfree = true;// check if spooler is free
    int numberofjob =0;
    int clock =0;
    int coretimes = 0;
    int diskcount = 0;



    cin >> step >> arg;
    while (cin >> step >> arg ) {
        cout << step << endl;
        max+=1;
        if (step == "MPL") {
            mpl = arg;
        } 
        else (step == "JOB") {
            cout << "Job found" << endl;            
            jobcount += 1;
            ind = jobcount -1;
            // pid[ind] = arg;           
            // process_list.push_back(queue <job>());//add more job to outter vector
        }
        //inner vector:
        // else {                 
              
        //     job curJob(step, arg); //assign instruction and key to a queue name curJob
        //     process_list[ind].push(curJob); // push the current instruction (CORE/DISk/..) to each queue
            
        // }
        
    
    }

    for (int i = 0; i < jobcount; i++){
        cout << jobtable[i];
    }
    cout << "made it" << endl; 
    //fetching the first job
    // int nextjob = 0;
    // fetchjobstoram(jobtable, pid, ind, numberofjob, mpl, nextjob, jobcount, clock, process_list);
    

    



    return 0;   
}