#3 - Refaça o programa anterior (refatorar) para que o programa recebe a distância e a velocidade média,
#    mas calcule e exiba o tempo da viagem.

import math

distancia_percorrida = int(input("Qual a distância que você irá percorrer em quilômetros?[Use um valor inteiro] "))
velocidade_media = int(input("Qual a sua velocidade média durante o percurso?[Use um valor inteiro] ")) 

tempo_viagem = math.ceil((distancia_percorrida/velocidade_media)*60)

print(f"Para essa viagem você vai levar {tempo_viagem} minutos")
