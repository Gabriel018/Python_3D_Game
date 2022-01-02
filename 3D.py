from self import self
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

def main():
        Sky()
        sky = Entity(model='sky_dome',color = color.rgb(54,54,54),scale =(100,100,100) )
        ground = Entity(
                        model='plane',
                        texture='grass',
                        color = color.brown,
                        collider='mesh',
                        texture_scale = (5,5),
                        scale=(100, 0, 100))

        wall  =Entity(model='cube',
                      texture='brick',
                      position= (10,0,10),
                      color = color.gray,
                      texture_scale = (5,5),
                      scale=(1,10,10))

        gun = Entity(model='cube', parent=camera.ui, texture='img/Gun.png', scale=0.4, position=(.0,-.3))

        player = FirstPersonController()

def input(key):
    gun_flah = Entity(model='quad',
                      texture='img/gun_animat',
                      parent=camera.ui,
                      fps=4, scale=0.2,
                      loop=False,
                      position=(.0, -.07))
    invoke(setattr, gun_flah, 'visible', False, delay=.4)
    gun_flah.visible = False
    if key == 'left mouse down':
        Audio('sound/shot.wav')
        gun_flah.visible = True
    else:
        gun_flah.visible = False



if __name__ == '__main__':
    main()
app.run()