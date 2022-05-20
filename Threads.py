import threading
import logging

threads = []


def start_thread(rule):
    global threads

    th = threading.Thread(target=rule.run, name=rule.getName())
    threads.append(th)
    th.start()


def end_threads():
    global threads

    for thread in threads:
        thread.join()
        logging.info("Thread %s done...", thread.name)
