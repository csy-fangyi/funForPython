# -*- coding: utf-8 -*-

# !/usr/bin/python
import Queue
import sys
import threading
import time


class ThreadTask(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        while True:
            try:
                do, args = self.work_queue.get(block=False)
                do(args)
                self.work_queue.task_done()
            except:
                break


class ThreadPoolManager(object):
    def __init__(self):
        self.work_queue = Queue.Queue()
        self.threads = []

    def add_job(self, func, *args):
        self.work_queue.put((func, list(args)))

    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive(): item.join()

    def run(self, thread_num):
        for i in range(thread_num):
            self.threads.append(ThreadTask(self.work_queue))


def process_run(cmd):
    print (cmd)


def start_process(type, code):
    url_file = "/tmp/%s" % code
    threadpool = ThreadPoolManager()
    while True:
        try:
            with open(url_file) as fp:
                all_lines = fp.readlines()
                for line in all_lines:
                    line_arr = line.strip('\n')
                    threadpool.add_job(process_run, line_arr)
            threadpool.run(6)
            threadpool.wait_allcomplete()
        except:
            break

        time.sleep(1000)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        start_process(sys.argv[1], sys.argv[2])
    else:
        print ("error argv...")
