class Car:
  # Problem 6: variable Creation
  total_cars = 0

  # Problem 1: Class and Object
  def __init__(self, userBrand, userModel):
    self.__brand = userBrand
    self.__model = userModel
    # self.total_cars
    Car.total_cars += 1

  # Problem 2: Class and Self Method
  def fullName(self):
    return f"{self.__brand} {self.__model}"

  # Problem 4: Encapsulation
  def get_brand(self):
    return self.__brand +"!"

  # Problem 4: Polymorphism
  def fuel_type(self):
    return "Petrol and Diesel"
  
  # Problem 7: Static Methods
  # self is not required when staticmethod is used (Decorators)
  @staticmethod
  def general_descrion():
    return "Cars are Good Means of Travelling."

  # Problem 8: Make readable objects
  @property
  def model(self):
    return self.__model

  # Problem 3: Inheritance
class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

  # Problem 4: Polymorphism
  def fuel_type(self):
    return "Electric Charge"

# Problem 1
toyota = Car("Toyota","Corolla")
# print(my_car.__brand)
print(toyota.get_brand)
print(toyota.model)

# Problem 2
tata = Car("Tata","Safari")
print(tata.fullName())

# Problem 3
tesla = ElectricCar("Tesla","Model S","85kWh")
print(tesla.fullName())

# Problem 4
# print(my_tesla.__brand())
print(tesla.get_brand())

# Problem 5
print(tesla.fuel_type())
print(tata.fuel_type())

# Problem 6
# test = Car("test","test")
# print(test.total_cars)
print(Car.total_cars)

# Problem 7: Use of decorators
print(tesla.general_descrion())
print(Car.general_descrion())

# Problem 8:
print(tata.model)

# Problem 9: isinstance() method
print(isinstance(tesla,Car))
print(isinstance(tesla, ElectricCar))



# Problem 10: Multiple Inheritence
class Battery:
  def battery_info(self):
    return "This is battery"

class Engine:
  def engine_info(self):
    return "This is engine"

class ElectricCarTwo(Car, Engine, Battery):
  pass

new_tesla = ElectricCarTwo("Tesla","Model S")
print(new_tesla.battery_info())
print(new_tesla.engine_info())