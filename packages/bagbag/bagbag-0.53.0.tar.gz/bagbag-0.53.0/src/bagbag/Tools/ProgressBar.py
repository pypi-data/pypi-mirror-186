import tqdm

class ProgressBarClass():
    def __init__(self, t:tqdm.tqdm):
        self.t = t 
    
    def Add(self, num:int=1):
        self.t.update(num)
    
    def Close(self):
        self.t.close()

def ProgressBareee(iterable_obj=None, startfrom=0, total=None, title=None, leave=False):
    """
    It creates a progress bar for iterable objects.
    
    :param iterable_obj: The iterable object you want to iterate over
    :param startfrom: The position of the progress bar, defaults to 0 (optional)
    :param total: The number of expected iterations. If unspecified, len(iterable) is used if possible
    :param title: Title of the progress bar
    :param leave: If True, tqdm will leave the progress bar on the screen after completion, defaults to
    False (optional)
    :return: A progress bar object.
    """
    if iterable_obj:
        return tqdm.tqdm(iterable_obj, dynamic_ncols=True, total=total, leave=leave, desc=title)
    
class ProgressBar():
    def __init__(self, iterable_obj=None, total=None, title=None, leave=False):
        self.iterable = iterable_obj
        self.tqdm = tqdm.tqdm(iterable_obj, dynamic_ncols=True, total=total, leave=leave, desc=title)
        self.total = total if total != None else 0
        self.current = 0

    def Add(self, num:int=1):
        self.current = self.current + num
        self.tqdm.update(num)
    
    def Set(self, num:int):
        if num < self.current:
            raise Exception("不能小于当前进度")

        if num == self.current:
            return

        step = num - self.current
        self.current = num
        self.tqdm.update(step)
    
    def Close(self):
        self.tqdm.close()
    
    def SetTotal(self, total:int):
        self.tqdm.total = total 
        self.tqdm.refresh()
    
    def Total(self) -> int:
        return self.total 

    def Current(self) -> int:
        return self.current 
    
    def Remain(self) -> int:
        return self.total - self.current 

    def __iter__(self):
        if not self.iterable:
            raise Exception("可迭代的参数没有传入, 需要传入, 例如Tools.ProgressBar(range(10))")

        for obj in self.iterable:
            # print("update")
            self.tqdm.update(1)
            yield obj 

        self.tqdm.close()
        return 
    
if __name__ == "__main__":
    import time
    for i in ProgressBar(range(10), title="test sleep"):
        time.sleep(0.3)
        #   print(i)
        
    p = ProgressBar(total=10, title="test sleep")
    for i in range(10):
        time.sleep(0.3)
        p.Add(1) 
    p.Close()