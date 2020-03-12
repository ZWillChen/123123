# this is an example about how to use the BatteryLearn lib
# for more procedure to use, check the mysql database

from BatteryData import GotionMySql
from BatteryDocs import DocProcess
import datetime


g_instance = GotionMySql(host_path='gordb.crjj5hgcxroo.us-east-1.rds.amazonaws.com', user_name='admin',
                         password_code='welcome123', db_name='GotionRDB')

g_instance.connect()
a = g_instance.runProcedure('QueryIssueStatus', ('', 'CSC', datetime.date(2019, 4, 13), datetime.date(2020, 2, 13)))
# argument needs to be tuple, % or empty for wildcard.


# example to download an 8D file
f = g_instance.runProcedure('DownloadFile', (1,), 0)

if f:
    with open('8Ddownload.xlsx', "wb") as local_file:
        local_file.write(f[0]['file'])

# example to process, parse and upload an 8D file to the db

xls_ins = DocProcess('8Dtemplate.xlsx')

(error_code, d_list, s_list) = xls_ins.process8Dfile()
if error_code != 0:
    print('the uploaded file has errors ! code: %s', error_code)
else:
    print('file was parsed successfully')

g_instance.upload8DTables(d_list)

