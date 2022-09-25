


class stack:

    def __init__(self, name, next_stack, previous_stack = None):
        self.name = name
        self.next = next_stack
        self.previous = previous_stack
        pass