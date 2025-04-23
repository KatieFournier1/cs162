# Katie Fournier
# CS 162 Spring 2025
# Week 03
# Arrays

# Git repository: https://github.com/KatieFournier1/cs162/tree/main/week03-arrays-queues
# (I made the Git repos from previous weeks specific for those weeks, not
# knowing we were going to reuse them later. I've invited you as a collaborator.)


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
