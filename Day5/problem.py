## keyword *args
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# add(4, 5, 6) # 15

## keyword **kwargs
def calculate(**kwargs):
    print(kwargs)

# calculate(add=3, multiply=5) # {'add': 3, 'multiply': 5}

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT3")
# print(my_car.model) # GT3

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)

## manipolation list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 24, 34, 55]
squared_numbers = [x**2 for x in numbers]
# print(squared_numbers)

list_of_string = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers2 = [int(x) for x in list_of_string]
result = [x for x in numbers2 if x % 2 == 0]
# print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
# print(result)