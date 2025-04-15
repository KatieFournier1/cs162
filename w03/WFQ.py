# Katie Fournier
# CS 162 Spring 2025
# Week 03
# WFQ


class Queue:
    def __init__(self, letter, weight):
        self.letter = letter
        self.weight = weight
        self.queue = []

    def pop(self, i = 0):
        return self.queue.pop(i)

    def append(self, other):
        self.queue.append(other)

    def __iadd__(self, other):
        self.append(other)

    def __len__(self):
        return len(self.queue)


def __main__():

    queues = [Queue('p', 3), Queue('s', 2), Queue('e', 1)]

    # Populate the weighted Queues from a file
    for line in open('input queue-1.txt'):
        for q in queues:
            if q.letter == line[0].lower():
                q += line[2:].strip()
                break


    # Pop items from the queues
    # Stop when all the queues are empty
    popped = 0
    while popped > 0:
        popped = 0
        for q in queues:
            # Weight determines how many items to pop consecutively
            for _ in range(min(q.weight, len(q))):
                print(q.pop(0))
                popped += 1

