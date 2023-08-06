import random 
from typing import Any
import copy

def Int(min:int, max:int) -> int:
    return random.randint(min, max)

def Choice(obj:list|str) -> Any:
    return random.choice(obj)

def String(length:int=8, charset:str="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") -> str:
    res = []
    while len(res) < length:
        res.append(random.choice(charset))
    
    return "".join(res)

def Shuffle(li:list) -> list:
    l = copy.copy(li)
    random.shuffle(l)
    return l

if __name__ == "__main__":
    print(Choice("doijwoefwe"))
    print(String(5))
    print(Shuffle([1,2,3,4,5]))