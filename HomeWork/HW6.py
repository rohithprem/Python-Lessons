import os
#  | | 
# -----
#  | | 

def draw(rows,cols):
  terminalSize = os.get_terminal_size(0);
  lines = terminalSize.lines
  columns = terminalSize.columns
  if cols > columns/2 or rows > lines/2:
    return False

  for rowIndex in range(1, rows+1):
    for colIndex in range(1, cols*2):
      # print(colIndex, end="")
      if colIndex%2==0:
        print("|", end="")
      else:
        print(" ", end="")
    print("")
    if rowIndex != rows:
      print("-"*((cols*2)-1))

  return True


print(draw(30 ,100))
