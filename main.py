# CLEAR AND INIT WORLD
def clear_and_get_world_size():
	clear()
	WORLD_SIZE = get_world_size()
	return WORLD_SIZE

# AUTOMATED PARAMETERS
WORLD_SIZE = clear_and_get_world_size()

# GRASS MODE
def grass_mode():
	while True:
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if can_harvest():
					harvest()
				move(North)
			move(East)

# # BUSH MODE
# def init_field_with_bush():
# 	for i in range(WORLD_SIZE):
# 			for j in range(WORLD_SIZE):
# 				plant(Entities.Bush)
# 				move(North)
# 			move(East)

# def automated_field_with_bush():
# 	while True:
# 		for i in range(WORLD_SIZE):
# 			for j in range(WORLD_SIZE):
# 				if can_harvest():
# 					harvest()
# 					plant(Entities.Bush)
# 					move(North)
# 				move(East)

# CARROT MODE
# def init_field_with_carrot():
# 	for i in range(WORLD_SIZE):
# 			for j in range(WORLD_SIZE):
# 				till()
# 				plant(Entities.Carrot)
# 				move(North)
# 			move(East)

# def automated_field_with_carrot():
# 	while True:
# 		for i in range(WORLD_SIZE):
# 			for j in range(WORLD_SIZE):
# 				if can_harvest():
# 					harvest()
# 					plant(Entities.Carrot)
# 					move(North)
# 				move(East)

# RUN
if __name__ == "__main__":
	clear_and_get_world_size()
	grass_mode()
	# init_field_with_bush()
	# automated_field_with_bush()
	# init_field_with_carrot()
	# automated_field_with_carrot()