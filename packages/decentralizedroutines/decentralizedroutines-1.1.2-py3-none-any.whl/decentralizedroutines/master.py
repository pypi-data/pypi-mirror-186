import os,sys

from SharedData.Logger import Logger
logger = Logger(__file__)
from SharedData.SharedDataAWSKinesis import KinesisStreamProducer
import decentralizedroutines.defaults as defaults 

producer = KinesisStreamProducer(os.environ['WORKERPOOL_STREAM'])

if len(sys.argv)>=2:
    data = str(sys.argv[1])
else:
    Logger.log.error('command not provided!')
    raise Exception('command not provided!')

producer.produce(data,'command')

# target='jcooloj@TRADEBOT00-PC'
# target='ALL'

# data = {
#     'sender' : 'MASTER',
#     'target' : target,
#     'job' : 'logger',
#     'repo' : 'logger'    
# }
# producer.produce(data,'command')


# data = {
#     'sender' : 'MASTER',
#     'target' : target,
#     'job' : 'scheduler',
#     'args' : 'TRADEBOT06'
# }
# producer.produce(data,'command')

# data = {
#     "sender" : "MASTER",
#     "target" : target,
#     "job" : "status"            
# }
# producer.produce(data,'command')