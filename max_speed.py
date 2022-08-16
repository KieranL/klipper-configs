import sys


printer_max_x = 250
printer_max_y = 250
margin_x = 5
margin_y = 5

feedrate = int(sys.argv[1])

times = int(sys.argv[2])

positions = [
    [0,0],
    [1,0],
    [1,1],
    [0,1],
    [0,0],
    [1,1],
    [1,0],
    [0,1],
    [0,0]
]

x_min = margin_x
x_max = printer_max_x - margin_x
y_min = margin_y
y_max = printer_max_y - margin_y
feedrate_mm_min = feedrate * 60

with open('test.gcode', 'w') as fp:
    for iteration in range(1, times + 1):
        fp.write(f';Iteration {iteration}\n')

        for position in positions:
            x = margin_x + (printer_max_x - margin_x * 2) * position[0]
            y = margin_y + (printer_max_y - margin_y * 2) * position[1]
            fp.write(f'G1 X{x} Y{y} F{feedrate_mm_min}\n')
