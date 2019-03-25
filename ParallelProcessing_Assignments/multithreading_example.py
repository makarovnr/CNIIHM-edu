import numpy as np
import threading
import time


PASSES = 100


def computing_foo(num):
    np.random.seed(num)
    val_list = np.random.pareto(100)
    return True, np.sum(val_list)


def single(passes=50):
    for i in range(passes):
        computing_foo(i)


def parallel(passes=50):
    for i in range(passes):
        thread = threading.Thread(target=computing_foo, args=np.random.randint(1, 10**10))
        thread.start()
        thread.join()


if __name__ == '__main__':
    parallel(passes=PASSES)
    single(passes=PASSES)

