# Source.Python imports
from listeners.tick import Delay
from engines.server import global_vars
from mathlib import Vector
from filters.players import PlayerIter

# Source.Python Globals
mapname = global_vars.map_name

# Timer imports
from ..events import round_events

# Timer globals
running = {}

def startloop():
	global running
	vec = round_events.startbox
	for x in PlayerIter():
		steamid = x.steamid
		origin = x.origin
		if Vector.is_within_box(Vector(origin[0],origin[1],origin[2]),Vector(vec[0][0], vec[0][1], vec[0][2]), Vector(vec[1][0], vec[1][1], vec[1][2])):
			if steamid not in running:
				running[steamid] = {}
				running[steamid]['running'] = 1
	Delay(0.01, startloop)