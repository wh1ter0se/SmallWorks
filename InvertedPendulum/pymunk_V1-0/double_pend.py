# double pendulum
import pymunk

space = pymunk.Space()

class PinJoint:
    def __init__(self, b, b2, a=(0, 0), a2=(0, 0)):
        joint = pymunk.constraint.PinJoint(b, b2, a, a2)
        space.add(joint)

b0 = space.static_body

p = pymunk.Vec2d(200, 190 )
v = pymunk.Vec2d(80, 0)

c = pymunk.Circle(p+v)
PinJoint(b0, c.body, p)

c2 = pymunk.Circle(p+2*v)
PinJoint(c.body, c2.body)

pymunk.App().run()