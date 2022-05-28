import threading
import time
sem = threading.Semaphore(2)
threads = []
# sem.acquire()
# sem.release()


def fun1():
    while True:
        sem.acquire()
        print("1 bohrain")
        time.sleep(5)
        sem.release()
        print("1 release")


def fun2():
    while True:
        sem.acquire()
        print("2 bohrani")
        time.sleep(3)
        sem.release()
        print("2 release")


def fun3():
    while True:
        sem.acquire()
        print("3 bohrani")
        time.sleep(2)
        sem.release()
        print("3 release")


t = threading.Thread(target=fun1)
t.start()
t2 = threading.Thread(target=fun2)
t2.start()
t3 = threading.Thread(target=fun3)
t3.start()
