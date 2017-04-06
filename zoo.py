zoo = ('tiger', 'elephant', 'gorilla', 'hyena', 'shark')
print(zoo)

print(zoo.index('gorilla'))

for animal in zoo:
    if animal is "hyena":
        print(animal)

(tiger, elephant, gorilla, hyena, shark) = zoo
print(tiger)
print(elephant)
print(gorilla)
print(hyena)
print(shark)

zoo2 = list(zoo)

zoo2.append('monkey')
zoo2.append('cheetah')
zoo2.append('seal')
print(zoo2)

zoo = tuple(zoo2)
print(zoo)
