import my_utilities

def init_field_with_grass(WORLD_SIZE):
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			my_utilities.watering_field()
			move(North)
		move(East)
		
def init_field_with_bush(WORLD_SIZE):
	for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				plant(Entities.Bush)
				my_utilities.watering_field()
				move(North)
			move(East)
			
def init_field_with_carrot(WORLD_SIZE):
	for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				till()
				plant(Entities.Carrot)
				my_utilities.watering_field()
				move(North)
			move(East)
			
def init_field_with_bush_and_tree(WORLD_SIZE):
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			my_utilities.plant_bush_or_tree_alternate(i, j)
			my_utilities.watering_field()
			move(North)
		move(East)
		
def init_field_with_pumpkin(WORLD_SIZE):
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			till()
			plant(Entities.Pumpkin)
			my_utilities.watering_field()
			move(North)
		move(East)
		
def init_field_with_sunflower(WORLD_SIZE):
	for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				till()
				plant(Entities.Sunflower)
				my_utilities.watering_field()
				move(North)
			move(East)

def init_field_with_cactus(WORLD_SIZE):
	for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				till()
				plant(Entities.Cactus)
				my_utilities.watering_field()
				move(North)
			move(East)