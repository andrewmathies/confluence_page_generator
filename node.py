class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.id = None
        self.content = None
        self.parent = None

    def __str__(self):
        return self.name