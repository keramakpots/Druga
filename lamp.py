class Lamp:


        def __init__(self, color, weight, size, name="<Class instance>", power=10):
            self.color = color
            self.weight = weight
            self.size = size
            self.power = power
            self.name = name

        def __str__(self):
           return str(['{} Attribute {} : {}'.format(self.name, key, value) for key, value in vars(self).items()]).strip("[]")
           #return "Object {} has got attributes: size {}, weight {}, color {}, power {}.".format(self.name, self.size,self.weight,self.color, self.power)

        def turn_it_on(self, working=False):
            if self.power > 40:
                return "To much power in a bulb"
            else:
                working = True

        def name_giver(self):
            return self

class Bulb:


        def __init__(self, power = 20):
            self.power = power
bulb = Bulb(60)
bulb1 = Bulb(30)
l3 = Lamp("Purple", 223, "Enormous")
l1 = Lamp("green", 50, "big", "l1")
l2 = Lamp("Yellow", 400, "Large", "l2", bulb1.power)

print(l1)
print(l2.name_giver())
l1.power = bulb.power + bulb1.power
print(type(vars(l1)))


for key, value in vars(l1).items():
    print('Attribute {} : {}.'.format(key, value))