"""polymophism in python"""

import random
from turtle import speed


students = ['adj', 'tanu', 'jony']
school = 'vnmps'

# calculating count
print(len(students))
print(len(school))

# the len() method treats an object as per its class type
# it prints out  3 for dictionary/list and 5 for string, thats polymorphism

"""method overrinding"""

class Ford:

    def __init__ (self, name, color, price):

        self.name = name
        self.color = color
        self.price = price
        self.details = []

    def show(self):

        details = str(self.name) + str(self.color) + str(self.price)

        self.details.append(details)

        return self.details

    def speed(self, speed):

        speed = random.randint(180)

        print('hii gari iko na speed ya maximum, {0}'.format(speed))

    def change_gear(self):

        gear_number = random.randomint(3)

        if speed <= 30 and gear_number == 1:

            print('gari imeregister hard start!')

        else:

            print('bado gari haijaanza')

        if speed > 30 and gear_number == 2:

            print('gari imeregister good start')

        else:

            print('gari inaanza vizuri')


class Mustang(Ford):

    def max_speed(self):
        print('Mustang max speed is' + str(self.max_speed))

    def change_gear(self):
        print('Mustang changes gear 7')

# Car model object

Ford_Mustang = Mustang('X1', 'Red', 20000)
Ford_Mustang.show()

# Calling methods for the class Mustang

Ford_Mustang.change_gear()
Ford_Mustang.speed()

ford = Ford('X', 'Black', 50000)
ford.show()

#Calling methods for the class Ford

ford.change_gear()
ford.speed(30)


