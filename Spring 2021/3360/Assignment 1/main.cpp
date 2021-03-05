#include <iostream>
#include <fstream>
#include <string>
#include <list> 
#include <vector> 
#include <queue> 

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

        string getRequest() {
            list<string>::iterator iter = this->jobRequests.begin();
            string request = *iter;
            return request;
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
    int completionTime;
    string requestName; // core, disk, spooler
    int jobId;
    Event(int completionTime, string requestName, int jobId) {
        this->completionTime = completionTime;
        this->requestName = requestName;
        this->jobId = jobId;
    }
};


struct EventList {
    list<Event*> eventList;

    // add events in order, first time is first in list
    void add(Event* event) {
        if (eventList.size() < 1) {
            eventList.push_front(event);
            return;
        }
        list<Event*>::iterator itr;
        for (itr = eventList.begin(); itr != eventList.end(); ++itr) {
            if ((*itr)->completionTime < event->completionTime) {
                eventList.insert(itr, event);
                return;
            }
        }
    }

    // Event* getEvent() {

    // }
};


struct Device {
    string status = "FREE";
    int busyCount = 0;
};


//slide 25
void printJobStart(int jobId, int currentTime, vector<int> jobTable, vector<Job*> inputTable) {
    cout << "Job " << jobId << " starts at time " << currentTime << " ms\n";
    cout << "Job Table:\n";
    //check if there is a job in the table
    if (jobTable.size() == 0) {
        cout << "There are no other active jobs\n";
    }
    else {
        for (auto itr = jobTable.begin(); itr != jobTable.end(); itr++) {
            cout << "Job " << inputTable[jobTable[*itr]]->jobId << " is " << inputTable[jobTable[*itr]]->state << endl;
        }
    }
    cout << "\n\n";
}


void coreRequest(Job *job, Device& core, int& currentTime, EventList &eventList, queue<Job*> *readyQ){
    cout << "1 core is: " << core.status << endl;
    if (core.status == "FREE") {
        core.status = "BUSY";
        // schedule CORE completion at currentTime + requestedTime for job jobID;
        // aka create event
        int duration = job->popDuration();
        int jobId = job->jobId;
        int completionTime = currentTime + duration;
        Event* event = new Event(completionTime, "CORE", jobId);
        eventList.add(event);
    }
    else {
    // queue jobID in readyQueue
        readyQ->push(job);
    }
    cout << "2 core is: " << core.status << endl;
} 

// void core_release (jobID) { 
//     if (readyQueue is not empty) {
//         // pop first core request in readyQueue
//         // schedule its completion at current_time + how_long
//     } else {
//         // core = FREE 
//     }
//     // process next job request for job jobID
// }

void fetchJobs(vector<Job*> inputTable, int &jobsProccessing, int &MPL, int &nextJob, int &jobsInTable, Device &core, int &currentTime, vector<int> jobTable, EventList &eventList, queue<Job*> *readyQ) {

    while ((jobsProccessing < MPL)&&(nextJob < jobsInTable)) {

        jobsProccessing++;
        int seqno = nextJob;
        nextJob++;
        // pop first job step from job seqno
        
        string request = inputTable[seqno]->getRequest();
        if (request == "CORE") {
            // process core request for job jobID[seqno]
            // tell processor that this job needs the core and for how long
            // if processor is busy, get in line to tell it your request
            printJobStart(inputTable[seqno]->jobId, currentTime, jobTable, inputTable);
            coreRequest(inputTable[seqno], core, currentTime, eventList, readyQ);
            jobTable.push_back(seqno);
        }
        else
            printf("PANIC: FIRST STEP IS NOT A CORE REQUEST");
    }
}

// FIXME pls
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
    EventList eventList;
    Event* event;
    queue<Job*> readyQ, diskQ, spoolQ;
    Device core, disk, spooler;
    // dynamic array of jobs loaded in RAM, num of elements = nextJob
    vector<int> jobTable;

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
        // MPL = 2;
        // cout << "before fetch core is: " << core.status << endl;
        cout << "\nbefore fetch first job req: " << inputTable[0]->getRequest() << "\n\n";
        fetchJobs(inputTable, jobsProccessing, MPL, nextJob, jobsInTable, core, currentTime, jobTable, eventList, &readyQ);

        // cout << "after fetch core is: " << core.status << endl;
        cout << "\nafter fetch first job req: " << inputTable[0]->getRequest() << "\n\n";


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
        // cout << "deleting 'job " << inputTable[i]->jobId << "' at index " << i << endl;
        delete inputTable[i];
    }

    // print simulation results
   
// inputTable have id and resouce
// resouce has request of CORE,DISK,and PRINT




    if (file.is_open()) { file.close(); }
    return 0;
}