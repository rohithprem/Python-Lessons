
myUniqueList = []
myLeftovers = []

def addToList(value):
  if (value in myUniqueList):
    myLeftovers.append(value)
    return False
  else:
    myUniqueList.append(value)
    return True



addToList(1)
addToList(2)
addToList(3)
addToList(4)
addToList(1)
addToList(2)
addToList(2)
addToList(3)
addToList(4)
addToList(5)
addToList(5)
addToList(10)
addToList(11)
addToList(1)


print("Unique");
print(myUniqueList);
print("Lefover");
print(myLeftovers);