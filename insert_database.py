from flask import Flask
import sys
import psycopg2
import urlparse

def insert_tables():
#run
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse("")
	commands = (
		"""
		INSERT INTO Workers (
			USER_ID,
			NAME,
			SURNAME,
			ADDED
			)
		VALUES (
			1,
			'Luka',
			'Malakhau',
			'now'
			),
			(
			2,
			'Bartosz',
			'Gorski',
			'now'
			),
			(
			3,
			'Darek',
			'Kowalczyk',
			'now'
			),
			(
			5,
			'Bartlomiej',
			'Pieta',
			'now'
			),
			(
			8,
			'Adrian',
			'Beben',
			'now'
			),
			(
			44,
			'Pan',
			'Wasaty',
			'now'
			)
		""",
		"""
		INSERT INTO Events (
			USER_ID,
			KINDOF,
			DATE
			)
		VALUES (
			1,
			't',
			'now'
			),
			(
			2,
			't',
			'now'
			),
			(
			2,
			'f',
			'now'
			),
			(
			3,
			't',
			'now'
			),
			(
			1,
			'f',
			'now'
			),
			(
			3,
			'f',
			'now'
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
	insert_tables()


