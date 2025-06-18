# CLEAR WORLD
clear()

# GRASS MODE
# while True:
# 	if can_harvest():
# 		harvest()
# 		move(North)

# BUSH MODE
# Init Field with Bush
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
# Harvest Bush
while True:
	if can_harvest():
		harvest()
		plant(Entities.Bush)
		move(North)
