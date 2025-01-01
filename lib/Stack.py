class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return_item = self.items[len(self.items) - 1]
        self.items.pop(len(self.items) - 1)
        return return_item

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            return len(self.items) - (self.items.index(target) + 1)
        except ValueError:
            return -1
        except:
            return None