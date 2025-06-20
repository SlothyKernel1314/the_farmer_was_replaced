import my_utilities
import my_init_fields
import my_cactus_utilities

def automated_field_with_grass(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
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

def automated_field_with_pumpkin(WORLD_SIZE, WORLD_NUMBER_OF_TILES):
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
				
def automated_field_with_sunflower_basic(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					plant(Entities.Sunflower)
					my_utilities.watering_field()
				move(North)
			move(East)

def automated_field_with_cactus_basic(WORLD_SIZE):
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
					plant(Entities.Cactus)
					my_utilities.watering_field()
				move(North)
			move(East)

def automated_field_with_cactus_advanced(WORLD_SIZE):
	while True:
		my_cactus_utilities.sort_cactus_field(WORLD_SIZE)
		harvest()
		move(North)
		move(East)
		my_init_fields.renew_field_with_cactus(WORLD_SIZE)