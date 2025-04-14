# Katie Fournier
# CS 162 Spring 2025
# Week 03
# Arrays

import numpy as np

array_size = 5
array = np.random.randint(9, size=[array_size, array_size], dtype=int)
outputs = [array,
           array[1][2],
           np.sum(array),
           np.mean(array, axis=1),
           np.max(array, axis=1)]
for line in outputs:
    print(line)
