# Source.Python imports
from effects import box
from filters.recipients import RecipientFilter
from engines.precache import Model
from listeners.tick import Delay
from mathlib import Vector

# Source.Python Globals
model = Model('sprites/laser.vmt')

# Timer imports
from ..events import round_events

def draw_start():
	vec = round_events.startbox
	vec_x1 = vec[0][0]
	vec_y1 = vec[0][1]
	vec_z1 = vec[0][2]
	vec_x2 = vec[1][0]
	vec_y2 = vec[1][1]
	vec_z2 = vec[1][2]
	box(
		RecipientFilter(),
		Vector(vec_x1, vec_y1, vec_z1),
		Vector(vec_x2, vec_y2, vec_z2+50),
		alpha=255,
		blue=0,
		green=255,
		red=0,
		amplitude=0,
		end_width=1,
		life_time=1,
		start_width=1,
		fade_length=0,
		flags=0,
		frame_rate=255,
		halo=model,
		model=model,
		start_frame=0
	)
	Delay(0.1, draw_start)

def draw_end():
	vec = round_events.endbox
	vec_x1 = vec[0][0]
	vec_y1 = vec[0][1]
	vec_z1 = vec[0][2]
	vec_x2 = vec[1][0]
	vec_y2 = vec[1][1]
	vec_z2 = vec[1][2]
	box(
		RecipientFilter(),
		Vector(vec_x1, vec_y1, vec_z1),
		Vector(vec_x2, vec_y2, vec_z2+50),
		alpha=255,
		blue=0,
		green=0,
		red=255,
		amplitude=0,
		end_width=1,
		life_time=1,
		start_width=1,
		fade_length=0,
		flags=0,
		frame_rate=255,
		halo=model,
		model=model,
		start_frame=0
	)
	Delay(0.1, draw_end)
