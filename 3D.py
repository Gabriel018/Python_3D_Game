from self import self
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


player = FirstPersonController(position=(10,0,0))

gun=Entity(model='cube', parent=camera.ui, texture='img/Gun.png', scale=0.5, position=(.0, -.3))
                    # Carrega,cenario do jogo
Sky()
sky = Entity(model='sky_dome',color = color.rgb(54,54,54),scale =(100,100,100) )

ground = Entity(
                    model='plane',
                    texture='grass',
                    color = color.brown,
                    collider='mesh',
                    texture_scale = (5,5),
                    scale=(100, 0, 100))

wall1  =Entity(model='cube',
                   texture='brick',
                   position= (0,5,50),
                   color = color.gray,
                   collider='box',
                   texture_scale = (3,3),
                   scale=(100,10,1))
wall2 = duplicate(wall1,z=-50)
wall3 = duplicate(wall1,rotation_y=90,x=-50,z=0)
wall14 = duplicate(wall3,x=50)



enemy = Entity(model='quad', position=(5, 3, 5),
                   texture="img/monster.png",
                   collider='box',
                   scale=5)

gun_flah = Entity(model='quad',
                             texture='img/gun_animat',
                             parent=camera.ui,
                             fps=4, scale=0.2,
                             loop=False,
                             position=(.0, -.0))
invoke(setattr,gun_flah, 'visible', False, delay=.4)
gun_flah.visible = False


def input(key):

        if key == 'left mouse down':
            Audio('sound/shot.wav')
            if enemy.hovered:
                destroy(enemy)
            gun.position=(.0, -.28)
            gun_flah.visible = True
        else:
            gun_flah.visible = False
            gun.position = (.0, -.3)



app.run()