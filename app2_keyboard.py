from ursina import *
app = Ursina()


# model
class Cube(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "cube",
            texture='white_cube',
            scale=(2, 2, 2),
            position=(0, 0, 0),
            rotation=(0, 0, 0),
            double_sided = True
        )
cube = Cube()


# control update
def control():
    cubePos = cube.get_position()
    if held_keys['a']: print(cubePos)
    print(held_keys['a'], held_keys['d'], held_keys['w'], held_keys['s'])


# frame update
def update():  # timer update
    control()
    cube.rotation_x += 0.25
    cube.rotation_y += 0.5


if __name__ == "__main__":
    app.run()
