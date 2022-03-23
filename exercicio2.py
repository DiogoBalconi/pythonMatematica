#2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.

import math #usando uma biblioteca para aplicar a função ceil() que arredonda um valor para cima

distancia_percorrida = int(input("Quantos quilômetros você irá percorrer?[Use um valor inteiro] "))
tempo_minutos = int(input("Quanto tempo irá durar sua viagem em minutos? " )) 

tempo_horas = tempo_minutos/60
velocidade_media = math.ceil(distancia_percorrida/tempo_horas)

print(f"Para esta viagem você precisará manter uma velocidade média de {velocidade_media} km/h")
