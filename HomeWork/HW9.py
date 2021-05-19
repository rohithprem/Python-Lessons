class Vehicle():

  def __init__(self, make, model, year, weight, needsMaintenance = False, tripSinceMaintenance = 0):
    self.make = make
    self.model = model
    self.year = year
    self.weight = weight
    self.needsMaintenance = needsMaintenance
    self.tripSinceMaintenance = tripSinceMaintenance

  def setMake(self, make):
    self.make = make
  def getMake(self):
    return self.make

  def setModel(self, model):
    self.model = model
  def getModel(self):
    return self.model

  def getYear(self):
    return self.year
  def setYear(self, year):
    self.year = year

  def getWeight(self):
    return self.weight
  def setWeight(self, weight):
    self.weight = weight

  def setNeedsMaintenance(self, needsMaintenance):
    self.needsMaintenance = needsMaintenance
  def getNeedsMaintenance(self):
    return self.needsMaintenance

  def setTripSinceMaintenance(self, tripSinceMaintenance):
    self.tripSinceMaintenance = tripSinceMaintenance
  def getTripSinceMaintenance(self):
    return self.tripSinceMaintenance

  def repair(self):
    self.needsMaintenance = False
    self.tripSinceMaintenance = 0

  def __str__(self):
    return "\nMake: " + self.make + "\nModel: " + self.model + " \nYear: " + str(self.year) + "\nWeight: " + self.weight + "\nNeeds Maintenance: " + str(self.needsMaintenance) + "\nTrips Since Maintenance: " + str(self.tripSinceMaintenance)


class Cars(Vehicle):

  def __init__(self, make, model, year, weight, needsMaintenance = False, tripSinceMaintenance = 0, isDriving = False):
    Vehicle.__init__(self, make, model, year, weight, needsMaintenance, tripSinceMaintenance)
    self.isDriving = isDriving

  def drive(self):
    self.isDriving = True

  def stop(self):
    self.isDriving = False
    self.tripSinceMaintenance += 1
    if self.tripSinceMaintenance > 100:
      self.needsMaintenance = True

class Planes(Vehicle):

  def __init__(self, make, model, year, weight, needsMaintenance = False, tripSinceMaintenance = 0, isFlying = False):
    Vehicle.__init__(self, make, model, year, weight, needsMaintenance, tripSinceMaintenance)
    self.isFlying = isFlying

  def fly(self):
    if self.needsMaintenance:
      print("Plane cannot fly until it is repaired")
      self.isFlying = False
    else:
      self.isFlying = True

    return self.isFlying

  def land(self):
    self.isFlying = False
    self.tripSinceMaintenance += 1
    if self.tripSinceMaintenance > 100:
      self.needsMaintenance = True


car1 = Cars("Honda", "Civic", 2020, "800kg")
car2 = Cars("Toyota", "Camry", 1995, "9500kg")
car3 = Cars("Jeep", "Cherokee", 2000, "1050kg")


for i in range(101):
  car1.drive()
  car1.stop()

for i in range(50):
  car2.drive()
  car2.stop()

for i in range(200):
  car3.drive()
  car3.stop()

print(car1)
print(car2)
print(car3)

plane1 = Planes("Airbus", "A380", 2020, "10000kg")
plane2 = Planes("Boeing", "777", 1995, "10500kg")
plane3 = Planes("Airbus", "A320", 2000, "9000kg")


for i in range(101):
  if not plane1.fly():
    break;
  plane1.land()

for i in range(50):
  if not plane2.fly():
    break;
  plane2.land()

for i in range(200):
  if not plane3.fly():
    break;
  plane3.land()

print(plane1)
print(plane2)
print(plane3)





