# this is an example about how to use the BatteryLearn lib
# for more procedure to use, check the mysql database

from .BatteryData import GotionMySql
from .BatteryDocs import DocProcess
import datetime


g_instance = GotionMySql(host_path='gordb.crjj5hgcxroo.us-east-1.rds.amazonaws.com', user_name='admin',
                         password_code='welcome123', db_name='GotionRDB')
g_instance.connect()

# Multiple Queries
QueryIssue = g_instance.runProcedure('QueryIssue', ('', '', datetime.date(2019, 4, 13), datetime.date(2020, 2, 13)))  # argument needs to be tuple, % for wildcard, if leave empty, it is all wildcard

# results = []
#
# print(len(QueryIssue))
# print(len(QueryIssue.columns[1:-1]))
# print(QueryIssue.columns[1:-1])
# print("---")
# result = []
# for i in range(len(QueryIssue)):
#     inner = []
#     for j in range(1, len(QueryIssue.columns[1:-1]) + 1):
#         print(QueryIssue.iat[i, j])
#         inner.append(QueryIssue.iat[i, j])
#     print("diyige")
#     results.append(inner)
# print(results)
# for row in QueryIssue.itertuples(index=False):
#     inner = []
#     for c in QueryIssue.columns[1:-1]:
#         print(c)
#         for value in QueryIssue[c].values:
#             print(value)
#             inner.append(value)
#
#     results.append(inner)
# print(results)
