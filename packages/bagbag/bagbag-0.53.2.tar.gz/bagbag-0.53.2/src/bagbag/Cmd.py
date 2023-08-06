import subprocess
import typing 

def GetStatusOutput(cmd:str) -> typing.Tuple[int, str]:
    tsk = subprocess.Popen(["sh", "-c", cmd],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    status = tsk.wait()

    return status, tsk.stdout.read().decode('utf-8')

def GetOutput(cmd:str) -> str:
    _, output = GetStatusOutput(cmd)

    return output
