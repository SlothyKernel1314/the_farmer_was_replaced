# CLEAR AND INIT WORLD
def clear_and_get_world_size():
	clear()
	WORLD_SIZE = get_world_size()
	return WORLD_SIZE

# MISC UTILITIES  
def watering_field():
	if get_water() <= 0.75:
		use_item(Items.Water)
		
# PLANT UTILITIES
def plant_bush_or_tree_alternate(i, j):
	total = i + j
	if total % 2 == 0:
		plant(Entities.Bush)
	else:
		plant(Entities.Tree)