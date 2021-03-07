#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <queue>

using namespace std;

class Job
{
public:
    int SeqNum;
    int jobId;
    string state = "ready";
    list<string> jobRequests;
    list<int> jobDurations;
    void setId(int Id) { SeqNum = Id; }
    // void setRequest(string req) {request = req;}

    void printRequests()
    {
        list<string>::iterator iter = this->jobRequests.begin();
        while (iter != this->jobRequests.end())
        {
            cout << "Request " << *iter << endl;
            ++iter;
        }
    }

    string getRequest()
    {
        list<string>::iterator iter = this->jobRequests.begin();
        string request = *iter;
        return request;
    }

    // return and remove next job request
    string popRequest()
    {
        list<string>::iterator iter = this->jobRequests.begin();
        string request = *iter;
        this->jobRequests.pop_front();
        return request;
    }

    int getDuration()
    {
        list<int>::iterator iter = this->jobDurations.begin();
        int duration = *iter;
        return duration;
    }

    // return and remove next job duration
    int popDuration()
    {
        list<int>::iterator iter = this->jobDurations.begin();
        int time = *iter;
        this->jobDurations.pop_front();
        return time;
    }

    bool isDone()
    {
        return ((jobRequests.size() < 1) || (jobDurations.size() < 1));
    }
};

struct Event
{
    // event list holds time that it will complete at. start time + time needed
    int completionTime;
    int duration;
    string requestName; // core, disk, spooler
    // int jobId;
    Job *job;

    Event(int duration, int completionTime, string requestName, Job *job)
    {
        this->completionTime = completionTime;
        this->duration = duration;
        this->requestName = requestName;
        this->job = job;
    }
};

struct EventList
{
    list<Event *> eventList;

    // add events in order, first time is first in list
    void add(Event *event)
    {
        //        cout << "-- Job " << event->job->jobId << " requests " << event->requestName << " access for " << event->duration << ". with comp time: " << event->completionTime << endl;
        bool eventAdded = false;
        if (eventList.size() < 1)
        {
            eventList.push_front(event);
            //            cout << "event " << event->requestName << " insterted 1\n\n";
            eventAdded = true;
        }
        else
        {
            list<Event *>::iterator itr;
            for (itr = eventList.begin(); itr != eventList.end(); ++itr)
            {
                if (event->completionTime < (*itr)->completionTime)
                {
                    eventList.insert(itr, event);
                    //                    cout << "event " << event->requestName << " insterted 2\n\n";
                    eventAdded = true;
                    break;
                }
            }
            if (eventAdded == false)
            {
                eventList.push_back(event);
            }
        }
        //                this->printEvents();
    }

    bool isNotEmpty()
    {
        return (eventList.size() > 0);
    }

    Event *getAndPopEvent()
    {
        Event *event = eventList.front();
        eventList.pop_front();
        return event;
    }
    void printEvents()
    {
        cout << "\nEvent list:\n";
        list<Event *>::iterator itr;
        for (itr = eventList.begin(); itr != eventList.end(); ++itr)
        {
            cout << "Job: " << (*itr)->job->jobId << ", request: " << (*itr)->requestName << ", comp time: " << (*itr)->completionTime << endl;
        }
        cout << "end of list\n\n";
    }
};

struct Device
{
    string status = "FREE";
    int busyCount = 0;
};

//slide 25
void printJobUpdate(string update, int jobId, int currentTime, vector<int> jobTable, vector<Job *> inputTable)
{
    cout << "\nJob " << jobId << " " << update << " at time " << currentTime << " ms\n";
    cout << "Job Table:\n";
    //check if there is a job in the table
    if (jobTable.size() == 0)
    {
        cout << "There are no other active jobs\n";
    }
    else
    {
        for (auto itr = jobTable.begin(); itr != jobTable.end(); itr++)
        {
            cout << "Job " << inputTable[jobTable[*itr]]->jobId << " is " << inputTable[jobTable[*itr]]->state << endl;
        }
    }
    cout << "\n\n";
}

void coreRequest(Job *job, Device &core, int &currentTime, EventList &eventList, queue<Job *> *readyQ)
{
    cout << "-- Job " << job->jobId << " requests a " << job->getRequest() << " at time " << currentTime << " for " << job->getDuration() << " ms.\n";
    if (core.status == "FREE")
    {
        core.status = "BUSY";
        job->state = "RUNNING";
        // schedule CORE completion at currentTime + requestedTime for job jobID;
        // aka create event
        Event *event = new Event(job->getDuration(), currentTime + job->popDuration(), job->popRequest(), job);
        eventList.add(event);
    }
    else
    {
        // queue jobID in readyQueue
        job->state = "READY";
        cout << "-- Job " << job->jobId << " must wait for a core.\n";
        readyQ->push(job);
        cout << "-- Ready queue now contains " << readyQ->size() << " job(s) waiting for a core.\n";
    }
    // cout << "2 core is: " << core.status << endl;
}

void fetchJobs(vector<Job *> inputTable, int &jobsProccessing, int &MPL, int &nextJob, int &jobsInTable, Device &core, int &currentTime, vector<int> &jobTable, EventList &eventList, queue<Job *> *readyQ)
{

    while ((jobsProccessing < MPL) && (nextJob < jobsInTable))
    {
        jobsProccessing++;
        int seqno = nextJob;
        nextJob++;
        string request = inputTable[seqno]->getRequest();
        if (request == "CORE")
        {
            // process core request for job jobID[seqno]
            // tell processor that this job needs the core and for how long
            // if processor is busy, get in line to tell it your request
            printJobUpdate("starts", inputTable[seqno]->jobId, currentTime, jobTable, inputTable);
            coreRequest(inputTable[seqno], core, currentTime, eventList, readyQ);
            jobTable.push_back(seqno);
        }
        else
            printf("PANIC: FIRST STEP IS NOT A CORE REQUEST");
    }
}

//called from core release
//inputTable, jobTable, job, core, disk, spooler, currentTime, eventList, &readyQ, &diskQ, &spoolerQ
void terminateJob(vector<Job *> inputTable, vector<int> &jobTable, int &jobsProccessing, int &MPL, int &nextJob, int &jobsInTable, Job *job, Device &core, int &currentTime, EventList &eventList, queue<Job *> *readyQ)
{
    job->state = "TERMINATED";
    //    cout << "\nseq: " << job->SeqNum << " size: " << jobTable.size() << endl;
    printJobUpdate("terminates", job->jobId, currentTime, jobTable, inputTable);
    jobsProccessing--;
    //    jobTable.erase(jobTable.begin()+job->SeqNum);
    //    inputTable.erase(inputTable.begin()+job->SeqNum);
    fetchJobs(inputTable, jobsProccessing, MPL, nextJob, jobsInTable, core, currentTime, jobTable, eventList, readyQ);
}

// disk request
void diskRequest(Job *job, Device &core, Device &disk, Device &spooler, int &currentTime, EventList &eventList, queue<Job *> *readyQ, queue<Job *> *diskQ)
{
    //    cout << "Job " << job->jobId << " requesting " << job->getRequest() << " for " << job->getDuration() << "ms : Time " << currentTime << endl;
    job->state = "BLOCKED: at Disk";
    if (job->getDuration() == 0)
    {
        job->popDuration();
        job->popRequest();
        if (job->getRequest() == "CORE")
        {
            coreRequest(job, core, currentTime, eventList, readyQ);
        }
        else
        {
            cout << "\nCORE wasn't requested after DISK\n\n";
        }
    }
    else if (disk.status == "FREE")
    {
        disk.status = "BUSY";
        Event *event = new Event(job->getDuration(), currentTime + job->popDuration(), job->popRequest(), job);
        eventList.add(event);
    }
    else
    {
        cout << "Job " << job->jobId << " added to disk queue\n";
        diskQ->push(job);
    }
}

void spoolerRequest(Job *job, Device &core, Device &disk, Device &spooler, int &currentTime, EventList &eventList, queue<Job *> *readyQ, queue<Job *> *spoolerQ)
{
    //    cout << "Job " << job->jobId << " requesting " << job->getRequest() << " for " << job->getDuration() << "ms : Time " << currentTime << endl;
    job->state = "BLOCKED: at Spooler";
    if (job->getDuration() == 0)
    {
        // perform next job request #should always be for core
        job->popDuration();
        job->popRequest();
        if (job->getRequest() == "CORE")
        {
            coreRequest(job, core, currentTime, eventList, readyQ);
        }
        else
        {
            cout << "\nCORE wasn't requested after PRINT\n\n";
        }
    }
    else if (spooler.status == "FREE")
    {
        spooler.status = "BUSY";
        Event *event = new Event(job->getDuration(), currentTime + job->popDuration(), job->popRequest(), job);
        eventList.add(event);
    }
    else
    {
        cout << "Job " << job->jobId << " added to spooler queue\n";
        spoolerQ->push(job);
    }
}

void proccessNextRequest(Job *job, Device &core, Device &disk, Device &spooler, int &currentTime, EventList &eventList, queue<Job *> *readyQ, queue<Job *> *diskQ, queue<Job *> *spoolerQ)
{
    if (job->getRequest() == "CORE")
    {
        coreRequest(job, core, currentTime, eventList, readyQ);
    }
    else if (job->getRequest() == "DISK")
    {
        diskRequest(job, core, disk, spooler, currentTime, eventList, readyQ, diskQ);
    }
    else if (job->getRequest() == "PRINT")
    {
        spoolerRequest(job, core, disk, spooler, currentTime, eventList, readyQ, spoolerQ);
    }
    else
    {
        cout << "\n\nSomething went wrong! could not get next request for job at coreRelease. Job request: " << job->getRequest() << "\n\n";
    }
}

void coreRelease(vector<Job *> inputTable, vector<int> &jobTable, int &jobsProccessing, int &MPL, int &nextJob, int &jobsInTable, Job *job, Device &core, Device &disk, int &diskCount, Device &spooler, int &currentTime, EventList &eventList, queue<Job *> *readyQ, queue<Job *> *diskQ, queue<Job *> *spoolerQ)
{
    //    cout << "Job " << job->jobId << " releasing core\n";
    if (readyQ->size() == 0)
    {
        core.status = "FREE";
    }
    else
    {
        // pop first core request in readyQueue
        Job *nextJob = readyQ->front();
        readyQ->pop();
        //        cout << "Job " << nextJob->jobId << " removed from ready queue\n";
        // schedule its completion at current_time + how_long
        Event *event = new Event(job->getDuration(), currentTime + nextJob->popDuration(), nextJob->popRequest(), nextJob);
        eventList.add(event);
    }
    if (job->isDone())
    {
        terminateJob(inputTable, jobTable, jobsProccessing, MPL, nextJob, jobsInTable, job, core, currentTime, eventList, readyQ);
        return;
    }
    else
    {
        // process next job request for job jobID
        if (job->getRequest() == "DISK")
        {
            diskCount++;
        }
        proccessNextRequest(job, core, disk, spooler, currentTime, eventList, readyQ, diskQ, spoolerQ);
    }
}

void diskRelease(Job *job, Device &core, Device &disk, Device &spooler, int &currentTime, EventList &eventList, queue<Job *> *readyQ, queue<Job *> *diskQ, queue<Job *> *spoolerQ)
{
    //    cout << "Job " << job->jobId << " releasing disk\n";
    if (diskQ->size() == 0)
    {
        disk.status = "FREE";
    }
    else
    {
        // pop first disk request in diskQueue
        Job *nextJob = diskQ->front();
        diskQ->pop();
        //        cout << "Job " << nextJob->jobId << " removed from disk queue\n";
        Event *event = new Event(job->getDuration(), currentTime + nextJob->popDuration(), nextJob->popRequest(), nextJob);
        eventList.add(event);
    }
    // process next job request for job jobID
    proccessNextRequest(job, core, disk, spooler, currentTime, eventList, readyQ, diskQ, spoolerQ);
}

void spoolerRelease(Job *job, Device &core, Device &disk, Device &spooler, int &currentTime, EventList &eventList, queue<Job *> *readyQ, queue<Job *> *diskQ, queue<Job *> *spoolerQ)
{
    //    cout << "Job " << job->jobId << " releasing spooler\n";
    if (spoolerQ->size() == 0)
    {
        spooler.status = "FREE";
    }
    else
    {
        // pop first spooler request in diskQueue
        Job *nextJob = spoolerQ->front();
        spoolerQ->pop();
        //        cout << "Job " << nextJob->jobId << " removed from spooler queue\n";
        Event *event = new Event(job->getDuration(), currentTime + nextJob->popDuration(), nextJob->popRequest(), nextJob);
        eventList.add(event);
    }
    // process next job request for job jobID
    proccessNextRequest(job, core, disk, spooler, currentTime, eventList, readyQ, diskQ, spoolerQ);
}

//fstream getFile(int argc, char *argv[])
//{
//
//    string fileName;
//    fstream file;
//
//    if (argc > 1)
//    {
//        fileName = argv[2];
//        cout << "\n\n\nAttempting to open file '" << fileName << "'\n\n";
//        file.open(fileName);
//        if (file.is_open())
//        {
//            cout << "File '" << fileName << "' opened from arg! (Good job!)\n\n\n";
//            return file;
//        }
//        else
//        {
//            cout << "Could not open file '" << fileName << "' from arg\n\n\n";
//        }
//    }
//    else
//    {
//        cout << "No file name provided in arg \n(Hint: you can include file name as the third argument like > ./main filler input10.txt  )\n\n\n";
//    }
//
//    while (true)
//    {
//        cout << "Please enter file name (Enter \"q\" to exit):\n";
//        cin >> fileName;
//        file.open(fileName);
//        if ((file.is_open()) || (fileName == "q"))
//        { // program exits with "q"
//            return file;
//        }
//        else
//        {
//            cout << "\n\n\n\tCould not open file '" << fileName << "'\n\tPlease try another file name or check if the file is in the correct directory.\n\n";
//        }
//    } // while
//    return file;
//}

int main(int argc, char *argv[])
{
    cout << "\n\n\n\n\n\n\n\n\n";
    fstream file;
    string fileName, keyword, argument, request;
    int MPL = 0, duration = 0, jobsInTable = 0, nextJob = 0, currentTime = 0, jobsProccessing = 0;
    vector<Job *> inputTable;
    Job *job = NULL;
    EventList eventList;
    Event *event;
    queue<Job *> readyQ, diskQ, spoolerQ;
    Device core, disk, spooler;
    // dynamic array of jobs loaded in RAM, num of elements = nextJob
    vector<int> jobTable;

    // file = getFile(argc, argv);
    // file.open("input10.txt");
    // if (!file.is_open()) { // user chose to exit before entering valid file request
    //     cout << "\n\n\nExiting... Goodbye!\n\n";
    //     return 0;
    // }
    //
    // cout << "\nFile opened. Beginning to read from file.\n\n";
    // first line contains MPL
    // file >> request >> MPL;
    // cin >> request >> MPL;

    // while (file >> request >> duration) {
    while (cin >> request >> duration)
    {
        // Create a new Job object
        if (request == "MPL")
        {
            MPL = duration;
        }
        else if (request == "JOB")
        {
            job = new Job;
            job->jobId = duration;
            job->SeqNum = jobsInTable;
            inputTable.push_back(job);
            jobsInTable++;
            continue;
            // Add requests for the last Job created
        }
        else if (jobsInTable > 0)
        {
            job->jobRequests.push_back(request);
            job->jobDurations.push_back(duration);
        }
    } // while

    cout << "Done reading file.\nMPL: " << MPL << "\n \n";

    // MPL = 2;
    fetchJobs(inputTable, jobsProccessing, MPL, nextJob, jobsInTable, core, currentTime, jobTable, eventList, &readyQ);

    //// Main ////
    int diskCount = 0;
    int cpuTime = 0;

    while (eventList.isNotEmpty())
    {
        //        eventList.printEvents();
        // pop event and do can correct request
        event = eventList.getAndPopEvent();
        currentTime = event->completionTime;
        job = event->job;

        //        cout << "\nevent popped: Job" << event->job->jobId << ", " << event->requestName << ", completion: " << currentTime << "\n";
        //    SUMMARY:
        //    Total elapsed time: 9208 ms
        //    Number of jobs that completed: 4
        //    Total number of disk accesses: 62
        //    CPU utilization: 0.787

        if (event->requestName == "CORE")
        {
            cpuTime += event->duration;
            coreRelease(inputTable, jobTable, jobsProccessing, MPL, nextJob, jobsInTable, job, core, disk, diskCount, spooler, currentTime, eventList, &readyQ, &diskQ, &spoolerQ);
        }
        else if (event->requestName == "DISK")
        {
            diskRelease(job, core, disk, spooler, currentTime, eventList, &readyQ, &diskQ, &spoolerQ);
        }
        else if (event->requestName == "PRINT")
        {
            spoolerRelease(job, core, disk, spooler, currentTime, eventList, &readyQ, &diskQ, &spoolerQ);
        }
    }

    // cout << "after fetch core is: " << core.status << endl;
    // cout << "\nafter fetch first job req: " << inputTable[0]->getRequest() << "\n\n";

    for (int i = 0; i < jobsInTable; ++i)
    {
        cout << "deleting 'job " << inputTable[i]->jobId << "' at index " << i << endl;
        delete inputTable[i];
    }

    // print simulation results
    double util = (float)cpuTime / (float)currentTime;
    cout << "\n\nSUMMARY:\nTotal elapsed time: " << currentTime << " ms.\n";
    cout << "Number of jobs that completed: " << jobsInTable << "\n";
    cout << "Total number of disk accesses: " << diskCount << "\n";
    cout << "CPU utlization: " << util << "\n";

    if (file.is_open())
    {
        file.close();
    }
    return 0;
}
