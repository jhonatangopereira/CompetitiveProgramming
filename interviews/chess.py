letras = ["A", "B", "C", "D", "E", "F", "G", "H"]

def is_black(tabuleiro, letra, numero):
  if (retornar_posicao_letra(letra) + numero) % 2 == 0:
    return True
  return False

def retornar_posicao_letra(letra):
  return letras.index(letra) + 1

def print_result(movimentos, caminho):
  # print(f"{movimentos} {letra} {numero}")
  pass


def possiveis_caminhos(letra, numero):
  caminhos = []
  for i in range(retornar_posicao_letra(letra) - 2, 0, -1):
    caminhos.append([letras[i], i])
  print()
  
  for i in range(retornar_posicao_letra(letra), 9):
    print(letras[i - 1], i)
  print()
  
  for i in range(retornar_posicao_letra(letra) - 1, 0, -1):
    print(letras[i - 1], 9 - i)
  print()
  
  for i in range(retornar_posicao_letra(letra), 9):
    print(letras[i - 1], 9 - i)

tabuleiro = []
for i in range(8):
  tabuleiro.append({letras[i]: [j + 1 for j in range(8)]})

# for i in range(len(tabuleiro)):
#   print(tabuleiro[i])

jogadas = int(input())
for i in range(jogadas):
  letra1, numero1, letra2, numero2 = map(str, input().split())
  numero1 = int(numero1)
  numero2 = int(numero2)
  movimentos = 0

  if is_black(tabuleiro, letra1, numero1) != is_black(tabuleiro, letra2, numero2):
    print("Impossible")
    continue
  
  caminho = [[letra1, numero1]]
  if letra1 == letra2 and numero1 == numero2:
    print_result(movimentos, caminho)
    continue


  letraAtual = letra1
  numeroAtual = numero1

  possiveis_caminhos(letraAtual, numeroAtual)
  while True:
    # if letra1 == caminho[-1][0] and numero1 == caminho[-1][0]:
    #   print_result(movimentos, caminho)
    #   break
    break
  

