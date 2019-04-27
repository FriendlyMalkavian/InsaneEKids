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
         self.a = [Vec3(30, 30, 30),
         Vec3(30, 30, 60),
         Vec3(45, 45, 45),]
         self.b = [Vec3(30, 30, 60),
         Vec3(60, 30, 60),
         Vec3(45, 45 , 45),]
         self.c = [Vec3(60, 30, 30),
         Vec3(60, 30, 60),
         Vec3(45, 45, 45),]
         self.d = [Vec3(30, 30, 30),
         Vec3(60, 30, 30),
         Vec3(45, 45, 45),]
    
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

LENGTH = 300
def draw_flat():
    for x in range(LENGTH):
        for z in range(LENGTH):
             mc.setBlock(x, 30, z, block.GRASS)
             
def draw_flat2():
    for x in range(LENGTH):
        for z in range(LENGTH):
             mc.setBlock(x, 29, z, block.GRASS)
             
def draw_bedrock():
    for x in range(LENGTH):
        for z in range(LENGTH):
             mc.setBlock(x, -1, z, block.BEDROCK)

def draw_lava(count):
    for c in range(count):
        r_x = randint(0,LENGTH-1)
        r_z = randint(0,LENGTH-1)
        mc.setBlock(r_x, 30, r_z, block.LAVA_STATIONARY )
        
def draw_cactus(count):
    for c in range(count):
        r_x = randint(0,LENGTH-1)
        r_z = randint(0,LENGTH-1)
        mc.setBlock(r_x, 31, r_z, block.CACTUS )
        mc.setBlock(r_x, 32, r_z, block.CACTUS )
        
        
        
        

        
class Wall:
    def __init__(self):
        mc.setBlocks(1, 1, 1, 5, 4, 6, block.CACTUS)
      
SKY = 70      
def draw_air():
    for x in range(LENGTH):
        for z in range(LENGTH):
            for y in range (SKY):
             mc.setBlock(x, y, z, block.AIR)
        

   


   


def chest():
    mc.setBlock(45, 46, 45, block.CHEST)
    
def prepare():
    mcDrawing.drawFace
    W = Wall()
    P = Pyramidka()
    P.draw()
    draw_flat()
    draw_flat2()
    draw_bedrock()
    #num = input('Сколько ловушек?')
    #num_int = int(num)
    draw_lava(2800)
    chest()
    draw_cactus(3000)
def game():
    while True:
        pass



def main():
    prepare()
    #game()

main()
#draw_air()