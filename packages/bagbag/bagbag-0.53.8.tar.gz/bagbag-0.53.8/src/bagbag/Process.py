import multiprocessing 
from typing import Any

def Process(func, *args:Any, daemon:bool=True) -> multiprocessing.Process:
    p = multiprocessing.Process(target=func, args=args)
    p.daemon = daemon 
    p.start()

    return p 

# import time 
# 
# def p(s:str, ss:str):
#     while True:
#         time.sleep(1)
#         print(s, ss, time.time())

if __name__ == "__main__":
    p = Process(p, "oo", "kk")

    while True:
        time.sleep(1)



