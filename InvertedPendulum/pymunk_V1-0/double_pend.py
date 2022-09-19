# double pendulum
import pymunk

space = pymunk.Space()

class PinJoint:
    def __init__(self, b, b2, a=(0, 0), a2=(0, 0)):
        joint = pymunk.constraint.PinJoint(b, b2, a, a2)
        space.add(joint)

class Circle:
    def __init__(self, pos, radius=20):
        self.body = pymunk.Body()
        self.body.position = pos
        shape = pymunk.Circle(self.body, radius)
        shape.density = 0.01
        shape.friction = 0.5
        shape.elasticity = 1
        space.add(self.body, shape)


b0 = space.static_body

p = pymunk.Vec2d(200, 190 )
v = pymunk.Vec2d(80, 0)

c1 = Circle(p+v)
PinJoint(b0, c1.body, p)

c2 = pymunk.Circle(p+2*v)
PinJoint(c1.body, c2.body)

pymunk.App().run()