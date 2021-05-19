import sys
from termcolor import colored

boardMatrix = []
boardRows = 6
boardCols = 7

def getDirectionalMatches(currentRowIndex, currentColIndex, rowIncrementValue, colIncrementValue, symbol):
  matches = 0
  newRowIndex = currentRowIndex + rowIncrementValue
  newColIndex = currentColIndex + colIncrementValue
  # print("Col:",newColIndex, "Row:", newRowIndex)
  if newRowIndex == boardRows or newColIndex == boardCols or newRowIndex < 0 or newColIndex < 0:
    return matches
  if boardMatrix[newColIndex][newRowIndex] == symbol:
    matches += 1
    matches += getDirectionalMatches(newRowIndex, newColIndex, rowIncrementValue, colIncrementValue, symbol)
  return matches


def checkVerticalConnect4(currentCol, latestRowIndex, currentSymbol):
  isConnect4 = False
  matches = 0
  for i in range(latestRowIndex, len(currentCol)):
    if currentCol[i] == currentSymbol:
      matches += 1
    else:
      break

  return matches == 4


def verifyHorizontalConnect4(latestRowIndex, latestColIndex, currentSymbol):
  horizontalMatches = getDirectionalMatches(latestRowIndex, latestColIndex, 0, 1, currentSymbol)
  horizontalMatches += getDirectionalMatches(latestRowIndex, latestColIndex, 0, -1, currentSymbol)

  return horizontalMatches == 3


def verifyRisingDiagonalConnect4(latestRowIndex, latestColIndex, currentSymbol):
  diagonalMatches = getDirectionalMatches(latestRowIndex, latestColIndex, -1, 1, currentSymbol)
  diagonalMatches += getDirectionalMatches(latestRowIndex, latestColIndex, 1, -1, currentSymbol)
  
  return diagonalMatches == 3


def verifyFallingDiagonalConnect4(latestRowIndex, latestColIndex, currentSymbol):
  diagonalMatches = getDirectionalMatches(latestRowIndex, latestColIndex, 1, 1, currentSymbol)
  diagonalMatches += getDirectionalMatches(latestRowIndex, latestColIndex, -1, -1, currentSymbol)
  
  return diagonalMatches == 3


def verifyWin(latestColIndex, latestRowIndex, currentSymbol):
  currentCol = boardMatrix[latestColIndex]
  if checkVerticalConnect4(currentCol, latestRowIndex, currentSymbol):

    return True
  if verifyHorizontalConnect4(latestRowIndex, latestColIndex, currentSymbol):

    return True
  if verifyRisingDiagonalConnect4(latestRowIndex, latestColIndex, currentSymbol):

    return True
  if verifyFallingDiagonalConnect4(latestRowIndex, latestColIndex, currentSymbol):

    return True

  return False


def initBoardData(rows, cols):
  for colIndex in range(cols):
    # print(colIndex)
    colData = []
    for rowIndex in range(rows):
      # print(rowIndex)
      colData.append(" ")
    boardMatrix.append(colData)


def addToCol(col, symbol):
  colList = boardMatrix[col]
  dataExistsIndex = len(colList)
  for i in range(len(colList)):
    if colList[i] != " ":
      dataExistsIndex = i
      break
  colList[dataExistsIndex-1] = symbol

  return verifyWin(col, dataExistsIndex-1, symbol)


def draw(rows, cols):
  print("\n")
  actualRow = 0
  for rowIndex in range(1, rows+1):
    actualCol = 0
    for colIndex in range(1, cols*2):
      if colIndex%2==0:
        print("|", end="")
      else:
        print(boardMatrix[actualCol][actualRow], end="")
        actualCol += 1
    print("")
    if rowIndex != rows:
      print("-"*((cols*2)-1))
      actualRow += 1
  print("\n")

initBoardData(boardRows,boardCols)
draw(boardRows,boardCols)

while(True):
  col = int(input("Player 1 please provide the col: "))
  isWin = addToCol(col-1, colored('O', 'red'))
  draw(boardRows,boardCols)
  if isWin:
    print("Player 1 Wins!!")
    break

  col = int(input("Player 2 please provide the col: "))
  isWin = addToCol(col-1, colored('X', 'blue'))
  draw(boardRows,boardCols)
  if isWin:
    print("Player 2 Wins!!")
    break

