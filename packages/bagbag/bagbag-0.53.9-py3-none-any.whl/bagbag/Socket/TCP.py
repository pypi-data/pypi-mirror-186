from __future__ import annotations

import socket

import sys 
sys.path.append("..")
try:
    from bagbag.Tools import Chan
    from bagbag.Thread import Thread 
except:
    from Tools import Chan
    from Thread import Thread

import typing 
import pickle

class StreamClosedError(Exception):
    pass

class TCPPeerAddress():
    def __init__(self, host:str, port:int):
        self.Host = host 
        self.Port = port 
    
    def __str__(self) -> str:
        return f"TCPPeerAddress(Host={self.Host}, Port={self.Port})"
    
    def __repr__(self) -> str:
        return self.__str__()

class PacketConnection():
    def __init__(self, sc:StreamConnection) -> None:
        self.sc = sc 

    def PeerAddress(self) -> TCPPeerAddress:
        return TCPPeerAddress(self.sc.Host, self.sc.Port)

    def Close(self):
        self.sc.Close()

    def Send(self, data:typing.Any):
        datab = pickle.dumps(data, protocol=2)
        length = len(datab)
        lengthb = length.to_bytes(8, "big")
        self.sc.SendBytes(lengthb + datab)

    def Recv(self) -> typing.Any:
        length = int.from_bytes(self.sc.RecvBytes(8), "big")
        datab = self.sc.RecvBytes(length)
        return pickle.loads(datab)
    
    def __str__(self):
        return f"PacketConnection(Host={self.sc.Host} Port={self.sc.Port})"
    
    def __repr__(self):
        return f"PacketConnection(Host={self.sc.Host} Port={self.sc.Port})"
        
class StreamConnection():
    def __init__(self, ss:socket, host:str, port:int):
        self.ss = ss
        self.Host = host
        self.Port = port 
    
    def PeerAddress(self) -> TCPPeerAddress:
        return TCPPeerAddress(self.Host, self.Port)
    
    def Send(self, data:str):
        self.SendBytes(data.encode('utf-8'))

    def SendBytes(self, data:bytes):
        try:
            self.ss.sendall(data) 
        except BrokenPipeError:
            raise StreamClosedError("发送数据出错")

    def Recv(self, length:int) -> str:
        return self.RecvBytes(length).decode('utf-8')

    def RecvBytes(self, length:int) -> bytes:
        buf = self.ss.recv(length)
        if buf:
            return buf 
        else:
            raise StreamClosedError("接收数据出错")
    
    def Close(self):
        self.ss.close()
    
    def __str__(self):
        return f"StreamConnection(Host={self.Host} Port={self.Port})"
    
    def __repr__(self):
        return f"StreamConnection(Host={self.Host} Port={self.Port})"

class Listen():
    def __init__(self, host:str, port:int, waitQueue:int=5):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((host, port))
        self.s.listen(waitQueue)

        self.q:Chan[StreamConnection] = Chan(10)

        Thread(self.acceptloop)
    
    def acceptloop(self):
        while True:
            ss, addr = self.s.accept()
            self.q.Put(StreamConnection(ss, addr[0], addr[1]))
    
    def Accept(self) -> Chan[StreamConnection]:
        return self.q
    
    def AcceptOne(self) -> StreamConnection:
        return self.q.Get()
    
    def Close(self):
        self.s.close()

def Connect(host:str, port:int) -> StreamConnection:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((host, port))  
    return StreamConnection(s, host, port)

if __name__ == "__main__":
    import time 

    def test1():
        def server():
            print("listen on: ", "127.0.0.1", 22222)
            l = Listen("127.0.0.1", 22222)
            for s in l.Accept():
                print("Connect from:",s.PeerAddress())
                print("Receive:",s.Recv(512))
                print("Close on server side")
                s.Close()
            
        Thread(server)

        time.sleep(2)

        def client():
            print("connect to", "127.0.0.1", 22222)
            s = Connect("127.0.0.1", 22222)
            s.Send(str(int(time.time())))
            time.sleep(1)
            print("Close on client side")
            s.Close()

        for _ in range(10):
            client()
            time.sleep(1)
    # test1()

    l = Listen("127.0.0.1", 22222)
    s = l.AcceptOne()

    while True:
        # print(type(s.RecvBytes(1024)))
        time.sleep(1)
        s.Send(str(time.time()))