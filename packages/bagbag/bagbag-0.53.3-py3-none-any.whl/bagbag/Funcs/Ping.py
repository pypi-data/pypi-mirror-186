from pythonping import ping

from ..Tools import Chan
from .. import Re 
from ..Thread import Thread

class filelike():
    def __init__(self, c):
        self.c = c 

    def write(self, msg):
        msg = msg.strip()
        if msg != "":
            if 'timed out' in msg:
                self.c.Put("timeout")
            else:
                self.c.Put(float(Re.FindAll("Reply from .+?, .+? bytes in (.+)ms", msg)[0][0]))

def Ping(host, timeout:int=3, count:int=None, interval:int=1):
    c = Chan(0)
    fd = filelike(c)
    def run():
        if count:
            ping(host, timeout=timeout, count=count, interval=interval, verbose=True, out=fd)
        else:
            while True:
                ping(host, timeout=timeout, count=60, interval=interval, verbose=True, out=fd)
        c.Close()
    Thread(run)
    return c

if __name__ == "__main__":
    while True:
        for i in Ping("8.8.8.8"):
            Lg.Trace(i)