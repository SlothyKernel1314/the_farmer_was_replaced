import my_utilities
import my_init_fields
import my_automated_fields

# AUTOMATED PARAMETERS
WORLD_SIZE = my_utilities.clear_and_get_world_size()
WORLD_NUMBER_OF_TILES = WORLD_SIZE * WORLD_SIZE

# MANUAL PARAMETERS
FIELD_MODE = {
    'GRASS_SPAMMING_MODE': False,
	'BUSH_SPAMMING_MODE': False,
    'CARROT_SPAMMING_MODE': False,
	'BUSH_TREE_SPAMMING_MODE': True,
	'PUMPKIN_SPAMMING_MODE': False,
	'SUNFLOWER_BASIC_SPAMMING_MODE': False,
	'CACTUS_BASIC_SPAMMING_MODE': False,
	'CACTUS_ADVANCED_SPAMMING_MODE': False
}

# RUN
if __name__ == "__main__":
	if FIELD_MODE['GRASS_SPAMMING_MODE'] == True:
		my_init_fields.init_field_with_grass(WORLD_SIZE)
		my_automated_fields.automated_field_with_grass(WORLD_SIZE)
	if FIELD_MODE['BUSH_SPAMMING_MODE'] == True:
		my_init_fields.init_field_with_bush(WORLD_SIZE)
		my_automated_fields.automated_field_with_bush(WORLD_SIZE)
	if FIELD_MODE['BUSH_TREE_SPAMMING_MODE'] == True:
		my_init_fields.init_field_with_bush_and_tree(WORLD_SIZE)
		my_automated_fields.automated_field_with_bush_and_tree(WORLD_SIZE)
	if FIELD_MODE['CARROT_SPAMMING_MODE'] == True:
		my_init_fields.init_field_with_carrot(WORLD_SIZE)
		my_automated_fields.automated_field_with_carrot(WORLD_SIZE)
	if FIELD_MODE['PUMPKIN_SPAMMING_MODE'] == True:
		my_init_fields.init_field_with_pumpkin(WORLD_SIZE)
		my_automated_fields.automated_field_with_pumpkin(WORLD_SIZE, WORLD_NUMBER_OF_TILES)
	if FIELD_MODE['SUNFLOWER_BASIC_SPAMMING_MODE'] == True:
		my_init_fields.init_field_with_sunflower(WORLD_SIZE)
		my_automated_fields.automated_field_with_sunflower_basic(WORLD_SIZE)
	if FIELD_MODE['CACTUS_BASIC_SPAMMING_MODE'] == True:
		my_init_fields.init_field_with_cactus(WORLD_SIZE)
		my_automated_fields.automated_field_with_cactus_basic(WORLD_SIZE)
	if FIELD_MODE['CACTUS_ADVANCED_SPAMMING_MODE'] == True:
		my_init_fields.init_field_with_cactus(WORLD_SIZE)
		my_automated_fields.automated_field_with_cactus_advanced(WORLD_SIZE)

# TODO :
# Fertilizer
# Complex Sunflower Management : implement sunflower rules and constraints 
# (but is it really cost-effective on large fields?)
# Optimized movement: serpentine movement (?)
# Optimised cactus buuble sort : variance calculation for processing the highest rows and columns.., 
# ... memory for rows and columns already processed so that they do not need to be processed again