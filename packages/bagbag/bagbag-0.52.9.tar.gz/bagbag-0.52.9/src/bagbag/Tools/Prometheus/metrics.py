import prometheus_client as pc

class PrometheusCounter():
    def __init__(self, name:str, help:str, registry:pc.CollectorRegistry) -> None:
        self.c = pc.Counter(name, help, registry=registry)
    
    def Add(self, num:int|float=1):
        self.c.inc(num)

class PrometheusCounterVec():
    def __init__(self, name:str, labels:list[str], help:str, registry:pc.CollectorRegistry) -> None:
        self.labels = labels 
        self.c = pc.Counter(name, help, labels, registry=registry)
        self.current = {}
    
    def Add(self, labels:dict|list, num:int|float=1):
        """
        It adds a new label to the metric.
        
        :param labels: a list of labels, or a dict of labels
        :type labels: dict|list
        :param num: The number to increment the counter by, defaults to 1
        :type num: int|float (optional)
        """
        if type(labels) == dict:
            lb = []
            for k in self.labels:
                if k in labels:
                    lb.append(labels[k])
                else:
                    lb.append("")
        elif type(labels) == list:
            if len(self.labels) == len(labels):
                lb = labels
            else:
                lb = labels[:len(self.labels)] + [""]*(len(self.labels) - len(labels))

        lbr = repr(lb)
        if lbr not in self.current:
            self.current[lbr] = 0

        self.current[lbr] = self.current[lbr] + num
        self.c.labels(*lb).inc(num)
    
    def Set(self, labels:dict|list, num:int|float=1):
        """
        It adds a new label to the metric.
        
        :param labels: a list of labels, or a dict of labels
        :type labels: dict|list
        :param num: The number to increment the counter by, defaults to 1
        :type num: int|float (optional)
        """
        if type(labels) == dict:
            lb = []
            for k in self.labels:
                if k in labels:
                    lb.append(labels[k])
                else:
                    lb.append("")
        elif type(labels) == list:
            if len(self.labels) == len(labels):
                lb = labels
            else:
                lb = labels[:len(self.labels)] + [""]*(len(self.labels) - len(labels))

        lbr = repr(lb)
        if lbr not in self.current:
            self.current[lbr] = 0
        
        if num < self.current[lbr]:
            raise Exception(f"Count类型只能设置更大类型的值, 当前值和想设置的值为: {self.current}, {num}")
        
        if num == self.current[lbr]:
            return 

        self.c.labels(*lb).inc(num - self.current[lbr])
        self.current[lbr] = num

class PrometheusGauge:
    def __init__(self, name:str, help:str, registry:pc.CollectorRegistry) -> None:
        self.g = pc.Gauge(name, help, registry=registry)
    
    def Set(self, num:int|float):
        self.g.set(num)

class PrometheusGaugeVec():
    def __init__(self, name:str, labels:list[str], help:str, registry:pc.CollectorRegistry) -> None:
        self.labels = labels 
        self.g = pc.Gauge(name, help, labels, registry=registry)
    
    def Set(self, labels:dict|list, num:int|float):
        """
        It adds a number to the graph.
        
        :param labels: The labels of the histogram
        :type labels: dict|list
        :param num: The number of times the label is added, defaults to 1
        :type num: int|float (optional)
        """
        if type(labels) == dict:
            lb = []
            for k in self.labels:
                if k in labels:
                    lb.append(labels[k])
                else:
                    lb.append("")
        elif type(labels) == list:
            if len(self.labels) == len(labels):
                lb = labels
            else:
                lb = labels[:len(self.labels)] + [0]*(len(self.labels) - len(labels))
        self.g.labels(*lb).set(num)
