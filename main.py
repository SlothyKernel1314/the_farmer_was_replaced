# TODO :
# Watering Tanks

# CLEAR AND INIT WORLD
def clear_and_get_world_size():
	clear()
	WORLD_SIZE = get_world_size()
	return WORLD_SIZE

# AUTOMATED PARAMETERS
WORLD_SIZE = clear_and_get_world_size()

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

# GRASS MODE
def init_field_with_grass(WORLD_SIZE):
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			watering_field()
			move(North)
		move(East)

def automated_field_with_grass(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					watering_field()
				move(North)
			move(East)

# BUSH MODE
def init_field_with_bush(WORLD_SIZE):
	for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				plant(Entities.Bush)
				watering_field()
				move(North)
			move(East)

def automated_field_with_bush(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					plant(Entities.Bush)
					watering_field()
				move(North)
			move(East)

# CARROT MODE
def init_field_with_carrot(WORLD_SIZE):
	for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				till()
				plant(Entities.Carrot)
				watering_field()
				move(North)
			move(East)

def automated_field_with_carrot(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					plant(Entities.Carrot)
					watering_field()
				move(North)
			move(East)

# TREE MODE
def init_field_with_bush_and_tree(WORLD_SIZE):
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			plant_bush_or_tree_alternate(i, j)
			watering_field()
			move(North)
		move(East)

def automated_field_with_bush_and_tree(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					plant_bush_or_tree_alternate(i, j)
					watering_field()
				move(North)
			move(East)

# PUMPKIN MODE
def init_field_with_pumpkin(WORLD_SIZE):
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			till()
			plant(Entities.Pumpkin)
			watering_field()
			move(North)
		move(East)

def automated_field_with_pumpkin(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					# Retarde l'exécution afin d'augm.
					# la proba. d'avoir un + gros pump.
					harvest()
					plant(Entities.Pumpkin)
					watering_field()
				else:
					# Retarde l'exécution afin d'augm.
					# la proba. d'avoir un + gros pump.
					plant(Entities.Pumpkin)
					watering_field()
				move(North)
			move(East) 

# RUN
if __name__ == "__main__":
	# init_field_with_grass(WORLD_SIZE)
	# automated_field_with_grass(WORLD_SIZE)
	# init_field_with_bush(WORLD_SIZE)
	# automated_field_with_bush(WORLD_SIZE)
	# init_field_with_carrot(WORLD_SIZE)
	# automated_field_with_carrot(WORLD_SIZE)
	# init_field_with_bush_and_tree(WORLD_SIZE)
	# automated_field_with_bush_and_tree(WORLD_SIZE)
	init_field_with_pumpkin(WORLD_SIZE)
	automated_field_with_pumpkin(WORLD_SIZE)
