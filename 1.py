def is_degenerated(xy: tuple) -> bool:
    return xy[0] == xy[1]
def is_vertical(xy: tuple) -> bool:
    return xy[0][0] == xy[1][0] and xy[0][1] != xy[1][1]
def is_horizontal(xy: tuple) -> bool:
    return xy[0][1] == xy[1][1] and xy[0][0] != xy[1][0]
def is_inclined(xy: tuple) -> bool:
    return is_degenerated(xy) == False and is_vertical(xy) == False and is_horizontal(xy) == False

line1 = (0, 10), (100, 130)
line2 = (42, 1), (42, 2)
line3 = (100, 50), (200, 50)
line4 = (50, 50), (50, 50)
print(is_degenerated(line1), is_vertical(line1), is_horizontal(line1), is_inclined(line1))
print(is_degenerated(line2), is_vertical(line2), is_horizontal(line2), is_inclined(line2))
print(is_degenerated(line3), is_vertical(line3), is_horizontal(line3), is_inclined(line3))
print(is_degenerated(line4), is_vertical(line4), is_horizontal(line4), is_inclined(line4))
