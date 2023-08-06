from kafka import KafkaProducer as kkp
from kafka import KafkaConsumer as kkc
import json

class KafkaProducer():
    def __init__(self, topic:str, servers:str|list, value_serializer):
        self.kp = kkp(bootstrap_servers=servers, value_serializer=value_serializer)
        self.topic = topic
    
    def Send(self, data:dict):
        self.kp.send(self.topic, data)

class KafkaConsumer():
    def __init__(self, topic:str, servers:str|list, group_id:str=None, auto_offset_reset:str='earliest'):
        self.kc = kkc(topic, bootstrap_servers=servers, group_id=group_id, auto_offset_reset=auto_offset_reset)
    
    def Get(self) -> dict:
        return json.loads(next(self.kc).value.decode())

    def __iter__(self) -> dict:
        while True:
            try:
                yield self.Get()
            except StopIteration:
                return 

class Kafka():
    def __init__(self, topic:str, servers:str|list):
        """
        This function initializes the Kafka object with the topic and servers
        server 可以是字符串也可以是列表, 例如"192.168.168.70:9092"或者["192.168.168.70:9092", "192.168.168.71:9092"]
        
        :param topic: The topic to which the message will be published
        :type topic: str
        :param servers: A list of Kafka servers to connect to
        :type servers: str|list
        """
        self.topic = topic
        self.servers = servers 
    
    def Producer(self, value_serializer=lambda m: json.dumps(m).encode()) -> KafkaProducer:
        return KafkaProducer(self.topic, self.servers, value_serializer)

    def Consumer(self, group_id:str=None, auto_offset_reset:str='earliest') -> KafkaConsumer:
        return KafkaConsumer(self.topic, self.servers, group_id, auto_offset_reset)

if __name__ == "__main__":
    import time 
    import sys

    kafka = Kafka("test_topic", '192.168.168.70:9092')
    if sys.argv[1] == 'p':
        p = kafka.Producer()
        while True:
            p.Send({"time": time.time()})
            time.sleep(1)
            
    elif sys.argv[1] == 'c':
        c = kafka.Consumer()
        print("Get one:", c.Get())
        for i in c:
            print("Get with for loop:", i)