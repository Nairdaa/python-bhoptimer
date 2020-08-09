# Source.Python imports
from events import Event
from engines.server import global_vars
from mathlib import Vector

# Source.Python Globals
mapname = global_vars.map_name

# Timer imports
from ..sqlite.connection import fetchone, execute, save, fetchall
from .. zones import draw
from ..loops import startzone
from ..loops import endzone

startbox = []
endbox = []

@Event('round_start')
def _round_start(event):
	global startbox
	global endbox

	# Let's check if current map exists in the database.
	execute('''SELECT mapname FROM maplist WHERE mapname=?''', (mapname,))
	result = fetchone()

	# If not, let's write it into the table.
	if not result:
		execute('''INSERT INTO maplist VALUES(?, ?)''', (mapname, 1))
		execute('''INSERT INTO startzone VALUES(?, ?, ?, ?, ?, ?, ?)''', (mapname, 0, 0, 0, 0, 0, 0))
		execute('''INSERT INTO endzone VALUES(?, ?, ?, ?, ?, ?, ?)''', (mapname, 0, 0, 0, 0, 0, 0))
		save()

	# Lets check if the map is set up with zones.
	if result:
		execute('''SELECT start1_x, start1_y, start1_z, start2_x, start2_y, start2_z FROM startzone WHERE mapname=?''', (mapname,))
		start_list = fetchone()
		x1 = start_list[0]
		y1 = start_list[1]
		z1 = start_list[2]
		x2 = start_list[3]
		y2 = start_list[4]
		z2 = start_list[5]
		start_p1 = (x1,y1,z1)
		start_p2 = (x2,y2,z2)
		startbox = (start_p1, start_p2)
		draw.draw_start()
		startzone.startloop()
		
		execute('''SELECT end1_x, end1_y, end1_z, end2_x, end2_y, end2_z FROM endzone WHERE mapname=?''', (mapname,))
		end_list = fetchone()
		x1 = end_list[0]
		y1 = end_list[1]
		z1 = end_list[2]
		x2 = end_list[3]
		y2 = end_list[4]
		z2 = end_list[5]
		end_p1 = (x1,y1,z1)
		end_p2 = (x2,y2,z2)
		endbox = (end_p1, end_p2)
		draw.draw_end()
		endzone.endloop()