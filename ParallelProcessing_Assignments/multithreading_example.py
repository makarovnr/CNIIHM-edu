import time
from threading import Thread


total_sleep = 0


class MyThread(Thread):
    thread_list = []

    def __init__(self, name, am):
        Thread.__init__(self)
        self.name = name
        self.amount = am

    def run(self):
        global total_sleep
        amount = self.amount
        total_sleep += amount
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)
        MyThread.thread_list.append(self)


def create_threads(treads_num=5, total_wait=15.):
    for i in range(treads_num):
        name = "Thread #%s" % (i + 1)
        my_thread = MyThread(name, total_wait / treads_num)
        my_thread.start()

    for thread in MyThread.thread_list:
        thread.join()


if __name__ == "__main__":
    create_threads()
