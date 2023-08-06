try:
    from .. import Http
    # from .. import Lg
except:
    import sys 
    sys.path.append("..")
    import Http
    # import Lg

def GetPublicIP(HttpProxy:str=None) -> str:
    servers = [
        "http://ifconfig.me",
        "http://icanhazip.com",
        "http://ipinfo.io/ip",
        "http://api.ipify.org",
        "http://ident.me",
        "http://ipecho.net/plain",
    ]

    for s in servers:
        try:
            resp = Http.Get(s, Headers={"User-Agent": "curl/7.79.1"}, HttpProxy=HttpProxy)
            if resp.StatusCode != 200:
                continue
            else:
                return resp.Content.strip()
        except:
            pass 
    
    raise Exception("找不到公网IP, 可能是没有联网?")

if __name__ == "__main__":
    print(GetPublicIP("http://192.168.1.186:8899"))