/* 
Jonathan Hirsch
COSC 3360
This assignment uses quite a bit of pointers. Each 'job' is a pointer a Job class object that has a couple lists for that jobs requests and durations. Once an event has been made for this request, it is popped from the list for this job. 
An Event is described more below, but once an event is created from a jobs request, a pointer to that event is added to an EventList. The main loop will then pop the pointer to the event with the nearest completion time and then make the appropriate requests for that event, passing a pointer for that job as well.
*/

#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <queue>

using namespace std;


// Each Job has an ID, seequence number, state (used when printing the state of each job), a list of request names in order received, and list of durations for those requests in order received.
class Job
{
public:
    int SeqNum;
    int jobId;
    string state = "ready";
    list<string> jobRequests;
    list<int> jobDurations;

    // used while developing to make sure all requests were received correctly
    void printRequests()
    {
        list<string>::iterator iter = this->jobRequests.begin();
        while (iter != this->jobRequests.end())
        {
            cout << "Request " << *iter << endl;
            ++iter;
        }
    }

    // return the value of the next request without poping
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

// individual Event as recommended in the slides, but also has a pointer to the job that this event is for 
struct Event
{
    // event list holds time that it will complete at. start time + time needed
    int completionTime;
    int duration;
    string requestName; // core, disk, spooler
    // int jobId;
    Job *job;

    // constructor
    Event(int duration, int completionTime, string requestName, Job *job)
    {
        this->completionTime = completionTime;
        this->duration = duration;
        this->requestName = requestName;
        this->job = job;
    }
};

// Just a list of Event structs above
struct EventList
{
    list<Event *> eventList;

    // add events in order by completion time. 
    void add(Event *event)
    {
        //        cout << "-- Job " << event->job->jobId << " requests " << event->requestName << " access for " << event->duration << ". with comp time: " << event->completionTime << endl;
        bool eventAdded = false;
        if (eventList.size() < 1)
        {
            eventList.push_front(event);
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
                    eventAdded = true;
                    break;
                }
            }
            if (eventAdded == false)
            {
                eventList.push_back(event);
            }
        }
    }

    // returns true if the list is not empty
    bool isNotEmpty()
    {
        return (eventList.size() > 0);
    }

    // return the next event to be proccessed and pop from list
    Event *getAndPopEvent()
    {
        Event *event = eventList.front();
        eventList.pop_front();
        return event;
    }

    // for testing
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

// used to create a CORE, DISK, and SPOOLER device to keep track of that devices status 
struct Device
{
    string status = "FREE";
    int busyCount = 0;
};

// called when a job starts or terminates to print all jobs and their status
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

// Create a new event or add job to queue
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

// start a core request for each job that needs to be loaded into memory. Called before main loop and after job termination
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

//called only from core release when there are no more requests for that job. call fetchJobs
void terminateJob(vector<Job *> inputTable, vector<int> &jobTable, int &jobsProccessing, int &MPL, int &nextJob, int &jobsInTable, Job *job, Device &core, int &currentTime, EventList &eventList, queue<Job *> *readyQ)
{
    job->state = "TERMINATED";
    printJobUpdate("terminates", job->jobId, currentTime, jobTable, inputTable);
    jobsProccessing--;
    //    jobTable.erase(jobTable.begin()+job->SeqNum);
    //    inputTable.erase(inputTable.begin()+job->SeqNum);
    fetchJobs(inputTable, jobsProccessing, MPL, nextJob, jobsInTable, core, currentTime, jobTable, eventList, readyQ);
}

// Create a new event or add job to queue
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
            cout << "\nERROR: CORE wasn't requested after DISK\n\n";
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

// Create a new event or add job to queue
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
            cout << "\nERROR: CORE wasn't requested after PRINT\n\n";
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

// used by the 3 release methods to determine which request to make next
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

// handles job finishing with a device, starting next request for that job, and loading new job from queue if there is one
void coreRelease(vector<Job *> inputTable, vector<int> &jobTable, int &jobsProccessing, int &MPL, int &nextJob, int &jobsInTable, Job *job, Device &core, Device &disk, int &diskCount, Device &spooler, int &currentTime, EventList &eventList, queue<Job *> *readyQ, queue<Job *> *diskQ, queue<Job *> *spoolerQ)
{
    cout << "Job " << job->jobId << " releasing core\n";
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
        Event *event = new Event(nextJob->getDuration(), currentTime + nextJob->popDuration(), nextJob->popRequest(), nextJob);
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

// handles job finishing with a device, starting next request for that job, and loading new job from queue if there is one
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
        Event *event = new Event(nextJob->getDuration(), currentTime + nextJob->popDuration(), nextJob->popRequest(), nextJob);
        eventList.add(event);
    }
    // process next job request for job jobID
    proccessNextRequest(job, core, disk, spooler, currentTime, eventList, readyQ, diskQ, spoolerQ);
}

// handles job finishing with a device, starting next request for that job, and loading new job from queue if there is one
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
        Event *event = new Event(nextJob->getDuration(), currentTime + nextJob->popDuration(), nextJob->popRequest(), nextJob);
        eventList.add(event);
    }
    // process next job request for job jobID
    proccessNextRequest(job, core, disk, spooler, currentTime, eventList, readyQ, diskQ, spoolerQ);
}

// used to get file from input when not running on linux
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
    vector<int> jobTable;

    // for reading from file before I read assignment instruction 2nd time
    // file = getFile(argc, argv);
    // file.open("input10.txt");
    // if (!file.is_open()) { // user chose to exit before entering valid file request
    //     cout << "\n\n\nExiting... Goodbye!\n\n";
    //     return 0;
    // }
    // cout << "\nFile opened. Beginning to read from file.\n\n";

    // while (file >> request >> duration) {
    while (cin >> request >> duration)
    {
        if (request == "MPL")
        {
            MPL = duration;
        }
        // create a new job (pointer to memory for a job) and push to inputTable
        else if (request == "JOB")
        {
            job = new Job;
            job->jobId = duration;
            job->SeqNum = jobsInTable;
            inputTable.push_back(job);
            jobsInTable++;
            continue;
            
        } // Add requests for the last Job created in inputTable
        else if (jobsInTable > 0) // this prevents segmentation faults
        {
            job->jobRequests.push_back(request);
            job->jobDurations.push_back(duration);
        }
    } // while

    cout << "\n\n\nDone reading inputs.\nMPL: " << MPL << "\n\n";

    // load the first mpl jobs into 'memory' aka add the first event for these jobs
    fetchJobs(inputTable, jobsProccessing, MPL, nextJob, jobsInTable, core, currentTime, jobTable, eventList, &readyQ);

    //// Main ////
    int diskCount = 0;
    int cpuTime = 0;

    while (eventList.isNotEmpty())
    {
        // pop event for eventList and make appropriate request
        event = eventList.getAndPopEvent();
        currentTime = event->completionTime;
        job = event->job;

        if (event->requestName == "CORE")
        {
            cpuTime += event->duration; // count total time CPU is in use for later
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

    for (int i = 0; i < jobsInTable; ++i)
    {
        delete inputTable[i]; // no one likes a memory leak
    }

    // print simulation results
    double util = (float)cpuTime / (float)currentTime;
    cout << "\n\nSUMMARY:\nTotal elapsed time: " << currentTime << " ms.\n";
    cout << "Number of jobs that completed: " << jobsInTable << "\n";
    cout << "Total number of disk accesses: " << diskCount << "\n";
    cout << "CPU utlization: " << util << "\n";


    // if (file.is_open())
    // {
    //     file.close();
    // }
    return 0;
}
