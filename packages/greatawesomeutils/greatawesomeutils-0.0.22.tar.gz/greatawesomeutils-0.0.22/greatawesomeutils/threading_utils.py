import multiprocessing
from multiprocessing import Queue
import time

def fn(q,f):
    result = f()
    q.put(result)

def on_execute_more_than_seconds(f, seconds, on_more_than):

    q = Queue()
    p = multiprocessing.Process(target=fn, args=(q,f,))
    p.start()
    p.join(seconds)
    if p.is_alive():
        # Terminate foo
        p.terminate()
        p.join()
        on_more_than()
    else:
         return q.get()


def long_run():
    time.sleep(2)
    return {"ok":True}

if __name__ == '__main__':

    print(on_execute_more_than_seconds(long_run, 1, lambda: print('Ran Too Long')))
