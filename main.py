import my_utilities
import my_init_fields
import my_automated_fields

# AUTOMATED PARAMETERS
WORLD_SIZE = my_utilities.clear_and_get_world_size()
WORLD_NUMBER_OF_TILES = WORLD_SIZE * WORLD_SIZE

# RUN
if __name__ == "__main__":
	# my_init_fields.init_field_with_grass(WORLD_SIZE)
	# my_automated_fields.automated_field_with_grass(WORLD_SIZE)
	# my_init_fields.init_field_with_bush(WORLD_SIZE)
	# my_automated_fields.automated_field_with_bush(WORLD_SIZE)
	# my_init_fields.init_field_with_carrot(WORLD_SIZE)
	# my_automated_fields.automated_field_with_carrot(WORLD_SIZE)
	# my_init_fields.init_field_with_bush_and_tree(WORLD_SIZE)
	# my_automated_fields.automated_field_with_bush_and_tree(WORLD_SIZE)
	my_init_fields.init_field_with_pumpkin(WORLD_SIZE)
	my_automated_fields.automated_field_with_pumpkin(WORLD_SIZE, WORLD_NUMBER_OF_TILES)
