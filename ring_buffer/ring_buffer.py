class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

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

            # find way to override this
            else:
                self.ring_buffer = Node(item)
                self.end = self.ring_buffer
        else:
            self.ring_buffer.next.set_next(item)
            self.ring_buffer = self.ring_buffer.next

    def get(self):
        arr = []
        for i in range(self.size):
            # push to arr
            arr.append(self.end.get_value())
            self.end = self.end.next
        return arr


buffer = RingBuffer(3)

print('buffer.get -> ', buffer.get())  # get()

buffer.append('a')
buffer.append('b')
buffer.append('c')
# print(buffer.ring_buffer.value)
# print(buffer.get())
# print(buffer.ring_buffer.value)

# overriding
buffer.append('d')

print('buffer.get()--> ', buffer.get())

buffer.append('e')
buffer.append('f')

# print(buffer.get())
