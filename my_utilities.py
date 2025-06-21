# CLEAR AND INIT WORLD
def clear_and_get_world_size():
	clear()
	WORLD_SIZE = get_world_size()
	return WORLD_SIZE

# MISC UTILITIES  
def watering_field():
	if get_water() <= 0.75:
		use_item(Items.Water)
            
def goto(target_x, target_y):
	# This function moves the drone naively to (target_x, target_y)...
	# ... using only move(East) and move(North).                   
    # X axis (West-East)
    while get_pos_x() != target_x:
        # one step at right
        move(East)                             
    # Y axis (South-North)
    while get_pos_y() != target_y:
        # one step at up            
        move(North)                            
		
# PLANT UTILITIES
def plant_bush_or_tree_alternate(i, j):
	total = i + j
	if total % 2 == 0:
		plant(Entities.Bush)
	else:
		plant(Entities.Tree)