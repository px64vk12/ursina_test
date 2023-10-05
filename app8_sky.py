from ursina import *

app = Ursina()
Sky(texture='sky_sunset')
camera.fov = 90
EditorCamera()
app.run()
