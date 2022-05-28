import threading
import time
import logging

SEMLEN = 8
A = 0
threads = []

car_wash_sem = threading.Semaphore(8)
A_B_sem = threading.Semaphore(2)
C_sem = threading.Semaphore()
D_sem = threading.Semaphore()
# sem.acquire()
# sem.release()


def wash(id: int):
    global A
    A_B_sem.acquire()
    if A == 0:
        A = 1
        logging.info("car{} is washing at [A]".format(id))
        time.sleep(0.5)
        A = 0
    else:
        logging.info("car{} is washing at [B]".format(id))
        time.sleep(0.5)

    A_B_sem.release()
    logging.info("car{} end washing".format(id))
    dry(id)


def dry(id: int):
    C_sem.acquire()
    logging.info("worker is washing the car ...")
    logging.info("car{} is drying..".format(id))
    time.sleep(0.5)
    C_sem.release()
    logging.info("car{} end drying".format(id))
    logging.info("worker has done washing car{} and goes to sleep...".format(id))
    pay(id)


def pay(id: int):
    D_sem.acquire()
    logging.info("car{} is paying..".format(id))
    time.sleep(0.5)
    D_sem.release()
    logging.info("car{} end paying".format(id))


def car(id: int):
    car_wash_sem.acquire()
    logging.info("car{} is going to carwash..".format(id))
    wash(id)
    car_wash_sem.release()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    n = int(input("number of cars:"))
    # creating threads
    for i in range(n):
        th = threading.Thread(target=car, args=(i+1,), name=str(i+1))
        threads.append(th)
        th.start()
    # end of threads
    for thread in threads:
        thread.join()
        logging.info("car%s washing is done...", thread.name)
