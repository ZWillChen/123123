__author__ = "Tony Li"
__credits__ = ["Tony Li", "new guy"]
__version__ = "1.1.0"
__maintainer__ = "Tony Li"
__status__ = "R&D"

DEBUG = 1

import os
import pandas as pd
from influxdb import DataFrameClient
import pymysql.cursors
from sqlalchemy import create_engine


## inlfuxdb realted
# -*- coding: utf-8 -*-
def fetch_file():
    file_list = os.listdir()
    for file in file_list:
        if ".csv" in file or '.xls' in file or '.dat' in file:
            return file


def load_file(filename):
    try:
        if '.xlsx' in filename:
            dfc = pd.read_excel(filename, sep='\t', encoding="GBK")
        elif ('.csv' in filename) or ('.xls' in filename):
            dfc = pd.read_csv(filename, sep='\t', encoding='GBK')
    except:
        dfc = pd.read_table(filename, sep='\t', encoding='GBK')
    return dfc


# deal with some encoding problems
def clean_df(df):
    try:
        col1 = df.columns.str.encode("latin1")
        col2 = [x.decode("gb2312") for x in col1]
        df.columns = col2
    except:
        print('skip re-endcoding')
    return df


def df_int_to_float(df):
    for i in df.select_dtypes('int64').columns.values:
        df[i] = df[i].astype(float)
    for i in df.select_dtypes('int32').columns.values:
        df[i] = df[i].astype(float)
    return df


def upload_to_influxdb(pd_obj=None, dbname='Test', measurement='Test', TEST=True, host_id='sw-wus-hx501q2'):
    chunk_size = 30000
    start_row = 0

    host = host_id
    port = 8086

    """Instantiate the connection to the InfluxDB client."""
    user = 'data_upload'
    password = 'guoxuangaoke'
    protocol = 'line'

    client = DataFrameClient(host, port, user, password, dbname)

    if TEST:
        print("Create pandas DataFrame")
        pd_obj = pd.DataFrame(data=list(range(30)),
                              index=pd.date_range(start='2019-1-16',
                                                  periods=30, freq='H'), columns=['测试'])
        print("Create database: " + dbname)
        client.create_database(dbname)

    print("Write DataFrame: " + measurement)

    (row_size, col_size) = pd_obj.shape

    # truncate the dataframe to 30000 entries per item before sending to influxdb

    while start_row < (row_size - 1):

        if (start_row + chunk_size) < row_size:

            print('size too large, chucking, start ' + str(start_row) \
                  + ' to ' + str(start_row + chunk_size))

            response = client.write_points(pd_obj[start_row: (start_row + chunk_size)], measurement, protocol=protocol)

            start_row += chunk_size + 1

        else:
            print('last bit, start ' + str(start_row) \
                  + ' to ' + str(row_size - 1))

            response = client.write_points(pd_obj[start_row:row_size - 1], measurement, protocol=protocol)

            start_row = row_size - 1

        print(response)

    # print("Write DataFrame with Tags")
    # client.write_points(df, 'demo',
    #                    {'k1': 'v1', 'k2': 'v2'}, protocol=protocol)

    # print("Read DataFrame")
    # client.query("select * from demo")

    # print("Delete database: " + dbname)
    # client.drop_database(dbname)


## mysql related


class GotionMySql:

    def __init__(self,
                 host_path='sw-wus-hx501q2',
                 user_name='data_viewer',
                 password_code='welcome123',
                 db_name='GotionDB'):

        self.host = host_path
        self.user = user_name
        self.password = password_code
        self.db = db_name

    def connect(self):

        try:
            setup = 'mysql://' + self.user + ':' + self.password + '@' \
                    + self.host + '/' + self.db
            self.alchemy_engine = create_engine(setup)
            connection = pymysql.connect(host=self.host,
                                         user=self.user,
                                         password=self.password,
                                         db=self.db,
                                         cursorclass=pymysql.cursors.DictCursor)
            self.cursor = connection.cursor()
            self.connection = connection
            print('connect to the database' + ' ' + self.db)

        except:
            print('can not connect to the database')

    def runSqlQuery(self, sql_statement: str) -> object:

        # try:
        #     self.cursor.execute(SQL_statement)
        #     return self.cursor.fetchall()
        try:
            return pd.read_sql(sql_statement, self.connection)
        except:
            print('query failed')

    def runProcedure(self, procedure_name, argument=(), df_return=1):

        arguments = str(argument)

        query = 'Call ' + procedure_name + arguments
        print('run mysql query [' + query + ']')

        self.cursor.callproc(procedure_name, argument)
        query_results = self.cursor.fetchall()
        self.connection.commit()
        if df_return and query_results:
            query_results = pd.DataFrame(query_results)

        return query_results

    def df2MysqlTable(self, table_name: str, table: pd.DataFrame):
        table.to_sql(table_name, self.alchemy_engine, if_exists='append', index=False)
        print('pushed ' + table_name + ' to the database')

    def __update8Dmembers(self, doc_members):
        member_list = self.runProcedure('QueryMember')
        rows_list = []
        for member_name in doc_members.unique():
            member_name = member_name.strip()
            if not member_list['Name'].str.contains(member_name).any():
                print('%s not find in the Member table' % member_name)
                rows_list.append({'Name': member_name})
                print('following members added to the member table')
        if rows_list:
            self.df2MysqlTable('Members', pd.DataFrame(rows_list))

    def __process8DTables(self, Action_Table):

        pass

    def upload8DTables(self, d_list: list):

        if d_list['D0'].empty:
            return 1, 'main issue table is empty'

        issue_id = d_list['D0']['ID'][1]
        list_issues = self.runProcedure('GetAllIssueNumbers')

        # cleanup the issue if already exist in the database
        if issue_id in list_issues['id']:
            self.runProcedure('CleanIssue', (issue_id,), 0)

        # prepare to update table "Issue" D0 and D2
        issue = d_list['D0']
        # assign description item to table issue
        issue['Description'] = d_list['D2'][d_list['D2'].columns[0]].values
        self.df2MysqlTable('Issue', issue)
        file_bin = pymysql.Binary(d_list['file'])
        self.runProcedure('UploadFile', (file_bin, issue_id))

        # prepare the Team table D1
        # get the member table to check if member already in the team
        meb_tb = self.runProcedure('QueryMember')
        tm_tb = d_list['D1']

        if not tm_tb.empty:
            self.__update8Dmembers(tm_tb['Name'])  # check if the existing table needs update
            meb_tb = self.runProcedure('QueryMember')
            rows_list = []

            for name in tm_tb['Name']:
                name = name.strip()  # remove leading and trailing whitespace
                a = meb_tb['Name'].str.contains(name)
                if a.any():
                    mem_indx = meb_tb['id'][a].iloc[-1]
                    tmp = {'issue_id': issue_id,
                           'member_id': mem_indx}
                    rows_list.append(tmp)
            team = pd.DataFrame(rows_list)
            self.df2MysqlTable('Team', team)
        else:
            pass

        # process D3-D7
        print('test')
        rename_list1 = {'D3': 'Contain_Symptons',
                        'D4': 'Root_Causes',
                        'D5': 'Select/Verify_Corrective_Actions',
                        'D6': 'Implement/Validate_Corrective_Actions',
                        'D7': 'Prevent_Recurrence'}

        rename_list2 = {'D3': 'Implementation_Date',
                        'D4': 'Evidence',
                        'D5': 'Verification',
                        'D6': 'Implementation_Date',
                        'D7': 'Implementation_Date'}

        for d_tmp in ('D3', 'D4', 'D5', 'D6', 'D7'):
            tmp = d_list[d_tmp]

            tmp.rename(columns={tmp.columns[0]: rename_list1[d_tmp]}, inplace=True)
            tmp.rename(columns={tmp.columns[1]: rename_list2[d_tmp]}, inplace=True)

            tmp['Issue_id'] = issue_id

            self.df2MysqlTable(d_tmp, tmp)

        # process D8
        tm_tb = d_list['D8']
        if not tm_tb.empty:

            rows_list = []

            for name in tm_tb['Name']:
                name = name.strip()  # remove leading and trailing whitespace
                a = meb_tb['Name'].str.contains(name)
                if a.any():
                    mem_indx = meb_tb['id'][a].iloc[-1]
                    tmp = {'issue_id': issue_id,
                           'member_id': mem_indx,
                           'Closure Date':
                               tm_tb['Closure Date'][a[a==True].index[0]]} # add the closure time
                    rows_list.append(tmp)
            D8 = pd.DataFrame(rows_list)
            self.df2MysqlTable('D8', D8)
        else:
            return 1, 'the recognized team member is not in database or your team session'

        # process the Actions items
        actions_items = d_list['Action']

        if not actions_items.empty:
            actions_items['Member_id'] = -1
            actions_items['Issue_id'] = issue_id
            for i in range(len(actions_items['Owner'])):
                name = actions_items['Owner'][i]
                a = meb_tb['Name'].str.contains(name)
                if a.any():
                    mem_indx = meb_tb['id'][a].iloc[-1]
                    actions_items.at[i, 'Member_id'] = mem_indx
                else:
                    return 1, 'you have someone not in the team but in the action list'
            actions_items = actions_items.drop(columns='Owner')

            self.df2MysqlTable('Action', actions_items)

        return 0, 'success'

    def fetchAllTablesName(self):
        tables = self.runSqlQuery \
            ('SELECT table_name FROM information_schema.tables where table_schema='
             '\'' + self.db + '\';')
        return pd.DataFrame(tables), tables

    def downloadTable(self, tablename):

        sql = 'SELECT * FROM ' + tablename + ';'

        listdata = self.runSqlQuery(sql)

        #         dfcols   = [k for k in a[1]]

        #         dfdata   = []

        #         for ai in a:
        #             dfdata.append([v for v in ai.values()])

        dftable = pd.DataFrame(listdata)

        return dftable, listdata
