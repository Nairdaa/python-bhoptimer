# Source.Python imports
import sqlite3
from listeners.tick import Delay

# Timer imports
from .libs.sqlite import connection
from .libs.events import player_events, round_events
from .libs.zones import create

def load():
	print("Hello.")

def unload():
	# Save database
	connection.save()

	# Unloading database connections
	connection.close()
	print("Everything went well, all connections closed!") 