from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import TextureStage
import panda3d

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        if 0:
            # Load the environment model.
            self.scene = self.loader.loadModel("models/environment")
            # Reparent the model to render.
            self.scene.reparentTo(self.render)
            # Apply scale and position transforms on the model.
            self.scene.setScale(0.25, 0.25, 0.25)
            self.scene.setPos(-8, 42, 0)


        # Load and transform the panda actor.
        self.girl = self.loader.loadModel("Girl/girl.fbx")
        
        body = self.loader.loadTexture("Girl/body.png")
        cloth = self.loader.loadTexture("Girl/clothes.png")
        face = self.loader.loadTexture("Girl/face.png")
        hair1 = self.loader.loadTexture("Girl/hair.back.png")
        hair2 = self.loader.loadTexture("Girl/hair.front.png")
        self.girl.find('**/obj1').setTexture(body, 1)
        self.girl.find('**/obj1.001').setTexture(face, 1)
        self.girl.find('**/obj1.002').setTexture(cloth, 1)
        self.girl.find('**/obj1.003').setTexture(hair2, 1)
        self.girl.find('**/obj1.004').setTexture(hair1, 1)
        self.girl.setScale(0.016, 0.016, 0.016)
        self.girl.setHpr(0,90,90)
        self.girl.reparentTo(self.render)
        
        


app = MyApp()
app.run()