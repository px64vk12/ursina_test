from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False)
window.size = (800, 600)


# model
from ursina.shaders import lit_with_shadows_shader # you have to apply this shader to enties for them to receive shadows.
Entity(model='plane', scale=10, color=color.black, shader=lit_with_shadows_shader)
Entity(model='cube', color=color.gray, y=1, shader=lit_with_shadows_shader)

#DirectionalLight(parent=Entity(), y=2, z=2, shadows=True)
pl = PointLight(parent=Entity(), y=2, z=2, shadows=True)
#al = AmbientLight(parent=Entity(), y=1, z=2, shadows=True)  # spotlight와 같이 쓰면 좋다.
#sl = SpotLight(parent=Entity(), position=(0,1,2),  color = (1,1,1,0.1), shadows=True)


# control
EditorCamera()
def control(): 
    if held_keys['a']: pl.disable()

# update
def update():  # timer update
    control()

if __name__ == "__main__":
    app.run()
