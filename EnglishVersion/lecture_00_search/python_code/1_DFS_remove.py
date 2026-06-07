def remove(self):
    if self.empty():
        raise Exception("Stack is empty")
    else:
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node