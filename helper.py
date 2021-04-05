
def calculate_quadrants(width, height, left=0, top=0):
    """
    Calculates quadrants of a rect defined by provided attributes. The returned points will be the middle points of
    the rects 0 to 8 which are defined by the horizontal and vertical thirds of the rect.

    visualisation:
    -------------------
    |  x  |  x  |  x  |
    -------------------   
    |  x  |  x  |  x  |
    -------------------    
    |  x  |  x  |  x  |
    -------------------
    """
    return [
        [left+width//6, top+height//6],
        [left+3*width//6, top+height//6],
        [left+5*width//6, top+height//6],
        [left+width//6, top+3*height//6],
        [left+3*width//6, top+3*height//6],
        [left+5*width//6, top+3*height//6],
        [left+width//6, top+5*height//6],
        [left+3*width//6, top+5*height//6],
        [left+5*width//6, top+5*height//6],
    ]

delta = 20

# What kint of movement does a number equate to? This only applied for special mode of direct movement.
move_delta = [
    [-delta, -delta],
    [0, -delta],
    [delta, -delta],
    [-delta, 0],
    [0, 0],
    [delta, 0],
    [-delta, delta],
    [0, delta],
    [delta, delta],
]

# Map the numbers in regular order to the directions implied by the numpad. (Left top == 7; Middle = 5; Right bottom == 3; ...)
mapping = {1: 6, 2: 7, 3: 8, 4: 3, 5: 4, 6: 5, 7: 0, 8: 1, 9: 2}