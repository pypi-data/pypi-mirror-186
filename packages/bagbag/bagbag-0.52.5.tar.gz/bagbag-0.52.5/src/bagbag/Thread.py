import threading 
from typing import Any

def Thread(func, *args:Any, daemon:bool=True) -> threading.Thread:
    t = threading.Thread(target=func, args=args)
    t.daemon = daemon 
    t.start()

    return t 

if __name__ == "__main__":
    import time 

    def p(s:str, ss:str):
        while True:
            time.sleep(1)
            print(s, ss, time.time())

    t = Thread(p, "oo", "kk")

    while True:
        time.sleep(1)



