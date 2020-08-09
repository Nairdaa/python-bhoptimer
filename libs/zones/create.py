# Source.Python imports
from players.entity import Player
from commands.typed import TypedSayCommand, CommandReturn
from menus import SimpleMenu, SimpleOption
from engines.server import global_vars

# Source.Python Globals
mapname = global_vars.map_name

# Timer imports
from ..sqlite.connection import fetchone, execute, quickSelect, save

@TypedSayCommand('!timer')
def timer_command(command_info, *args):
	player = Player(command_info.index)
	timer_menu = SimpleMenu()
	timer_menu.append('Timer Menu')
	timer_menu.append(SimpleOption(choice_index=1, text='Set Start 1', value=1, highlight=True, selectable=True))
	timer_menu.append(SimpleOption(choice_index=2, text='Set Start 2', value=2, highlight=True, selectable=True))
	timer_menu.append(SimpleOption(choice_index=3, text='Set End 1', value=3, highlight=True, selectable=True))
	timer_menu.append(SimpleOption(choice_index=4, text='Set End 2', value=4, highlight=True, selectable=True))
	timer_menu.append(' ')
	timer_menu.append(SimpleOption(choice_index=5, text='Save database', value=5, highlight=True, selectable=True))
	timer_menu.append(' ')
	timer_menu.append('0. Close')
	timer_menu.send(player)
	@timer_menu.register_select_callback
	def _timer_menu(menu, index, option):
		origin = player.origin
		if option.value == 1:
			execute('''UPDATE startzone SET start1_x=?, start1_y=?, start1_z=? WHERE mapname=?''', (origin[0], origin[1], origin[2], mapname))
			timer_menu.send(player)
		if option.value == 2:
			execute('''UPDATE startzone SET start2_x=?, start2_y=?, start2_z=? WHERE mapname=?''', (origin[0], origin[1], origin[2], mapname))
			timer_menu.send(player)
		if option.value == 3:
			execute('''UPDATE endzone SET end1_x=?, end1_y=?, end1_z=? WHERE mapname=?''', (origin[0], origin[1], origin[2], mapname))
			timer_menu.send(player)
		if option.value == 4:
			execute('''UPDATE endzone SET end2_x=?, end2_y=?, end2_z=? WHERE mapname=?''', (origin[0], origin[1], origin[2], mapname))
			timer_menu.send(player)
		if option.value == 5:
			save()

			
	
"""
@TypedSayCommand('timer')
def timer_command(command_info, *args):
    player = Player(command_info.index)
    model_menu = SimpleMenu()
    model_menu.append('Timer Menu')
    model_menu.append(SimpleOption(choice_index=1, text='Set Start 1', value=1, highlight=True, selectable=True))
    model_menu.append(SimpleOption(choice_index=2, text='Set Start 2', value=2, highlight=True, selectable=True))
    model_menu.append(' ')
    model_menu.append('0. Close')
    model_menu.send(player)

    @model_menu.register_select_callback
    def on_model_menu(menu, index, option):
        if option.value == 1:
            model_menu_list = SimpleMenu()
            model_menu_list.append('test menu 1 heH')
            model_menu_list.append(' ')
            model_menu_list.append(SimpleOption(choice_index=8, text='Back', value=8, highlight=True, selectable=True))
            model_menu_list.append('0. Close')
            model_menu_list.send(player)
            @model_menu_list.register_select_callback
            def on_model_menu_list(menu, index, option):
                if option.value == 1:
                    model_menu.append('Test 1')
"""