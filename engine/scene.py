class Scene:
    def __init__(self):
        self.actors = []

    def load(self):
        for a in self.actors:
            a.load()

    def update(self):
        for a in self.actors:
            a.update()

    def render(self, window):
        for a in self.actors:
           a.render(window)
    
    