from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen =True
window.color=color.black

player = FirstPersonController(
  collider='box', jump_duration=0.35
)
player.cursor.visible=False

ground = Entity(
  color=color.brown,
  model='cube',
  collider='mesh',
  scale=(30,0,5)
)

pill1 = Entity(
  model='cube',
  color=color.white,
  scale=(0.4,0.1,53),
  z=28,x=-0.7
)

pill2 = duplicate(pill1, x=-3.7)
pill3 = duplicate(pill1, x=0.6)
pill4 = duplicate(pill1, x=3.6)

from random import randint

blocks = []
for i in range(12):
  block = Entity(
    model='cube',
    collider='box',
    color=color.white33,
    position=(2,0.1,3+i*4),
    scale=(3,0.1,2.5)
  )
  block2 = duplicate(block, x=-2.2)
  blocks.append(
    (block, block2, randint(0,10) > 7, randint(0,10) > 7)
  )

goal = Entity(
  color=color.brown,
  model='cube',
  z=55,
  scale=(10,1,10),
)

pillar = Entity(
  color=color.yellow,
  model='cube',
  z=58,
  scale=(1,15,1),
  y=8
)

game_over = Text(
  text='Game Over!\nPress R to restart.\nPress Q to quit.',
  scale=2,
  origin=(0, 0),
  y=0.05,
  background=True,
  background_color=color.black66,
  enabled=False
)

def update():
  for block1,block2,k,n in blocks:
    for x,y in [(block1,k), (block2,n)]:
      if x.intersects() and y:
        invoke(destroy, x, delay=0.1)
        x.fade_out(duration=0.2)

 
  if player.y < ground.y-4:
    player.enabled = False
    game_over.enabled = True

def input(key):
  if key == 'q':
    quit()
  elif key == 'r' and game_over.enabled:
    # Restart game
    player.enabled = True
    player.position = (0, 1, 0)
    game_over.enabled = False

app.run()
