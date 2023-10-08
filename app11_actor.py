from ursina import *
from direct.actor.Actor import Actor

app = Ursina()
EditorCamera() # rotote key = right

entity = Entity(scale=1)
#actor = Actor("dino/scene.gltf")
actor = Actor("assets/dino/scene.gltf")
actor.reparentTo(entity)
print(actor.ls())
#actor.play("Armature|RiseUp")


for i in actor.getJoints():
    joint = actor.exposeJoint(None, 'modelRoot', i.getName())
    b = load_model('cube')
    b = Entity(model='cube', scale = (1,0.01,0.01))
    b.reparentTo(joint)
 
 
def control(): pass


# update
def update():  # timer update
    control()


if __name__ == "__main__":
    app.run()
