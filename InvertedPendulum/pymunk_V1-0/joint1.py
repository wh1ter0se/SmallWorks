# pivot point
from joint import *

p = Vec2d(100, 190)
v = Vec2d(80, 0)


segment = Segment(p+3*v, 2*v)
PivotJoint(b0, segment.body, p+3*v)

segment2 = Segment(p+5*v, v)
PivotJoint(segment.body, segment2.body, 2*v)

App().run()