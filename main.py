import my_utilities

# AUTOMATED PARAMETERS
WORLD_SIZE = my_utilities.clear_and_get_world_size()
WORLD_NUMBER_OF_TILES = WORLD_SIZE * WORLD_SIZE

# GRASS MODE
def init_field_with_grass(WORLD_SIZE):
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			my_utilities.watering_field()
			move(North)
		move(East)

def automated_field_with_grass(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					my_utilities.watering_field()
				move(North)
			move(East)

# BUSH MODE
def init_field_with_bush(WORLD_SIZE):
	for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				plant(Entities.Bush)
				my_utilities.watering_field()
				move(North)
			move(East)

def automated_field_with_bush(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					plant(Entities.Bush)
					my_utilities.watering_field()
				move(North)
			move(East)

# CARROT MODE
def init_field_with_carrot(WORLD_SIZE):
	for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				till()
				plant(Entities.Carrot)
				my_utilities.watering_field()
				move(North)
			move(East)

def automated_field_with_carrot(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					plant(Entities.Carrot)
					my_utilities.watering_field()
				move(North)
			move(East)

# TREE MODE
def init_field_with_bush_and_tree(WORLD_SIZE):
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			my_utilities.plant_bush_or_tree_alternate(i, j)
			my_utilities.watering_field()
			move(North)
		move(East)

def automated_field_with_bush_and_tree(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					my_utilities.plant_bush_or_tree_alternate(i, j)
					my_utilities.watering_field()
				move(North)
			move(East)

# PUMPKIN MODE
def init_field_with_pumpkin(WORLD_SIZE):
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			till()
			plant(Entities.Pumpkin)
			my_utilities.watering_field()
			move(North)
		move(East)

def automated_field_with_pumpkin(WORLD_SIZE):
	# This function encourages pumpkins to merge 
	# and is optimized to replace pumpkins that die 
	# + not harvest pumpkins that have not yet reached world size.
	while True:
		occuped_tiles = 0
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					occuped_tiles += 1
				else:
					plant(Entities.Pumpkin)
					my_utilities.watering_field()
				move(North)
			move(East)
			if occuped_tiles == WORLD_NUMBER_OF_TILES:
				harvest()
				occuped_tiles = 0


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
