import threading
import logging

threads = []


def start_thread(object, id: int):
    global threads

    th = threading.Thread(target=object, name=str(id))
    threads.append(th)
    th.start()


def end_threads():
    global threads

    for thread in threads:
        thread.join()
        logging.info("Thread car%s done...", thread.name)
