import math

sufixosLongos = ["mil", "mi", "bi", "tri", "qua", "qui", "sex"]
sufixosCurtos = ["k", "m", "b", "t", "q", "qui", "s"]

def transformNum(num, precisao = 1, curto = False):
  stringNum = str(num)
  size = len(stringNum)

  if(size <= 3):
    print("num",num)
    return num
  else:
    index = math.ceil((size - 3) / 3) - 1

  finalString = ""

  endFor = size % 3
  if(endFor == 0):
    endFor = 3

  for i in range(0, endFor, 1):
    finalString+= stringNum[i]

  if(precisao > 0):
    finalString += "."
    for j in range(endFor, endFor + precisao, 1):
      if(j > size - 1):
        finalString += "0"
        continue
      
      finalString += stringNum[j]

  finalString += sufixosCurtos[index] if curto == True else sufixosLongos[index]
  return finalString

