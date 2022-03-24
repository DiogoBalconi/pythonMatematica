#7 - Faça um programa Python que receba duas notas, calcule a média aritmética e mostre o resultado.
#    Além disso, deve mostrar ao lado da média Aprovado (se média >= 7.0) Reprovado (se média <= 3.0),
#    Exame (se média entre 3.0 e 7.0)

primeira_nota = float(input("Qual a sua primeira nota? "))
segunda_nota = float(input("Qual a sua segunda nota? "))

media = (primeira_nota + segunda_nota)/2
print(f"sua média é {media}")

if(media >= 7):
  print("Aprovado")
elif(media <= 3 ):
  print("Reprovado")
elif(3 < media < 7):
  print("Exame")
