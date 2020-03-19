from BatteryDocs import DocProcess
import sys

# if sys.argv[1] =="-help" or sys.argv[1] == "-h":
#     print("\n\n a2lCheck.exe <a2lfile_samepath> <verbose_level>\n 0 - only show number of interface with issues \n 1 - print out all names of interface with issues \n 2 - also print out all interface names (cautious)")
#     sys.exit()
#
# filename = sys.argv[1]
# try:
#     verbose = sys.argv[2]
# except:
#     verbose = 0

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='sw-wus-hx501q2',
                             user='data_viewer',
                             password='welcome123',
                             db='GotionDB',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()