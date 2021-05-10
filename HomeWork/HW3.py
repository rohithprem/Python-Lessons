



def compare(arg1, arg2, arg3):
  if (int(arg1) == int(arg2)) or (int(arg2) == int(arg3)) or (int(arg3) == int(arg1)):
    return True
  else:
    return False


print(compare(6,5,5))
print(compare(6,5,"5"))
print(compare(6,5,"7"))
