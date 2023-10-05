from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import panda3d
from ursina.shaders import lit_with_shadows_shader # you have to apply this shader to enties for them to receive shadows.
app = Ursina(borderless=False)
window.size = (800, 600)

import numpy as np 



# model
        
class Girl(Entity):
    def __init__(self, scale=(1,1,1), position=(0,0,0), rotation=(0,0,0)):
        super().__init__(
            parent = scene,
            scale=scale,
            position=position,
            rotation=(0, 0, 0),
            model = "assets/Girl/girl.fbx",
            collider='box',
            double_sided = True,
            shader=lit_with_shadows_shader)
        print(self.ls())
        
girlPos = np.array([-3,0.01, 0])
girl = Girl(position = girlPos)
   
Entity(model='plane', scale=10, color=color.black, shader=lit_with_shadows_shader)
Entity(model='cube', color=color.gray, y=1, shader=lit_with_shadows_shader)
   
al = AmbientLight(parent=Entity(), position=(0,1,2), shadows=True)  
sl = SpotLight(parent=Entity(), position=(0,1,2),  color = (1,1,1,0.1), shadows=True)



# control
EditorCamera() # rotote key = right
def control(): 
    if held_keys['a']: girlPos[0] += 0.1
    if held_keys['d']: girlPos[0] -= 0.1
    if held_keys['w']: girlPos[2] += 0.1
    if held_keys['s']: girlPos[2] -= 0.1
    girl.position = girlPos




# update
def update():  # timer update
    control()


if __name__ == "__main__":
    app.run()
