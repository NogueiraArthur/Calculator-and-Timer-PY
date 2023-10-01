import time

def timer():
 secs = int(input("\nsetar o timer para quantos segundos? "))
 x = 0
 print("------------")
 while (x <= secs):
   print(x)
   time.sleep(1)
   x += 1

def calculadora():
  n1 = int(input("\nnumero1: "))
  calculo = input("sinal: ")
  n2 = int(input("numero2: "))

  if calculo == "+":
    resultado = n1 + n2
  if calculo == "-":
    resultado = n1 - n2
  if calculo == "*":
    resultado = n1 * n2
  if calculo == "/":
    resultado = n1 / n2
    
  print(resultado)

  

print("1 - timer")
print("2 - calculadora")

pesquisa = int(input("digite a funcao desejada:\n"))

if pesquisa == 1:
  timer()
if pesquisa == 2:
  calculadora()