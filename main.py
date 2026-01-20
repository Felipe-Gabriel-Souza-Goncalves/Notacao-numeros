import math

# Arrays de sufixos disponíveis
sufixosLongos = [" mil", " milhões", " bilhões", " trilhões", " quadrilhões", " quintilhões", " sextilhões", " octilhões", " nonilhões", " decilhões"]
sufixosCurtos = ["k", "mi", "bi", "tri", "qua", "qui", "sex", "sep", "oct", "non", "dec"]

def transformNum(num, precisao = 1, curto = False):

  # Filtra a string e pega seu tamanho
  stringNum = str(num)
  stringNum = filterStringNum(stringNum)
  size = len(stringNum)

  # Retorna se número for menor que 1000
  if(size <= 3):
    return num
  else:
    # Qual index para pegar no array de sufixos
    index = math.ceil((size - 3) / 3) - 1 

  # Calcula quantos números antes do ponto
  endFor = size % 3
  if(endFor == 0):
    endFor = 3

  # String que será retornada
  finalString = ""

  # Se o número for negativo
  if(num[0] == "-"):
    finalString += "-"

  # Adiciona os números necessários antes do ponto
  for i in range(0, endFor, 1):
    finalString+= stringNum[i]

  # Adiciona o resto dos números para precisão
  if(precisao > 0):
    finalString += "."

    # Adiciona 0 se a precisão for maior que o tamanho do número
    for j in range(endFor, endFor + precisao, 1):
      if(j > size - 1):
        finalString += "0"
        continue
      
      finalString += stringNum[j]

  # Adiciona o sufixo (longo/curto)
  if(curto):
    finalString += sufixosCurtos[index]
  else:
    finalString += sufixosLongos[index]

  return finalString


def filterStringNum(stringNum):
  stringNum = str(stringNum)
  stringNum = stringNum.replace(".", "")
  stringNum = stringNum.replace(" ", "")
  stringNum = stringNum.replace("+", "")
  stringNum = stringNum.replace("-", "")

  return stringNum
