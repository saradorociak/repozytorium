from flask import Flask
import sys
import psycopg2
import urlparse

def select_tables():
#run
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse("")
	commands = (
		"""
		SELECT * FROM Workers
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
		cur.execute(commands)
		print("Liczba wierszy: ", cur.rowcount)
		row = cur.fetchone()
		while row is not None:
			print(row)
			row = cur.fetchone()
		cur.close()
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

if __name__ == '__main__':
	select_tables()


