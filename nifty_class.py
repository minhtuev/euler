# http://blog.lerner.co.il/python-attributes/
class Person(object):
    population = 0
    def __init__(self, first, last):
        self.first = first        
        self.last = last
        Person.population += 1

p1 = Person('Reuven', 'Lerner')
p2 = Person('foo', 'bar')

print Person.population	