from pico2d import load_image


class Grass1:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 50)

    def update(self):
        pass

class Grass2:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 70)

    def update(self):
        pass