import os
#  | | 
# -----
#  | | 

crosses = [[],[],[]]
zeroes = [[],[],[]]

def draw(rows,cols):
  terminalSize = os.get_terminal_size(0);
  lines = terminalSize.lines
  columns = terminalSize.columns
  if cols > columns/2 or rows > lines/2:
    return False

  actualRow = 0
  for rowIndex in range(1, rows+1):
    actualCol = 0
    for colIndex in range(1, cols*2):
      # print(colIndex, end="")
      if colIndex%2==0:
        print("|", end="")
      else:
        if actualCol in crosses[actualRow]:
          print("X", end="")
        elif actualCol in zeroes[actualRow]:
          print("O", end="")
        else:
          print(" ", end="")
        actualCol += 1
    print("")
    if rowIndex != rows:
      print("-"*((cols*2)-1))
      actualRow += 1

  return True


draw(3,3)

while(True):
  rowCol = input("Player 1 please provide the move as row,col: ")
  rowColArray = rowCol.split(",")
  row = int(rowColArray[0])
  col = int(rowColArray[1])
  zeroes[row].append(col);
  draw(3,3)

  rowCol = input("Player 2 please provide the move as row,col: ")
  rowColArray = rowCol.split(",")
  row = int(rowColArray[0])
  col = int(rowColArray[1])
  # crosses.append([row,col])
  crosses[row].append(col);
  draw(3,3)

