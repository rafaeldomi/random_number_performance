#!/usr/bin/env python3
import random

SIZE=1000000

original_array = [i for i in range(1, SIZE+1)]

def random_array():
    new_array = [None] * SIZE
    indexes_set = set()
    
    for index,value in enumerate(original_array):
        print(f"IDX: {index} = value: {value}")

        # Find a free index in the new aray
        while True:
            random_index = random.randint(0, SIZE-1)
            if random_index not in indexes_set:
                print(f" . Found index: {random_index}")
                new_array[random_index] = value
                indexes_set.add(random_index)
                break
            #else:
            #   print(f" - Already exists {random_index}")
    
    return new_array

shuffled_array = random_array()
# print(shuffled_array)