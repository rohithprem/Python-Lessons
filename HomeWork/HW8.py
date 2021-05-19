import os.path
from os import path

def replaceFile(sFileName, sFileWriteMode, aNewValues):
  fFile = open(sFileName, sFileWriteMode)
  for sLine in aNewValues:
    fFile.write(sLine.strip("\n") + "\n");

sFileName=input("Please enter file name: ")
bIsFileExists = path.exists(sFileName)

if bIsFileExists:
  print("File Exists. What would you like to do?")
  print("A) Read the file contents")
  print("B) Delete the file and start over")
  print("C) Append the file")
  print("D) Replace a line")
  sUserSelection = input("Your Selection: ")

  if sUserSelection == "A":
    fFile = open(sFileName, "r")
    sFileContent = fFile.read()
    print(sFileContent);
    fFile.close()

  elif sUserSelection == "B":
    sNewValue = input("Enter data to replace in file: ")
    replaceFile(sFileName, "w", [sNewValue])

  elif sUserSelection == "C":
    sNewValue = input("Enter data to append to file: ")
    replaceFile(sFileName, "a", ["\n" + sNewValue])

  elif sUserSelection == "D":
    iLineToReplace = int(input("Which line would you like to replace? "))
    fFile = open(sFileName, "r")
    lLines = fFile.readlines()
    fFile.close()
    lLines[iLineToReplace-1] = input("What would you like to replace the line with? ")
    replaceFile(sFileName, "w", lLines)


else:
  sNewValue = input("Enter data to write to new file: ")
  replaceFile(sFileName, "w", [sNewValue])