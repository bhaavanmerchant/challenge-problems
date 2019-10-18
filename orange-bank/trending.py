from memory import Memory
from queue import Queue
from ingestor import Ingestor

from threading import Thread
from time import sleep

EXPIRATION_FREQUENCY = 0.01             # Results will be accurate till 0.01 seconds
RESULTS_FREQUENCY = 10                  # Results will be printed every 10 seconds
CURRENT_TIME = 1489926234422            # An epoch of time. We simulate this, to be a reasonable value for the data within the file
EXPIRATION_TIMEOUT = 100000             # This is the epoch length of the moving window. We're interested in the top trends of last 100000 seconds

def results(memory_store, queue_buffer):
    while (True):
        print(memory_store.all_country_trends())
        sleep(RESULTS_FREQUENCY)

def housekeeping_daemon(now_time, memory_store, queue_buffer):
    while (True):
        queue_buffer.housekeeping(now_time, memory_store)
        sleep(EXPIRATION_FREQUENCY)

if __name__ == "__main__":
    memory_store = Memory()
    queue_buffer = Queue(EXPIRATION_TIMEOUT)
    Ingestor(memory_store, queue_buffer, 'file')
    now_time = CURRENT_TIME
    housekeeper = Thread(target=housekeeping_daemon, args=(now_time, memory_store, queue_buffer))
    trend_printer = Thread(target=results, args=(memory_store, queue_buffer))
    housekeeper.start()
    trend_printer.start()
