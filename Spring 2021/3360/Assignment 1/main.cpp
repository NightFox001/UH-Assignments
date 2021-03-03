#include <iostream>
#include <fstream>
#include <string>
#include <list> 
using namespace std;


class Job {
    public:
        int SeqNum;
        int jobNum;
        list<string> requestNames;
        list<int> requestTimes;
        void setId(int Id) {SeqNum = Id;}
        // void setRequest(string req) {request = req;}
        
        void printNames() {
            list<string>::iterator iter = this->requestNames.begin();
            while(iter != this->requestNames.end())
            {
                cout << "Name " << *iter << endl;
                ++iter;
            }
        }
};

class Event {
    public:
        int completionTime, jobId;
        string requestName; // core, disk, spooler


};

void printJobStates(string table){
    // print stuff
}

void printSnapShot(int time, int jobId, string action) {
    // do stuff
    // print table 
}

// event list holds time that it will complete at. start time + time needed


fstream getFile(int argc, char *argv[]) {
    cout << argc << endl;
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

    
    fstream file;


    file = getFile(argc, argv);
    if (!file.is_open()) { // user chose to exit before entering valid file name
        cout << "\n\n\nExiting... Goodbye!\n\n";
        return 0;
    } else { 
        cout << "\nFile opened. Beginning to read from file.\n\n";

        string fileName, keyword, argument, name; 
        int MPL, num, jobsAdded = 0, jobsCompleted = 0, currentTime = 0, loopCount = 0;
        list<Job*> jobs;
        Job* jobPtr = NULL;

        // first line contains MPL
        file >> name >> MPL;

        // Get all jobs from file
        while (file >> name >> num) {
            // cout << name << " " << num << endl;

            // Create a new Job object
            if (name == "JOB") {
                jobPtr = new Job;
                jobPtr->jobNum = num;
                jobPtr->SeqNum = jobsAdded;
                jobs.push_back(jobPtr);
                jobsAdded++;
                    continue;

            // Add requests for the last Job created
            } else { 
                jobPtr->requestNames.push_back(name);
                jobPtr->requestTimes.push_back(num);
            }

        } // while
        cout << "Done reading file.";

        // start first MPL jobs
        while (jobsCompleted < jobsAdded and loopCount < 10000) {
            loopCount++; // avoid infinite loops

            // if jobs in ram < MPL { fetch new jobPtr }
            // starting a job will always be a core request

        }

        cout << "\nloop count: " << loopCount << endl;

        list<Job*>::iterator it2;
        for (it2 = jobs.begin(); it2 != jobs.end(); ++it2){
            delete (*it2);
        }

    } // after reading. end of program
  
    // while (event list is not empty) {
        // process next event in list

    // } 

    // print simulation results
   
// jobs have id and resouce
// resouce has request of CORE,DISK,and PRINT

    // list<Job*>::iterator it;
    // for (it = jobs.begin(); it != jobs.end(); ++it){
    //     cout << "Job " << (*it)->SeqNum << endl;    
    //     (*it)->printNames();    

    // }


    if (file.is_open()) { file.close(); }
    return 0;
}