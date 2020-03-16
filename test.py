# This program builds a tall tower inside Minecraft, using a for loop.
# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
# Connect to the Minecraft game
mc = minecraft.Minecraft.create()
# Get the player position
pos = mc.player.getTilePos()
# Build a tower 50 blocks high
for a in range(50):
    # Each block is at height: y+a
    mc.setBlock(pos.x+3+a, pos.y+a, pos.z, block.STAIRS_WOOD.id)
# END
