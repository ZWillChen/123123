from .BatteryData import GotionMySql
from .BatteryDocs import DocProcess
import datetime

g_instance = GotionMySql(host_path='gordb.crjj5hgcxroo.us-east-1.rds.amazonaws.com', user_name='admin',
                         password_code='welcome123', db_name='GotionRDB')
g_instance.connect()

# Run stored procedures
QueryIssue = g_instance.runProcedure('QueryIssue', ('', '', datetime.date(2019, 4, 13), datetime.date(2020, 2, 13)))  # argument needs to be tuple, % for wildcard, if leave empty, it is all wildcard
QueryMember = g_instance.runProcedure('QueryMember')

# A list to store all procedure results
QueryResults = [QueryIssue]

# Define export class
class QueryIssue(models.Model):


"""
    id = models.IntegerField(primary_key=True)
    customer = models.CharField(db_column='Customer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    identify = models.CharField(db_column='Identify', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(db_column='Project', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(db_column='Supplier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    part_num = models.CharField(db_column='Part_num', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ron_num = models.CharField(db_column='RON_num', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    open_date = models.DateField(db_column='Open Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    due_date = models.DateField(db_column='Due Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    closed_date = models.DateField(db_column='Closed Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file = models.TextField(db_column='File', blank=True, null=True)  # Field name made lowercase.
"""




