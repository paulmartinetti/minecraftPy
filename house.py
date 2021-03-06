# This program builds a house with a doorway, windows, a roof
# and a carpet. It defines a house() function that you can easily # reuse in other programs.
# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
# Connect to Minecraft
mc = minecraft.Minecraft.create()
# A constant, that sets the size of your house
SIZE = 20
# define a new function, that builds a house
def house():
    # Calculate the midpoints of the front face of the house
    midx = x+SIZE/2
    midy = y+SIZE/2
    # Build the outer shell of the house
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.COBBLESTONE.id)
    # Carve the insides out with AIR
    mc.setBlocks(x+1, y, z+1, x+SIZE-1, y+SIZE-1, z+SIZE-1, block.AIR.id)
    # Carve out a space for the doorway
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)
    # Carve out the left hand window
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)
    # Carve out the right hand window
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)
    # Add a wooden roof
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, block.WOOD.id)
    # Add a woolen carpet, the colour is 14, which is red.
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-2, y-1, z+SIZE-2, block.WOOL.id, 14)
   # Get the players position
pos = mc.player.getPos()
# Decide where to start building the house, slightly away from player
x = pos.x + 2
y = pos.y
z = pos.z
# run the house() function that was defined by def house():
# this will build a house at x,y,z
house()
# END
