# CLEAR WORLD
clear()

# GRASS MODE
# while True:
# 	for i in range(get_world_size()):
# 		for j in range(get_world_size()):
# 			if can_harvest():
# 				harvest()
# 			move(North)
# 		move(East)

# BUSH MODE
# Init Field with Bush
for i in range(get_world_size()):
		for j in range(get_world_size()):
			plant(Entities.Bush)
			move(North)
		move(East)
# Harvest Bush
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				move(North)
			move(East)
