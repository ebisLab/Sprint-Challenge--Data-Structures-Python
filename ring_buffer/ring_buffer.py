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
        self.size = 0

    def append(self, item):
        pass

    def get(self):
        pass
