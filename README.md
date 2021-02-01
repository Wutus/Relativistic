#### Summary

Application simulates movement of relativistic body in space.

### Description

- Unit for time is: 1s
- Unit for distanse is: 1c*1s (one lightsecond)
- Unit for velocity is: 1c (one lightspeed)

### Arguments

python main.py x1 y1 velocity_x1 velocity_y1  x2 y2 velocity_x2 velocity_y2

- x1 - x component of position of the body no. 1
- y1 - y component of position of the body no. 1
- vx1 - x component of velocity of the body no. 1
- vy1 - y component of velocity of the body no. 1
- x2 - x component of position of the body no. 2
- y2 - y component of position of the body no. 2
- vx2 - x component of velocity of the body no. 2
- vy2 - y component of velocity of the body no. 2

### Controls

Keys:
- 1/2/3 - change frame of reference to body no. 1/2/3
- q - change view to 2D coordinate perspective (and adjust simultaneousness)
- w - change view to spacetime-diagrams view (the left one is for x component, the right one for y component)
- e - force simultaneousness in spacetime-diagram view

### Known bugs
The formula for calculating speed when frame of reference is changed in two coordinates can reduce to nan.