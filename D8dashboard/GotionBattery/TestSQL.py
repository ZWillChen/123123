# this is an example about how to use the BatteryLearn lib
# for more procedure to use, check the mysql database

from .BatteryData import GotionMySql
from .BatteryDocs import DocProcess
import datetime


g_instance = GotionMySql(host_path='gordb.crjj5hgcxroo.us-east-1.rds.amazonaws.com', user_name='admin',
                         password_code='welcome123', db_name='GotionRDB')
# Test connection
# g_instance.connect()

# Sample Query
# argument needs to be tuple, % for wildcard, if leave empty, it is all wildcard

# QueryIssue = g_instance.runProcedure('QueryIssue', ('', '', datetime.date(2019, 4, 13), datetime.date(2020, 2, 13)))

