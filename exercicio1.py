#1 - Um usuário (diabético) de insulina rápida precisa fazer uso do medicamento sempre que for realizar
#    uma refeição. Assim, faça um programa que receba do usuário sua glicemia do momento (mg/dl),
#    meta pré-refeição (em geral é 100 mg/dl), fator de sensibilidade (valor inteiro entre 20 a 60). 
#    A partir desses valores, o programa deve calcular e exibir para o usuário a quantidade de insulina
#    que ele deverá administrar baseada na equação: 
#    quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade

glicemia_do_momento = int(input("Informe sua glicemia do momento:" ))
meta_pre_refeicao = int(input("Informe sua meta de refeição [100-140]: "))
fator_sensibilidade = int(input("Informe seu fator sensibilidade [20-60]: ")) 

quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade

if quantidade_insulina <= 0 :
  quantidade_insulina = 0
  print("Voce não precisa usar insulina neste momento")
else :
  print(f"A quantidade de insulina deve ser {quantidade_insulina} unidades")
