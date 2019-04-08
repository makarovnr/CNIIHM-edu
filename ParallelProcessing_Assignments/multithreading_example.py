import time

from threading import Thread


total_sleep = 0


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        global total_sleep
        amount = 10
        total_sleep += amount
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)


def create_threads():
    for i in range(5):
        name = "Thread #%s" % (i + 1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_threads()
