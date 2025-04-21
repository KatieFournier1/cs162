# Katie Fournier
# CS 162 Spring 2025
# Week 03
# WFQ

# Git repository: https://github.com/KatieFournier1/cs162/tree/main/week03-arrays-queues
# (I made the Git repos from previous weeks specific for those weeks, not
# knowing we were going to reuse them later. I've invited you as a collaborator.)


class WFQueue:
    """A weighted fair queue. Packets in the queue have a priority, or weight,
    with packets dequeued starting at the highest weight, dequeueing a number
    of packets at that weight equal to the weight, then moving down the packet
    weights and repeating the process.

    E.g., starting at, say, a max weight of 5, 5 weight 5 packets are dequeued
    before then dequeueing 4 weight 4 packets, then 3 weight 3 packets, and
    so on. After finally dequeueing 1 weight 1 packet, the entire process is
    repeated starting back at weight 5."""

    def __init__(self):
        self.__queues = [[]]
        self.__ptr = self.Pointer()

    class Pointer:
        """Stores the current location in the weighted dequeueing order."""

        def __init__(self):
            self.wgt = 0
            self.i = 0
            self.max_wgt = 0

        def reset(self):
            self.wgt = self.max_wgt
            self.i = self.max_wgt

        def lower(self):
            if self.wgt > 1:
                self.wgt -= 1
                self.i = self.wgt
            else:
                self.reset()

        def step(self):
            if self.i > 1:
                self.i -= 1
            else:
                self.lower()


    def pop(self):
        """Removes the packet at the front of the queue and returns it."""

        errOOB = 'queue is empty'
        if len(self.__queues) == 0:
            raise OutOfBoundsError(errOOB)

        # If we haven't dequeued anything yet (ptr.wgt can only be 0 at init)
        if self.__ptr.wgt == 0:
            # Loop back to the highest priority
            self.__ptr.reset()
        # Find the highest priority non-empty queue
        while len(self.__queues[self.__ptr.wgt - 1]) == 0:
            if self.__ptr.wgt > 1:
                self.__ptr.lower()
            else:
                # If we're here all queues must be empty
                raise OutOfBoundsError(errOOB)

        # Dequeue and move the pointer
        packet = self.__queues[self.__ptr.wgt - 1].pop(0)
        self.__ptr.step()
        return packet

    def append(self, packet, weight):
        """Add a weighted packet to the end of the queue."""

        while len(self.__queues) < weight:
            self.__queues.append([])
        self.__queues[weight - 1].append(packet)
        self.__ptr.max_wgt = max(self.__ptr.max_wgt, weight)

    def __len__(self):
        total = 0
        for q in self.__queues:
            total += len(q)
        return total


def main():
    """Populate a weighted fair queue (WFQ) from a file containing packet data
    then dequeue the packets in order, with higher weighted packets dequeueing
    more often."""

    queue = WFQueue()
    # Premium, Standard, Economy
    weights = {'P': 3, 'S': 2, 'E': 1}
    # Populate the weighted Queue from a file
    for line in open('input queue-1.txt'):
        data = line[2:].strip()
        weight = weights[line[0]]
        queue.append(data, weight)

    # Pop packets from the queue until the queue is empty
    while len(queue) > 0:
        print(queue.pop())


if __name__ == '__main__':
    main()


