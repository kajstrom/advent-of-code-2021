def get_coords(source, coords):
    x, y = coords
    return source[x][y]


def set_coords(source, coords, value):
    x, y = coords
    source[x][y] = value