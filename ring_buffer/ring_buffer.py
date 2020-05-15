class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return f"{self.value}"


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring_buffer = None
        self.size = 0

    def append(self, item):
        if self.size < self.capacity:
            if self.ring_buffer:
                self.size += 1  # increment
                self.ring_buffer.set_next(Node(item))
                self.ring_buffer = self.ring_buffer.next
            else:
                self.ring_buffer = Node(item)
                self.end = self.ring_buffer
        else:
            self.ring_buffer.next_node.set_next(item)
            self.ring_buffer = self.ring_buffer.next_node

    def get(self):
        arr = []
        for i in range(self.size):
            # push to arr
            arr.append(self.end.get_value())
            self.new_tail = self.new_tail.next
        return arr
