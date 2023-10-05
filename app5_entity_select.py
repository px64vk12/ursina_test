from ursina import *
app = Ursina()
EditorCamera() # rotote key = right


# model
class Cube(Entity):
    def __init__(self, scale=(1, 1, 1), position=(0, 0, 0), rotation=(0, 0, 0)):
        super().__init__(
            parent=scene,
            model="cube",
            texture='white_cube',
            scale=scale,
            position=position,
            rotation=rotation,
            collider='box',
            double_sided=True,
            action=None)


floor = []
for i in range(20):
    for j in range(20):
        floor.append(Cube(
            scale=(1, 1, 1),
            position=(-10+i, 0, -10+j),
        ))

def action (): print("pressed")
myCube = Entity(
    model="cube",
    texture='white_cube',
    collider='box',
    scale=(2,2,2),
    position=(0,3,0), 
    on_click=action
)

# control
def control(): pass


# update
def update():  # timer update
    control()
    #print(mouse.hovered_entity)
    print(myCube.hovered)


if __name__ == "__main__":
    app.run()
