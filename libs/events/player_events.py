# Source.Python imports
from events import Event
from players.entity import Player
from engines.server import global_vars
from messages import SayText2

# Source.Python globals
mapname = global_vars.map_name

# Timer imports
from ..sqlite.connection import fetchone, execute, quickSelect, save

# Cached stuff.
jumps = {}

@Event('player_activate')
def _player_activate(event):
	player = Player.from_userid(event['userid'])
	steamid = player.steamid

	# Check if it's a bot or an actual player
	if player.is_bot():
		return

	# Database calls...
	execute('''SELECT steamid FROM players WHERE steamid=?''', (player.steamid,))
	result = fetchone()
	
	if not result: # If player never was on the server before we insert him into the database
		execute('''INSERT INTO players (steamid, name, totaljumps) VALUES(?, ?, ?)''', (player.steamid, player.name, 0))
	else: # Otherwise just update his name to current one.
		execute('''UPDATE players SET name=? WHERE steamid=?''', (player.name, player.steamid))
	save()
	
@Event('player_spawn')
def _player_spawn(event):
	player = Player.from_userid(event['userid'])
	steamid = player.steamid

	# Check if it's a bot or an actual player
	if player.is_bot():
		return

	# Let's check if the map has zones set up. If not, we let the player know.
	no_zones = quickSelect('''SELECT ? FROM startzone WHERE start1_x=?''', (mapname, 0))
	if no_zones:
		SayText2("\x07ff0000Map has no zones. Contact an admin...").send(player)

	# Cache the player to store his playing statistics.
	if steamid not in jumps:
		jumps[steamid] = {}
		jumps[steamid]['jump_count'] = 0
	
@Event('player_disconnect')
def _player_disconnect(event):
	player = Player.from_userid(event['userid'])
	steamid = player.steamid

	# Check if it's a bot or an actual player
	if player.is_bot():
		return

	# Database calls...
	execute('''SELECT steamid FROM players WHERE steamid=?''', (player.steamid,))
	result = fetchone()

	# Sometimes players will "disconnect" before connecting to the server (Magic? Hi Volvo™)...
	if not result: 
		execute('''INSERT INTO players (steamid, name) VALUES(?, ?)''', (player.steamid, player.name))
	else:
		execute('''UPDATE players SET name=?, totaljumps=totaljumps+? WHERE steamid=?''', (player.name, jumps[steamid]['jump_count'], player.steamid))
	save()

	# Player have disconnected. Clear the player from cache.
	del jumps[steamid]
		
@Event('player_jump')
def _player_jump(event):
	player = Player.from_userid(event['userid'])
	steamid = player.steamid
	#name = player.name

	# Count the player's jumps. Will be added to his general statistics on disconnect.
	if steamid in jumps:
		jumps[steamid]['jump_count'] += 1

	"""
	userid = player.userid

	vel = player.velocity
	x = vel.x
	y = vel.y
	truevel = (x*x + y*y)**0.5

	# Check if it's a bot or an actual player
	if player.is_bot():
		return

	SayText2(f"{name} - uid: {userid} || sid: {steamid} - Velocity: {truevel:.2f}").send()
	"""