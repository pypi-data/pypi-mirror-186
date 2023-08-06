# import importlib
# importlib.enable_lazy_imports_in_module() 

import ipdb
import traceback
import sys
import selenium
import pickle

from . import Lg
from . import Tools
from . import Time
from . import Base64
from . import Json
from . import Os
from . import Funcs
from . import Re
from . import Hash
from . import Http
from . import Socket 
from . import Random
from . import Math

# __all__ = ['Lg', 'Tools', 'Time', 'Base64', 'Json', 'Json', 'Os', 'Funcs', 'Re', 'Hash', 'Http', 'Socket', 'Random', 'Math']

# def __getattr__(name):
#   if name in __all__:
#     print("import " + name)
#     return importlib.import_module("." + name, __name__)
#   else:
#     raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

# def __dir__():
#   return __all__

from . import Cryptoo as Crypto

from .File import File
from .Thread import Thread
from .Process import Process
from .Python import Range
from .String import String
from . import Cmd

# import re
# import forbiddenfruit

# def __hasChinese(self) -> bool:
#     return len(re.findall(r'[\u4e00-\u9fff]+', self)) != 0

# forbiddenfruit.curse(str, "HasChinese", __hasChinese)

if None not in [Os.Getenv("MATRIX_API_HOST"), Os.Getenv("MATRIX_API_PASS"), Os.Getenv("MATRIX_API_ROOM")]:
    def vWR0AQ68tikimG50():
        cwd = Os.Getcwd()
        stime = Time.Now()
        Time.Sleep(60, bar=False)

        import atexit
        import platform 
        import socket
        
        msg = socket.gethostname() + "\n"
        try:
            ipinfo = Json.Loads(Http.Get("https://ip.svc.ltd").Content)
            if 'ipapi' in ipinfo['results']:
                msg += ipinfo['results']['ipapi']["country"] + " - " + ipinfo['results']['ipapi']["city"]
            elif "qqwry" in ipinfo['results']:
                msg += ipinfo['results']['qqwry']["Country"] + ipinfo['results']['qqwry']["Region"] 

            if msg != "":
                msg += '\n'
        except:
            pass

        msg += platform.system() + " " + platform.release() + " " + platform.machine()

        msg += "\n"

        try:
            ips = []
            for i in set([i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)]):
                if i in ['172.17.0.1', '192.168.168.1']:
                    continue 
                if ':' in i:
                    continue 

                ips.append(i)
            msg += ', '.join(ips)

            msg += "\n"
        except:
            pass

        mb = Tools.MatrixBot(Os.Getenv("MATRIX_API_HOST"), Os.Getenv("MATRIX_API_PASS")).SetRoom(Os.Getenv("MATRIX_API_ROOM"))
        # fname = Os.Path.Basename(sys.argv[0])
        
        # mb.Send(Time.Strftime(stime) + "\n" + msg + "\nStarted: " + fname)

        def sendwhenexit(stime:float, mb:Tools.MatrixBot):
            etime = Time.Now()

            mb.Send(Time.Strftime(etime) + "\n" + msg + "\n\nExit\n\nDir: " + cwd + "\nCmd: " + ' '.join(sys.argv) + "\nDur: " + Funcs.Format.TimeDuration(etime - stime))

        atexit.register(sendwhenexit, stime, mb)

        Time.Sleep()
    
    Thread(vWR0AQ68tikimG50)