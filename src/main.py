import pgzrun  # required top
import random

WIDTH = 500
HEIGHT = 700
CENTER = WIDTH / 2  # center of screen x/y

'''PLAYER ACTOR'''

player = Actor('playeridle')
player.pos = midbottom=(CENTER, HEIGHT - 110)
player.speed = 7.5


''''GEM ACTOR'''
gems = []
gem_amount = 3

def gem_spawn():
    gems.append(Actor('goldgem', pos=(random.randint(0, WIDTH), 0)))

def gem_fall(gem):
    if gem.y < 620: #  HEIGHT - images.ground.get_height() - images.goldgem.get_height()/4:
        gem.y += 4

for i in range(gem_amount):  # spawn assigned number of gems
    gem_spawn()


def player_move():
    if keyboard.left and player.left > 0:  # if keyboard press left and player ???? keeps players in boundaries
        player.x -= player.speed
    elif keyboard.right and player.right < WIDTH:
        player.x += player.speed



def draw():
    screen.fill((90, 120, 200))  # RGB fill bg

    player.draw()

    for gem in gems:
        gem.draw()

    for i in range(8):  # creating range variable i 0-8
        screen.blit(images.ground, (i * images.ground.get_width(), HEIGHT - images.ground.get_height()))  # create ground tile 8(i) times

    screen.draw.text("Score: 0", midtop=(CENTER, 10), fontname="mini_square", fontsize=36)  # score center x, down 10 y
  #  screen.draw.text("Dodge the blades and grab the gems!", midbottom=(CENTER, HEIGHT - 15), fontname="mini_square", fontsize=15)  # instructions center x, height - num for bottom up y


def update():
    player_move()  # update check for player movement

    for gem in gems:
        gem_fall(gem)


pgzrun.go()  # end
