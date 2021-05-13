metadata = {"artist":"Radiohead", "genre":"Grunge", "song":"House of Cards","album":"In Rainbows", "durationInSeconds":329, "trackNo":3, "year":2007, "subgenres":["Experimental, Progressive, Rock"], "composer":"Thom Yorke", "language":"English"}


for metaKey in metadata:
  print(metaKey)
  print(metadata[metaKey])
  print("")



def guessParam(key, value):
  if key in metadata and value == metadata[key]:
    return True
  else:
    return False


while True:
  inputKey = input("What would you like to guess? => ")
  print(inputKey)
  inputValue = input("What's the answer? => ")
  print(guessParam(inputKey,inputValue))