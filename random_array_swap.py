#!/usr/bin/env python3

import random

SIZE=1000000

original_array = [i for i in range(1, SIZE+1)]

def random_array_swap():
    new_array = original_array[:]
    array_size = len(new_array)
    half_size = array_size // 2

    print(f"Will loop {half_size}")

    for _ in range(half_size):
        index1 = random.randint(0, array_size - 1)
        index2 = random.randint(0, array_size - 1)

        if index1 == index2:
            continue

        new_array[index1], new_array[index2] = new_array[index2], new_array[index1]
    
    return new_array

shuffled_array = random_array_swap()