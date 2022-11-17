#%%

class Car:
    pass

car1 = Car()
car2 = Car()
carN = Car()

other_car = car1

#print(type(car1))

print(car1 == other_car)
# %%

number1 = 4
number2 = 4

print(number1 == number2)

# %%

class Car:

    def __init__(self, brand, model, color):
        if type(brand) != str:
           raise Exception("brand must be a string") 

        self.brand = brand
        self.model = model
        self.color = color


#ferrari = Car("Ferrari", "488", "Red")
#tesla = Car("Tesla", "Model S", "White")

potato = Car("Ford", 5.2, 2)

#print(ferrari.brand)
#print(tesla.model)
# %%

class Clock:

    def __init__(self, hours, minutes):
        if type(hours) != int or type(minutes) != int:
            raise Exception("hours and minutes must be ints")

        self.hours = hours
        self.minutes = minutes


clock_1 = Clock(12, 23)
clock_2 = Clock(10, 5)

bonkers_clock = Clock("hello", -4.2)


print(clock_1.hours)

# %%
