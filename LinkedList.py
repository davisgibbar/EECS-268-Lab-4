from Node import node

class Linked_List:

    def __init__(self):
        self._front = None
        self._length = 0

    def length(self):
        return self._length

    def insert(self, index, entry):
        if index == 0:
            new_node = node(entry)
            new_node.next = self._front
            self._front = new_node
            self._length += 1
        elif index > 0 and index <= self._length:
            new_node = node(entry)
            before = self._front
            for i in range(index-1):
                before = before.next
            after = before.next
            before.next = new_node
            new_node.next = after
            self._length += 1
        else:
            raise RuntimeError("Index does not exist")


    def remove(self, index):
        if index == 0 and self._length >=1:
            temp = self._front.entry
            self._front = self._front.next
            self._length -= 1
            return temp
        elif index < self._length and index > 0:
            before = self._front
            for i in range(index-1):
                before = before.next
            target = before.next
            after = target.next
            before.next = after
            self._length -=1
            return target.entry
        else:
            raise IndexError("Index does not exist")

    def get_entry(self, index):
        if 0 <= index < self._length:
            x = 0
            temp_jumper = self._front
            while x < index:
                temp_jumper = temp_jumper.next
                x += 1
            return temp_jumper.entry
        else:
            raise RuntimeError("No entries")

    def set_entry(self, index, entry):
        if 0 <= index and index < self._length:
            x = 0
            temp_jumper = self._front
            while x < index:
                temp_jumper = temp_jumper.next
                x += 1
            temp_jumper.entry = entry


    def clear(self):
        self._front = None
        self._length = 0