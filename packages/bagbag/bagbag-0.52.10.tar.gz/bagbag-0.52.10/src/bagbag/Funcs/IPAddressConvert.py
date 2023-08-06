import ipaddress

def IP2Int(ip:str) -> int:
    return int(ipaddress.IPv4Address(ip))

def Int2IP(intip:int) -> str:
    return str(ipaddress.IPv4Address(intip))

if __name__ == "__main__":
    print(IP2Int("192.168.0.1"))
    print(Int2IP(3232235521))