from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import panda3d
app = Ursina(borderless=False)
window.size = (800, 600)




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
        
class Girl(Entity):
    def __init__(self, scale=(1,1,1), position=(0,0,0), rotation=(0,0,0)):
        super().__init__(
            parent = scene,
            scale=(0.002,0.002,0.002),
            position=(-3, 0.01, 0),
            rotation=(0, 0, 0),
            model = "Girl/girl.fbx",
            collider='box',
            double_sided = True)

        self.body = loader.loadTexture("Girl/body.png")
        self.cloth = loader.loadTexture("Girl/clothes.png")
        self.face = loader.loadTexture("Girl/face.png")
        self.hair1 = loader.loadTexture("Girl/hair.back.png")
        self.hair2 = loader.loadTexture("Girl/hair.front.png")
        self.find('**/obj1').setTexture(self.body)
        self.find('**/obj1.001').setTexture(self.face, 1)
        self.find('**/obj1.002').setTexture(self.cloth, 1)
        self.find('**/obj1.003').setTexture(self.hair1, 1)
        self.find('**/obj1.004').setTexture(self.hair2, 1)
     
girl = Girl()
   
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
    rotation=(0, 0, 0), 
enabled=True)
def control(): pass


# update
def update():  # timer update
    if player.y < -20: 
        player.set_position((0,0,0))
    control()


if __name__ == "__main__":
    app.run()
