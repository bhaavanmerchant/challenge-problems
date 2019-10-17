from memory import Memory
from queue import Queue
from ingestor import Ingestor

from multiprocessing import Process
from time import sleep


def print_data(memory_store, queue_buffer):
    while (True):
        memory_store.print_memory()
        queue_buffer.print_q()
        sleep(2)

def expire_old(now_time, memory_store, queue_buffer):
    while (True):
        queue_buffer.housekeeping(now_time, memory_store)
        sleep(0.1)

if __name__ == "__main__":
    memory_store = Memory()
    queue_buffer = Queue(100)
    Ingestor(memory_store, queue_buffer, 'file')
    now_time = 1489926234422
    p = Process(target=expire_old, args=(now_time, memory_store, queue_buffer))
    p.start()
    q = Process(target=print_data, args=(memory_store, queue_buffer))
    q.start()
    p.join()
    q.join()