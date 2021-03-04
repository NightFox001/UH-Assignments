

void printJobStates(string table){
    // print stuff
}

void printSnapShot(int time, int jobId, string action) {
    // do stuff
    // print table 
}


void coreRequest(requestedTime, jobID){
    if (core == FREE) {
        // core = BUSY;
    }
    // schedule CORE completion at currentTime + requestedTime for job jobID;
    } else {
    // queue jobID in readyQueue
    }
} 

void core_release (jobID) {
    if (readyQueue is not empty) {
        // pop first core request in readyQueue
        // schedule its completion at current_time + how_long
    } else {
        // core = FREE 
    }
    // process next job request for job jobID
}

struct Device {
    string status = "FREE";
    string type = "CORE"
    int busyCount = 0;
}

fetchJobs(int seqNo, int jobsLoaded, int mpl,) {
    while ((njobsinram < mpl)&&(nextjobtofetch < jobcount)) {
        njobsinram ++;
        seqno = nextjobtofetch;
        nextjobtofetch++;
        pop first job step from job seqno
        split into (request, duration)
        if (request == "CORE")
            process CORE request for job jobID[seqno]
        else
            printf("PANIC: FIRST STEP IS NOT A CORE REQUEST");
} // fetchjobs