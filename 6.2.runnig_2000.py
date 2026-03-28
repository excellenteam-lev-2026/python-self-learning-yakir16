import math
import time

def running_2000(func, *args, **kwargs):
        try:
            start = time.perf_counter()
            func(*args, **kwargs)
            end = time.perf_counter()
            length = end - start
            return length
        except TypeError as e:
            try:
                start = time.perf_counter()
                print(func(args))
                end = time.perf_counter()
                length = end - start
                return length
            except TypeError:
                 raise e



if __name__ == "__main__":
   running_2000()