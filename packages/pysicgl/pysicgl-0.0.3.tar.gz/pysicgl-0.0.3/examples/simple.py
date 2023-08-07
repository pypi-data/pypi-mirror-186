import pysicgl

# create a screen definition with extent (WIDTH, HEIGHT)
WIDTH = 256
HEIGHT = 128
display_screen = pysicgl.Screen((WIDTH, HEIGHT))

# allocate memory for the interface using the number of
# pixels in the display screen
display_memory = pysicgl.allocate_pixel_memory(display_screen.pixels)

# create an interface which controls access to this
# memory. the screen definition is used to inform
# geometrical constraints.
display = pysicgl.Interface(display_screen, display_memory)

# create a orange-red color using a 4-tuple of RGBA components
color = pysicgl.Color.from_rgba((255, 128, 3, 0))

# draw a pixel directly to the interface origin
# the coordinates are given in the interface-relative system
display.interface_pixel(color, (0, 0))

# show the fist pixel as memory
print(list(display.memory[0:4]))
