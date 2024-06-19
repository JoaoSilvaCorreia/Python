
"""
    Descrição: Lista de exercícios - Funções
    Autor: João Vitor
    Data: 30/03/2016
"""


#1A
print("Dados três numeros, calcule a soma")
def somador(n1,n2,n3):
    soma = n1+n2+n3
    return soma
print("O valor da soma é:",somador(50,7,3))
print('\n''\n')





#1B
print("Dados três numeros, calcule a subtração")
def subtrair(n1,n2,n3):
    menos = n1-n2-n3
    return menos
print("O valor da subtração é:",subtrair(10,5,2))
print('\n''\n')





#1C
print("Dados três numeros, calcule a multiplicação")
def multiplicar(n1,n2,n3):
    vezes = n1*n2*n3
    return vezes
print("O valor da multiplicação é:",multiplicar(2,3,4))
print('\n''\n')




#1D
print("Dados três numeros, calcule a divisão")
def divisor(n1,n2,n3):
    dividir = n1/n2/n3
    return dividir
print("O valor da divisão é:",divisor(16,4,2))
print('\n''\n')





#2A - retângulo
print("Calcule a área e o perimetro do retângulo")
def calculo_area(l1,l2):
    area = l1*l2
    return area
print("O valor da área do retângulo é:",calculo_area(10,20))



def calculo_perimetro(l1,l2,l3,l4):
    perimetro = l1+l2+l3+l4
    return perimetro
print("O valor do perimetro do retângulo é:",calculo_perimetro(10,20,10,20))
print('\n''\n')




#2B - quadrado
print("Calcule a área e o perimetro do quadrado")
def calculo_area(l1):
    area = l1**2
    return area
print("O valor da área do quadrado é:", calculo_area(20))

def calculo_perimetro(l1):
    perimetro = l1*4
    return perimetro
print("O valor do perimetro do quadrado é:",calculo_perimetro(20))
print('\n''\n')




#2C - círculo
import math
print("Calcule a área e o perimetro círculo")
def calculo_area(raio):
    area = raio**2*math.pi
    return area
print("O valor  da área do círculo é:",calculo_area(5))

def calculo_perimetro(raio):
    perimetro = 2*math.pi*raio
    return perimetro
print("O valor  do perimetro do círculo é:",calculo_perimetro(5))
print('\n''\n')






#2D - triângulo
print("Calcule a área e o perimetro do triângulo")
def calculo_area(b,h):
    area = b*h/2
    return area
print("O valor  da área do triângulo é :", calculo_area(10,5))


def calculo_perimetro(l1,l2,l3):
    perimetro = l1+l2+l3
    return perimetro
print("O valor  do perimetro do triângulo é:",calculo_perimetro(10,5,5))
print('\n''\n')




#3
print("Função que calcula área do triângulo equilatero, com apenas um lado fornecido")
def triangulo_equi(l):
    area = (l**2)/4*math.sqrt(3)
    return area
print("O valor  da área do triângulo equilatero é :",triangulo_equi(10))
print('\n''\n')




#4
print("Função que calcula a média do aluno")
def media_aluno(a1,a2,a3,a4):
    media = (a1+a2+a3+a4)/4
    return media
print("A media do aluno é:",media_aluno(100,80,70,50))
print('\n''\n')



#5
print("Função que retorne antecessor e sucessor de um número")
def antecessor_sucessor(n):
    antecessor = n-1
    sucessor = n+1
    return antecessor,sucessor
print("Antecessor e sucessor são :",antecessor_sucessor(5))
print('\n''\n')




#6
print("Função que retorne a terça parte do quadrado de um número inteiro/positivo")
def retorne_terca_parte(n):
    calculo = n**2/3
    return calculo
print("Terça parte do quadrado é:",retorne_terca_parte(10))
print('\n''\n')



#7
print("Função que retorne o quadrado e a raiz de um valor inteiro/positivo")
def retorne_quadrado_raiz(v):
    calculo1 = v**2
    calculo2 = math.sqrt(v)
    return calculo1,calculo2
print("O quadrado e a raiz são:",retorne_quadrado_raiz(9))
print('\n''\n')





#8
print("Função da média ponderada de 4 valores")
def media_ponderada(v1,v2,v3,v4):
    calculo = v1*1+v2*2+v3*3+v4*4/10
    return calculo
print("A media ponderada é:",media_ponderada(2,4,6,8))
print('\n''\n')





#9
print("Função que solucione uma equação do 2grau")
def equacao_2grau(a,b,c):
    x1 = b+math.sqrt(b**2-4*a*c)
    x2 = b-math.sqrt(b**2-4*a*c)
    return x1,x2
x1,x2 = equacao_2grau(2,10,6)
print("x1 é:",x1)
print("x2 é:",x2)
print('\n''\n')




#10
print("Função que retorne 4% do valor aplicado")
def saldo_rendimento(saldo):
    rendimento = saldo*0.04
    return rendimento
print("Rendimento de 4% do valor é :",saldo_rendimento(1000))
print('\n''\n')



#11
print("Função para calcular rendimentos")
def calc_rendimento(valor,pl):
    lucro = (valor*pl)/100
    rendimento = lucro/10
    return rendimento
print("O rendimento será:",calc_rendimento(800,5))
print('\n''\n')




#12
print("Função p/ inverter um valor númerico composto por centena, dezena, e unidade")
def inversor(v):
    centena = v//100
    rest = v%100
    dezena = rest//10
    unidade = rest%10
    calculo = (unidade*100)+ (dezena*10)+(centena)
    return calculo
print("O valor invertido é:",inversor(756))
print('\n''\n')



#13
print(" Função que calcule a conta de luz ")
def calculo_energia(kw,salario):
    calculo = (((salario/7)*kw)/100)
    return calculo
print("O valor da conta de luz é:",calculo_energia(120,1000))
print('\n''\n')



#14
print("Função p/ calcular a diagonal de um retângulo, fornecidos comprimento e largura")
def diagonal_retangulo(com,larg):
    calculo = (math.sqrt(com**2)+larg**2)
    return calculo
print("A diagonal do retângulo é:",diagonal_retangulo(3,6))
print('\n''\n')



#15
print("Função que calcula descontos p/ clientes")
def desconto_clientes(preco,desconto):
    desconto =  preco-((desconto/100)*preco)
    return desconto
print("O valor do desconto é:",desconto_clientes(500,10))
print('\n''\n')



#16
print(" Conversor de Centígrados/Fahrenehit")
def termometro(c):
    f = (9*c+180)/5
    return f
print("O valor em Fahrenheit é:",termometro(35))
print('\n''\n')



#17
print("Calcular quantidade de litros de combustível gastos")
def gasto_combustivel(tempo,velocidade):
    tempo_hora = tempo/60
    distancia = tempo_hora*velocidade
    litros = distancia/12
    return litros
print("Combustivel gasto é :",gasto_combustivel(20,40))
print('\n''\n')



#18
print("Calcular gorjeta do garçom")
def calculo_gorjeta(vgasto):
    calculo = vgasto/100
    gorjeta = calculo*10
    return gorjeta
print("O valor da gorjeta é:",calculo_gorjeta(500))
print('\n''\n')


#19A
print("Conversor de km/m ")
def convert_km_em_m(km):
    calculo = km*1000
    return calculo
print("O valor de km para metros é:",convert_km_em_m(5))
print('\n''\n')


#19B
print("Conversor de g/kg")
def convert_g_em_kg(g):
    calculo = g/1000
    return calculo
print("O valor de gramas para Kg é:",convert_g_em_kg(100))
print('\n''\n')


#19C
print("Conversor de cm/m")
def convert_cm_em_m(cm):
    calculo = cm/100
    return calculo
print("O valor de cm para metros é:",convert_cm_em_m(100))
print('\n''\n')


#19D
print("Conversor de cm/polegadas")
def convert_cm_em_pol(cm):
    calculo = cm/2.54
    return calculo
print("O valor de cm em polegadas é:",convert_cm_em_pol(30))
print('\n''\n')

 
#20
print("Calcular a potência de iluminação,através das dimenções em metros de um cômodo")
def calc_potencia_comodos(l1,l2):
    calculo = (l1*l2)*18
    return calculo
print("A potência de iluminação será:",calc_potencia_comodos(4,5),"W")
print('\n''\n')



#21
print("Receba o valor em hora, minuto, segundo, e retorne o valor em segundos")
def retorne_valor_segundos(h,m,s):
    total_s = h*3600
    total_s = total_s + m*60
    total_s = total_s + s
    return total_s
print("Valo em segundos:",retorne_valor_segundos(1,40,10))
print('\n''\n')


#22
print("Receba o valor em segundos e retorne em horas,minutos,segundos")
def relogio(s):
    hora = s//3600
    resto_hora = s%3600
    minutos  = resto_hora//60
    segundos = resto_hora%60
    return hora, minutos, segundos
print("Valor em h,m,s:",relogio(6010))

    





      




























































