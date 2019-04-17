import time
import numpy as np
from mpi4py import MPI


def load_func_norm(x, type=5.):
    arr = 0
    for y in x:
        arr += y ** pow
    return arr


def compute(sequence_length=10000000):
    # generating data
    x = np.random.randn(sequence_length)

    # single pass
    start = time.time()
    res = load_func(x)
    stop = time.time()
    
    # MPI block below, NUM is number of nodes
    # can be run with mpiexec -n NUM python mpiProg.py or ./mpi_launch.sh NUM

    '''
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    i = len(x) // size
    buf = x[i * rank: i * (rank + 1)]
    arr = load_func(buf)
    res = comm.allreduce(arr)
    '''

    print(f"Single pass time is {stop - start}")
    print(f"Computed result: {res}")


if __name__ == '__main__':
    compute(10000000)
