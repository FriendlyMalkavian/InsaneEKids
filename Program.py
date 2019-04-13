import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Vec3
from minecraftstuff import MinecraftDrawing
from minecraftstuff import MinecraftShape, ShapeBlock
from random import randint
from time import sleep

mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)

class Pyramidka:
    def __init__(self):
         self.a = [Vec3(0, 0, 0),
         Vec3(0, 0, 30),
         Vec3(15, 15, 15),]
         self.b = [Vec3(0, 0, 30),
         Vec3(30, 0, 30),
         Vec3(15, 15 , 15),]
         self.c = [Vec3(30, 0, 0),
         Vec3(30, 0, 30),
         Vec3(15, 15, 15),]
         self.d = [Vec3(0, 0, 0),
         Vec3(30, 0, 0),
         Vec3(15, 15, 15),]
    
    def draw(self):
        mcDrawing.drawFace(self.a, True, block.IRON_BLOCK)
        mcDrawing.drawFace(self.b, True, block.IRON_BLOCK)
        mcDrawing.drawFace(self.c, True, block.IRON_BLOCK)
        mcDrawing.drawFace(self.d, True, block.IRON_BLOCK)
    
    def scale(self,scale):
        for v in self.a:
            v.x = v.x * scale
            v.y = v.y * scale
            v.z = v.z * scale
            for v in self.b:
                v.x = v.x * scale
                v.y = v.y * scale
                v.z = v.z * scale
            for v in self.c:
                 v.x = v.x * scale
                 v.y = v.y * scale
                 v.z = v.z * scale
            for v in self.d:
                 v.x = v.x * scale
                 v.y = v.y * scale
                 v.z = v.z * scale

LENGTH = 100
def draw_flat():
    for x in range(LENGTH):
        for z in range(LENGTH):
             mc.setBlock(x, 0, z, block.GRASS)
             
def draw_bedrock():
    for x in range(LENGTH):
        for z in range(LENGTH):
             mc.setBlock(x, -1, z, block.BEDROCK)

def draw_lava(count):
    for c in range(count):
        r_x = randint(0,LENGTH-1)
        r_z = randint(0,LENGTH-1)
        mc.setBlock(r_x, 0, r_z, block.LAVA )
        

        
class Wall:
    def __init__(self):
        mc.setBlocks(1, 1, 1, 5, 4, 6, block.CACTUS)
   


   


def chest():
    mc.setBlock(15, 16, 15, block.CHEST)
    
def prepare():
    mcDrawing.drawFace
    W = Wall()
    P = Pyramidka()
    P.draw()
    draw_flat()
    draw_bedrock()
    #num = input('Сколько ловушек?')
    #num_int = int(num)
    draw_lava(700)
    chest()
    
def game():
    while True:
        pass



def main():
    prepare()
    #game()

main()