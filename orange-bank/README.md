### Meetrend
This system is a proof of concept that generates top trends for currently happening meetups.

###### Input:
It consumes data from either a file or a streaming api about current meetup RSVPs.
In the default mode, it assumes a file called `meetup.json` to exist, and consumes it.

##### Installation:
```
pip install -r requirements.txt
```

###### Execution:
To execute it, please run
```
python trending.py
```

##### Design:
The system continuosly consumes data from an input source. For every input, it parses the topics associated with it, and updates the counter of the topic for a country, topic pair in the memory store. It also records the topic event in
a queue system.

The system also spawns a thread which consumes old events from the queuing system and expires them / decreases the counter from the memory, as a moving window of time passes over.

Currently the memory store and the queue system use native python data structures, but they can be easily replaced by distributed solutions like redis and kafka. (This wasn't done in this assignment because of packaging problems).

Anoher thread is also spawned by the system to display the results on stdout at a fixed interval to display the top 10 trending topics per country.

Depending on product requirements, this can be a GRPC server, which consumes a country code, and displays it's trend or also an API server.
