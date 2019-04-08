from multiprocessing import Pool
import os
import time
import random


def task(name):
    print("运行任务：%s %s" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("%s任务执行了%s" % (name, end-start))


if __name__ == "__main__":
    print("父进程%s " % os.getpid())

    p = Pool(50)
    for i in range(6):
        p.apply_async(task, args=(i,))
    p.close()
    p.join()