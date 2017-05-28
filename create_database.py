from flask import Flask
import sys
import psycopg2
import urlparse

def create_tables():
#run
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse("")
	commands = (
		"""
		CREATE TABLE Workers (
			USER_ID INTEGER,
			NAME VARCHAR(40),
			SURNAME VARCHAR(40),
			ADDED DATE
			)
		""",
		"""
		CREATE TABLE Events (
			ID SERIAL PRIMARY KEY,
			USER_ID INTEGER,
			KINDOF BOOLEAN,
			DATE timestamp
			)
		""")
	conn = None	
	try:
		conn = psycopg2.connect(
			database = url.path[1:],
			user = url.username,
			password = url.password,
			host = url.hostname,
			port = url.port
		)
		cur = conn.cursor()
		for command in commands:
			cur.execute(command)
		cur.close()
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

if __name__ == '__main__':
	create_tables()


