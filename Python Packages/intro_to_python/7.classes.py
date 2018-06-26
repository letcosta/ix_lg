# -*- coding: utf-8 -*-

"""
Here we explain classes in Python

@author: manugarri
"""

"""
Python is an object oriented language, what does that mean? Even though we can code
in python using "functional programming" (i.e., using functions), python works best
if we use classes.

Classes are defined like this:

class ClassName:
    def method1(self): #-->ALL CLASS METHODS TAKE 'self' AS THE FIRST ARGUMENT
        here goes the method1 code

    def method2(self):
        here goes method2 code
"""

#%%

# For example, we can create a basic car class
class BasicCar:

    def turn_left(self):
        print("Turning Left")

    def turn_right(self):
        print("Turning Right")

print(BasicCar)

#%% 
"""
We have defined a BasicCar class. Classes can be thought of blueprints that we
can use to create actual objects (in programming jargon, this is called
"instantiate a class"). So we can use the class BasicCar to generate basic
cars (we call them objects or instances) (cars that are of class BasicCar)
instancia (objeto) de la clase Coche).
"""

manuel_car = BasicCar() # this is how we create an object
print(manuel_car)

#%%
# This car object is a BasicCar, so its an object of class BasicCar

print(type(manuel_car) == BasicCar)

#%%
# This car has all the methods of class BasicCar
manuel_car.turn_left()
manuel_car.turn_right()

#%%
"""
Besides functions, Classes can have specific characteristics (called attributes)
These attributes can be different for each object that belongs to a class
For example, all cars of class BasicCar will all be 100% similar (all of them
have 2 functions and thats all).

We can create an improved version, that allows us to specify the car color

When we define a class we can use the special method __init__ that we can use to
specify attributes for every specific object we create.
"""

class ColoredCar:

    def __init__(self, color):
        print("instantiating the class")
        self.color = color  #this is a class attribute

    def describe(self):
        # we haven't specified the attribute license_plate, it will default to None
        print("{} Car with license plate {}".format(self.color, self.license_plate))

    def turn_left(self):
        print("Turning Left")

    def turn_right(self):
        print("Turning Right")

    def speed_up(self):
        # we can use pass when we define a method that we know we will use in the future
        # but we dont want to define it now
        pass

    def slow_down(self):
        pass

red_car = ColoredCar(color="red")

#%%
blue_car = ColoredCar(color="blue")
blue_car.describe()
blue_car.turn_left()

#%%
red_car.describe()
print(red_car.color)

#%%
# We can add attributes to instances
red_car.license_plate = "ER23244"
print(red_car.license_plate)

#%%
# Now that we have color as an argument to __init__ we need to specify it or
# it will throw an error
car_without_color = ColoredCar() 

#%% 
# Same as with functions, we can use a default argument value for the __init__ function
class ColoredCarDefaultColor:

    def __init__(self, color="black"):
        self.color = color

    def describe(self):
        # we haven't specified the attribute license_plate, it will default to None
        print("{} Car with license plate {}".format(self.color, self.license_plate))

    def turn_left(self):
        print("Turning Left")

    def turn_right(self):
        print("Turning Right")

    def speed_up(self):
        # we can use pass when we define a method that we know we will use in the future
        # but we dont want to define it now
        pass

    def slow_down(self):
        pass

black_car = ColoredCarDefaultColor()
black_car.describe()

#%%
# We can define many attributes to define an object
class VariableCar:

    def __init__(self, model, max_speed, color="black"):
        self.color = color
        self.model = model
        self.max_speed = max_speed
        self.speed = 0 # the car starts with the engine off

    def describe(self):
        print("Car with Model: {}. Color {}. Max Speed: {}".format(
            self.model, self.color, self.max_speed))

    def describe_state(self):
        if self.speed == 0:
            print("The car is stopped")
        else:
            print("The car is driving at {} miles/hour".format(self.speed))

    def turn_left(self):
        print("Turning Left")

    def turn_right(self):
        print("Turning Right")

    def speed_up(self):
        # we can use pass when we define a method that we know we will use in the future
        # but we dont want to define it now
        pass

    def slow_down(self):
        pass

manuel_car = VariableCar(
        model="Peugeot 308",
        color="Azul", max_speed=140)
manuel_car.describe()
manuel_car.describe_state()


#%%
manuel_car.speed = 100
manuel_car.describe_state()

#%%
print(manuel_car)
#%%
"""
One of the main benefits of classes is that they preserve the "state" of an object
For example, if we werent using classes and we wanted to keep track of each car's
speed we would need to have a dictionary that would need to be in sync with the 
objects themselves.

By using classes each car object keeps its own state

We will add now the speed_up and slow_down functions to have a complete vehicle
"""

class Vehicle:

    def __init__(self, model, max_speed, color="black"):
        self.color = color
        self.model = model
        self.max_speed = max_speed
        self.speed = 0 # the car starts with the engine off

    def describe(self):
        print("Car with Model: {}. Color {}. Max Speed: {}".format(
            self.model, self.color, self.max_speed))

    # The method __repr__ is a python method that gets called when we use print
    def __repr__(self):
        return self.describe()

    def describe_state(self):
        if self.speed == 0:
            print("The car is stopped")
        elif self.speed > 0:
            print("The car is driving at {} miles/hour".format(self.speed))
        else:
            print("The car is pulling back at {} miles/hour".format(self.speed))

    def turn_left(self):
        print("Turning Left")

    def turn_right(self):
        print("Turning Right")

    def speed_up(self, speed_difference):
        print("Accelerating {} miles/h".format(speed_difference))
        # abs returns a number without its sign (always positive)
        self.speed += abs(speed_difference)
        # min returns the minimum value from a list of numbers
        self.speed = min(self.speed, self.max_speed)

    def slow_down(self, speed_difference):
        print("Slowing down {} miles/h".format(speed_difference))
        self.speed -= abs(speed_difference)
        # max returns the maximum value in a list of numbers
        self.speed = max(self.speed, -5)


manuel_car = Vehicle(model="Peugeot 308", color="Blue", max_speed=200)
manuel_car.describe_state()
manuel_car.speed_up(20)
manuel_car.describe_state()

#%%
manuel_car.speed_up(20)
manuel_car.describe_state()

#%%
manuel_car.slow_dow(60)
manuel_car.describe_state()

#%%
manuel_car.speed_up(5)
manuel_car.describe_state()
print(manuel_car)

#%%
"""
Class inheritance

One of the main advantages of using classes is that we can create classes using
other classes as their template (then we say that ClassB "inherits" from ClassA)

This allows us to create base classes and then create advanced classes that have
different functionalities

For example, we can create a Bus class that cant pull back and that has a maximum
speed of 60 miles/hour
"""

class Bus(Vehicle): # here we are specifying that Bus inherits from Vehicle
    def speed_up(self, speed_difference):
        print("Bus speeding up {} miles/h".format(speed_difference))
        self.speed += abs(speed_difference)
        self.speed = min(self.speed, 60)

    def slow_down(self, speed_difference):
        print("Bus slowing down {} miles/h".format(speed_difference))
        self.speed -= abs(speed_difference)
        self.speed = max(self.speed, 0)

school_bus = Bus(model="Mercedes", color="yellow", max_speed=120)
school_bus.describe_state()
school_bus.speed_up(50)
school_bus.describe_state()
school_bus.speed_up(50)
school_bus.describe_state()
school_bus.slow_down(100)
school_bus.describe_state()

#%%
"""
******************************************************************************

EXERCISES


Create a class Taxi, that inherits from Vehicle, that can charge us for a trip
It will have an attribute "total_distance" and three additional methods:
  - method "charge", that prints the amount to charge (3 dollar/mile * total_distance)
  - method "add_distance", that adds to the total distance a number of miles.
  - method "add_time", that given a time (in hours) and knowing the current speed adds distance
    to the total_distance

So you can do something like this:

taxi = Taxi(model="Mercedes Benz", max_speed=120)
taxi.speed_up(100)
taxi.add_time(1)
taxi.add_time(5)
taxi.charge()
******************************************************************************
"""



#%%
"""
******************************************************************************

Create a class Parking Parking, where we can park a limited number of Vehicles
(and only Vehicles!) and get cars out. (we can only get cars out if they are inside)
It can also check the ocupation rate (number of parked cars / total capacity)

parking_rossio = Parking(capacity=100)

manuel_car = Vehicle(model="Peugeot 308", color="Blue", max_speed=100)
red_car = Vehicle(model="Mercedes Benz", color="red", max_speed=140)
taxi = Taxi(model="Mercedes Benz", max_speed=90)

parking_rossio.park_vehicle(manuel_car)
parking_rossio.park_vehicle(red_car)

print(parking_rossio.occupation_rate())

parking_rossio.get_out_car(red_car)

# this will fail
parking_rossio.get_out_car(taxi)
******************************************************************************
"""

