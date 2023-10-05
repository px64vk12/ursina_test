from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()


# model
class Cube(Entity):
    def __init__(self, scale=(1,1,1), position=(0,0,0), rotation=(0,0,0)):
        super().__init__(
            parent = scene,
            model = "cube",
            texture='white_cube',
            scale=scale,
            position=position,
            rotation=rotation,
            collider='box',
            double_sided = True)
        
floor = []
for i in range(20):
    for j in range(20):
        floor.append(Cube(
            scale = (1,1,1),
            position = (-10+i, 0, -10+j),
        ))


# control
player = FirstPersonController(
    position=(0, 1, 0), 
    rotation=(0, 0, 0), enabled=True)
def control(): pass


# update
def update():  # timer update
    if player.y < -20: 
        player.set_position((0,0,0))
    control()


if __name__ == "__main__":
    app.run()
