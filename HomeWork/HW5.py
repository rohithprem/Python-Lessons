
def checkPrime(number):
  isPrime = True
  if number > 3:
    for n in range(2, int(number/2)):
      if number%n == 0:
        isPrime = False
        break
  return isPrime

for number in range(1, 100):
  isDivBy3 = False
  isDivBy5 = False
  isPrime = False
  if number%3 == 0:
    print("fizz", end="")
    isDivBy3 = True
  if number%5 == 0:
    print("buzz", end="")
    isDivBy5 = True
  if (not isDivBy3) and (not isDivBy5):
    isPrime = checkPrime(number)
    if isPrime:
      print("prime", end="")
    else:
      print(number, end="")
  print("")


