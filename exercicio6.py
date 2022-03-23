#6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que 
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens: 
#    Carioca Paulista Mineiro Outros estados

sigla_estado = input("Qual a sigla do seu estado? ")

sigla_estado = sigla_estado.upper()

if sigla_estado == "RJ":
  print("Você é carioca")
elif sigla_estado == "SP":
  print("Você é paulista")
elif sigla_estado == "MG":
  print("Você é mineiro")
else:
  print("Você é de outro estado")