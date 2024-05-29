import numpy as np
import time

def say_hello():
    print("Hello, World!")

def make_array():
    N = 10_000_000
    t1 = time.time()
    arr = np.random.randint(1,101,N)
    t2 = time.time()
    print(f"Time to generate random array with {N} elements: {t2-t1:.2f}s.")

if __name__ == "__main__":
    say_hello()
    make_array()