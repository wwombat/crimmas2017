import os
import sys
import time

def twiddle(secs):
    len_sleep = 0.1
    times = int(secs / len_sleep)
    frames=['|', '/', '-', '\\']
    for i in range(times):
        index = i % len(frames)
        sys.stdout.write(frames[index])
        sys.stdout.flush()
        time.sleep(len_sleep)
        sys.stdout.write('\x08')
    print()

twiddle(3)
