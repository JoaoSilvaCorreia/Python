"""
    Descrição: Lista de exercícios - Repetição por contagem
    Autor: João Vitor 
    Data: 02/04/2016
"""



import math


#1A 
print("numeros 1 a 100")
def numeros_um_a_cem():
    for numeros in range(1,101):
        print(numeros)
numeros_um_a_cem()
print('\n''\n')






#1B
print("pares de 10 a 50")
def numeros_pares_10_a_50():
    for numeros in range(10,51,2):                  
        print(numeros)
numeros_pares_10_a_50()
print('\n''\n')






#1C
print("impares de 10 a 50 ")
def numeros_impares_10_a_50():
    for numeros in range(11,51,2):
        print(numeros)
numeros_impares_10_a_50()
print('\n''\n')





#1D
print("numeros de 20 a 0 ")
def numeros_20_a_0():
    for numeros in range(20,-1,-1):
        print(numeros)
numeros_20_a_0()
print('\n''\n')




#1E
print("somar números de 3 a 10")
def somar_numeros_tres_a_dez():
      soma = 0
      for valor in range(3,11):
              soma = soma + valor
      return soma
print("O resultado da soma é:",somar_numeros_tres_a_dez())
print('\n''\n')





#1F
print("somar numreos pares de 4 a 20")
def somar_pares():
    soma = 0
    for valor in range(4,21,2):
            soma = soma+valor
    return soma
print("O resultado da soma é :",somar_pares())
print('\n''\n')






#1G
print("somar numeros impares de 10 a 15")
def somar_impares():
    soma = 0
    for valor in range(11,16,2):
            soma = soma+valor
    return soma
print("O resultado da soma é:",somar_impares())
print('\n''\n')




#1H
print("multiplicar numeros no intervalo fechado de 2 a 5")
def multiplicar_intervalo():
    multi = 1
    for valor in range(2,6):
        multi = multi + valor
    return multi
print("O resultado da multiplicação é:",multiplicar_intervalo())
print('\n''\n')





#1I
print("calcular media, numeros 1 a 10")
def media_um_a_dez():
    soma = 0
    cont = 0
    for valor in range(1,11):
        soma = soma+valor
        cont = cont+1
        media = soma/cont
    return media
print("A media será :",media_um_a_dez())
print('\n''\n')




#1J
print("calcular media,impares de 10 a 50")
def media_impares():
    soma = 0
    cont = 0
    for valor in range (11,51,2):
        soma = soma + valor
        cont = cont+2
        media = soma/cont
    return media
print(" a media será : ",media_impares())
print('\n''\n')




#1K
print("calcular media , divisiveis por 5, no intervelo de 10 a 50")
def media_divisiveis_por_cinco():
    div = 5
    cont =50
    for media in range(10,50,5):
        div = div/media
        cont = cont+5
        media = div /cont
    return media
print("a media será:",media_divisiveis_por_cinco())
print('\n''\n')




#2
print("imprimir tabuada ,numero qualquer")
def tabuada_sete():
    print("Tabuada do 7")
    for valor in range(11):
        calculo = valor*7
        print("7 x",valor,"=",calculo)
tabuada_sete()
print('\n''\n')




#3
print("Tabuada do 1 ao 9")
def tabuada(num):
    print("tabuada do", num)
    for valor in range(11):
        calculo = valor*num
        print(num, "x",valor,"=",calculo)
        
def tabuada_do_1_ao_10():
    for num in range(1,11):
        tabuada(num)

tabuada_do_1_ao_10()
print('\n''\n')


#4
print("saldo poupança de janeiro/2011 = R$1500, até janeiro/2012 = ?, com juros de 0.5% ao mês")
def saldo_rendimento():
    saldo = 1500
    juros = 0
    for valor in range (1,13):
        juros = saldo*0.5
        saldo = saldo + juros
        rendimento_poupanca = saldo + juros
        print("O rendimento  será:",rendimento_poupanca)
saldo_rendimento()
print('\n''\n')



#5
print("Calculo rendimento aplicação bancária")
def aplicacao_bancaria(vi,pl,dmeses):
    print("valor inicial:", vi)#para ver a mecanica dos meses(opcional)
    for mes in range(dmeses):
        vi = vi+vi*(pl/100)
        print("valor:",vi)#para ver a mecanica dos meses(opicional)
    return vi
valor = aplicacao_bancaria(1000,5,4)
print("Rendimento da aplicação:", valor)    
print('\n''\n')


#6
print("Função para imprimir o quadrado e a raiz quadrada, em intervalo numérico")
def quadrado_e_raiz_quadrada_com_intervalo_n():
    for valor in range (1,9):
        quadrado = valor**2
        raiz = math.sqrt(valor)
        print('\n')
        print("O quadrado de",valor,"será","=",quadrado)
        print("A raiz será de",valor,"será","=",raiz)
quadrado_e_raiz_quadrada_com_intervalo_n()
print('\n''\n')




#7
print("Tabela de conversão de cm/polegadas, valores de 1 á 100")
def centimetros_em_polegadas():
    for valor in range(1,101):
        conversao = valor*0.393701
        print(valor,"cm em polegadas será:",conversao)
centimetros_em_polegadas()
print('\n''\n')





#8 
print("Função que imprima os números naturais menores que o valor inteiro/positivo fornecido na entrada")
def numeros_naturais_menores_que_v(num):
    cont = 0
    for valor in range(num,0,-1):
        print(valor)    
numeros_naturais_menores_que_v(8)
print('\n''\n')




#9
print("Imprimir os 10 primeiros termos da série Fibonacci:")
def funcao_fibonacci():
     ultimo = 1
     penultimo = 0
     print(penultimo)
     print(ultimo)
     for valor in range(8):
         aux = ultimo
         ultimo = ultimo+penultimo
         penultimo = aux
         print(ultimo)
funcao_fibonacci()
print('\n''\n')





#10
print("Função que receba valor N , e retorne valor H")
def funcao_que_receba_n_retorne_h(n):
    h = 0
    for valor in range(1,n):
        h = h+(1/valor)
    return h
v = funcao_que_receba_n_retorne_h(10)
print("valor de H:",v)   
    
    

    
    
















        
      
    
      
























