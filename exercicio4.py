#4 - O volume de um cubo é determinado através do produto da área da base pela altura, 
#    (mas as arestas do cubo possuem medidas iguais), então temos que:
#    V = Ab * a ou V = a * a * a → V = a³. A partir disso, faça um programa, adequando as variáveis
#    para receber medidas de uma piscina (altura, largura e comprimento), para responder o volume de
#    água necessário para enchê-la.

altura = float(input("Qual a altura da sua piscina? [Em metros]"))
largura = float(input("Qual a largura da sua piscina? [Em metros]"))
comprimento = float(input("Qual o comprimento da sua piscina? [Em metros]"))

volume = altura * largura * comprimento 

print(f"Para essa piscina e com essas medidas serão necessários {volume} metros cúbicos de água ou {volume * 1000} litros de água")
