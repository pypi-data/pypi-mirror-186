import os

from SharedData.Logger import Logger
logger = Logger(__file__)
from SharedData.SharedDataAWSKinesis import KinesisStreamProducer
import decentralizedroutines.defaults as defaults 

producer = KinesisStreamProducer(os.environ['WORKERPOOL_STREAM'])

target='jcooloj@TRADEBOT00-PC'
target='ALL'

data = {
    'sender' : 'MASTER',
    'target' : target,
    'job' : 'logger',
    'repo' : 'logger'    
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "status"            
}
producer.produce(data,'command')