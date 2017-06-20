# coding=UTF-8
import MySQLdb
import json
import time

def SQL_func(data):
	localhost = ""
	username = ""
	passwd = ""
	DBName = ""

	json_data = data
	try:
	    decoded = json.loads(json_data)
	    # pretty printing of json-formatted string
	    print json.dumps(decoded, sort_keys=True, indent=4)
	    print "JSON parsing example: ", decoded['name']
	    name = decoded['name']
	    type_log = decoded['type']
	    print type_log
	
	except (ValueError, KeyError, TypeError):
	    print "JSON format error"

	try:
		# build DB connection information and set encoding to utf-8
		db = MySQLdb.connect(localhost, username, passwd, DBName, charset='utf8')

		cursor = db.cursor()
		cursor.execute("SELECT * FROM log")

		sql = "INSERT INTO log (device_name, date, log) VALUES (%s, %s, %s)"

		insert_data = (name, time.strftime('%d %b %Y %H:%M:%S'), type_log)

		# execute SQL statement
		
		cursor.execute(sql, insert_data)
		db.commit()

		"""
		# get multiple data
		results = cursor.fetchall()

		# loop for getting data
		for record in results: 
			col1 = record[0]
			col2 = record[1]
			col3 = record[2]
			col4 = record[3]

			print "%s, %s, %s, %s" % (col1, col2, col3, col4)
		"""
		# close connection
		db.close()

	except MySQLdb.Error as e:
		print "Error %d: %s" % (e.args[0], e.args[1])

