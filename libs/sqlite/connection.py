# Source.Python imports
import sqlite3
import os
from paths import PLUGIN_PATH

# Connect to the database
database = sqlite3.connect('%s/timer/data/database.db' %PLUGIN_PATH)
cursor = database.cursor()
execute = cursor.execute
fetchone = cursor.fetchone
fetchall = cursor.fetchall

# Check for database existance. If it's not there, it will autocreate it and the tables required.
execute	('''CREATE TABLE IF NOT EXISTS `players` (
	`steamid`	text UNIQUE,
	`name`	VARCHAR(40),
	`totaljumps`	INTEGER NOT NULL,
	PRIMARY KEY(steamid)
);''')

execute	('''CREATE TABLE IF NOT EXISTS `maplist` (
	`mapname`	text UNIQUE,
	`tier`	INT,
	PRIMARY KEY(mapname)
);''')

execute	('''CREATE TABLE IF NOT EXISTS `startzone` (
	`mapname`	text UNIQUE,
	`start1_x`	INT,
	`start1_y`	INT,
	`start1_z`	INT,
	`start2_x`	INT,
	`start2_y`	INT,
	`start2_z`	INT,
	PRIMARY KEY(mapname)
);''')

execute	('''CREATE TABLE IF NOT EXISTS `endzone` (
	`mapname`	text UNIQUE,
	`end1_x`	INT,
	`end1_y`	INT,
	`end1_z`	INT,
	`end2_x`	INT,
	`end2_y`	INT,
	`end2_z`	INT,
	PRIMARY KEY(mapname)
);''')


# Save the database.
def save():
    database.commit()

# Close the connection with database.
def close():
    cursor.close()
	
def quickSelect(stmt,cont=()):
    execute(stmt, cont)
    fetch = fetchall()
    if len(fetch) > 1:
        return fetch
    elif len(fetch) == 1:
        return fetch[0]
    else:
        return []