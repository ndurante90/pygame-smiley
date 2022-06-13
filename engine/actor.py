class Actor:
    def __init__(self):
        self.components = []

    def load(self):
        for a in self.components:
            a.load()
    
    def update(self):
        for a in self.components:
            a.update()

    def render(self, window):
        for a in self.components:
           a.render(window)
