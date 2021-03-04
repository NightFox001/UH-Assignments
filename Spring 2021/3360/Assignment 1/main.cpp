#include <iostream>
#include <fstream>
#include <string>
#include <list> 
#include <vector> 
using namespace std;


class Job {
    public:
        int SeqNum;
        int jobId;
        string state = "ready";
        list<string> jobRequests;
        list<int> jobDurations;
        void setId(int Id) {SeqNum = Id;}
        // void setRequest(string req) {request = req;}
        
        void printRequests() {
            list<string>::iterator iter = this->jobRequests.begin();
            while(iter != this->jobRequests.end())
            {
                cout << "Request " << *iter << endl;
                ++iter;
            }
        }

        // return and remove next job request
        string popRequest() {
            list<string>::iterator iter = this->jobRequests.begin();
            string request = *iter;
            this->jobRequests.pop_front();
            return request;
        }
        // return and remove next job duration
        int popDuration() {
            list<int>::iterator iter = this->jobDurations.begin();
            int time = *iter;
            this->jobDurations.pop_front();
            return time;
        }
};

struct Event {
        // event list holds time that it will complete at. start time + time needed
        int completionTime, jobId;
        string requestName; // core, disk, spooler
};

struct Device {
    string status = "FREE";
    int busyCount = 0;
};

void coreRequest(int duration, int jobID, Device core, int& currTime){
    if (core.status == "FREE") {
        core.status = "BUSY";
        // schedule CORE completion at currentTime + requestedTime for job jobID;
        // aka create event
    }
    else {
    // queue jobID in readyQueue

    }
} 

void fetchJobs(vector<Job*> inputTable, int& jobsProccessing, int& MPL, int& nextJob, int&jobsInTable) {
    while ((jobsProccessing < MPL)&&(nextJob < jobsInTable)) {

        jobsProccessing++;
        int seqno = nextJob;
        nextJob++;
        // pop first job step from job seqno
        string request = inputTable[seqno]->popRequest();
        int duration = inputTable[seqno]->popDuration();

        if (request == "CORE") {
            // process core request for job jobID[seqno]
            // tell processor that this job needs the core and for how long
            // if processor is busy, get in line to tell it your request
            printf("DONT PANIC: FIRST STEP IS A CORE REQUEST\n");
        }
        else
            printf("PANIC: FIRST STEP IS NOT A CORE REQUEST");
    }
}

void terminateJob() {
    // jobsProccessing -- ;
}

fstream getFile(int argc, char *argv[]) {

    string fileName;
    fstream file;

    if (argc > 1) {
        fileName = argv[2];
            cout << "\n\n\nAttempting to open file '" << fileName << "'\n\n";
            file.open(fileName);
            if (file.is_open()) {
                cout << "File '" << fileName << "' opened from arg! (Good job!)\n\n\n";
                return file;
            } else {
                cout << "Could not open file '" << fileName << "' from arg\n\n\n";
            }   
    } else { cout << "No file name provided in arg \n(Hint: you can include file name as the third argument like > ./main filler input10.txt  )\n\n\n"; }

    while (true) { 
        cout << "Please enter file name (Enter \"q\" to exit):\n";
        cin >> fileName;
        file.open(fileName);
        if ((file.is_open()) || (fileName == "q")) { // program exits with "q"
            return file;
        }
        else {
        cout << "\n\n\n\tCould not open file '" << fileName << "'\n\tPlease try another file name or check if the file is in the correct directory.\n\n";
        }
    } // while
    return file; 
}

int main(int argc, char *argv[]) {  
    cout << "\n\n\n\n\n\n\n\n\n";
    fstream file;
    string fileName, keyword, argument, request; 
    int MPL, duration, jobsInTable = 0, nextJob = 0, currentTime = 0, loopCount = 0;
    vector<Job*> inputTable;  
    Job* jobPtr = NULL;
    list<Event> eventList;
    Event* event;
    list<int> readyQ;
    list<int> diskQ;
    list<int> spoolQ;
    Device core;
    Device disk;
    Device spooler;


    // file = getFile(argc, argv);
    file.open("input10.txt");
    if (!file.is_open()) { // user chose to exit before entering valid file request
        cout << "\n\n\nExiting... Goodbye!\n\n";
        return 0;
    } 
    // 
    else { 
        cout << "\nFile opened. Beginning to read from file.\n\n";
        // first line contains MPL
        file >> request >> MPL;
        // Get all inputTable from file
        while (file >> request >> duration) {
            // Create a new Job object
            if (request == "JOB") {
                jobPtr = new Job;
                jobPtr->jobId = duration;
                jobPtr->SeqNum = jobsInTable;
                inputTable.push_back(jobPtr);
                jobsInTable++;
                    continue;
            // Add requests for the last Job created
            } 
            else { 
                jobPtr->jobRequests.push_back(request);
                jobPtr->jobDurations.push_back(duration);
            }

        } // while
        // MPL = 2;
        cout << "Done reading file.\nMPL: " << MPL << "\n \n";


        int jobsProccessing = 0;
        // if (jobsProccessing < MPL) and jobs there are still jobs ready to be fetched
        // fetchJobs()


            // starting a job will always be a core request
            // Event event;
            // event.completionTime = (*itr)->popDuration();
            // event.requestName = (*itr)->popRequest();
            // event.jobId = (*itr)->jobId;
         
            // eventList.push_back(event);
            // Event tempEvent;
            // while (eventList.size() > 0) {
            //     eventList.pop_front();
            //     // remove event with smallest completion time



    } // after reading. end of program
  
    for (int i = 0; i < jobsInTable; ++i){
        cout << "deleting 'job " << inputTable[i]->jobId << "' at index " << i << endl;
        delete inputTable[i];
    }

    // print simulation results
   
// inputTable have id and resouce
// resouce has request of CORE,DISK,and PRINT




    if (file.is_open()) { file.close(); }
    return 0;
}