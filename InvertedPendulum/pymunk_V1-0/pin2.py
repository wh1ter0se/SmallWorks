# double pendulum
from joint import *

p = Vec2d(200, 190 )
v = Vec2d(80, 0)

c1 = Circle(p+v)
PinJoint(b0, c1.body, p)

segment1 = Segment(p, v)
PivotJoint(b0, c1.body, p)

c2 = Circle(p+2*v)
PinJoint(c1.body, c2.body)

# SimpleMotor(b0, c1.body, 10)

App().run()