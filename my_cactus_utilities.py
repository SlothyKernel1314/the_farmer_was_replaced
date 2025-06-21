import my_utilities

def vertical_pass_for_cactus_bubble_sort(WORLD_SIZE):
    # Bubble sort in each column (South → North).
	# Returns True if there has been at least one swap.
    changed = False
    for col in range(WORLD_SIZE):
        # bottom of column (South)
        my_utilities.goto(col, 0)                           
        for row in range(WORLD_SIZE - 1):
            # compare with box above (North)
            if measure() > measure(North):
                # Swap the two cactus     
                swap(North)
                changed = True
            move(North)
    return changed


def horizontal_pass_for_cactus_bubble_sort(WORLD_SIZE):
    # Bubble sort in each column (West → East).
	# Returns True if there has been at least one swap.
    changed = False
    for row in range(WORLD_SIZE):
        # left of the row (West)
        my_utilities.goto(0, row)                           
        for col in range(WORLD_SIZE - 1):
            # compare with box right (East)
            if measure() > measure(East):
                # Swap the two cactus
                swap(East)
                changed = True
            move(East)
    return changed


def sort_cactus_field(WORLD_SIZE):
    # Put all the cactus fields in order using the “Bubble Sort” method
	# This method is far from optimal, but it's enough to harvest cacti quickly
	# This function allows harvesting by propagation on all cacti...
    # ... whatever the value of the “WORLD SIZE”...
    # ... and its complexity is correct for a “WORLD SIZE” not exceeding 10.
	# Assumes that the cacti are already mature (can_harvest() == True everywhere).
    changed = True
    while changed:
        # no exchange detected... yet !
        changed = False 
        # Did the column pass a swap?                 
        if vertical_pass_for_cactus_bubble_sort(WORLD_SIZE):
              # yes → go to the next round
              changed = True             
        # Did the row pass a swap?
        if horizontal_pass_for_cactus_bubble_sort(WORLD_SIZE):
              # yes → go to the next round
              changed = True