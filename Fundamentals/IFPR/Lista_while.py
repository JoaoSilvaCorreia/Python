"""
    Descrição: Lista de exercícios - Repetição por condição 
    Autor: João Vitor 
    Data: 13/04/2016
"""



#1
print("Qual será a quantidade de anos que pop A ultrapasse ou iguale pop B")
def num_anos_A_ultrapasse_B(popa,txa,popb,txb):
    anos = 0
    while (popa<=popb):
        popa = popa+popa*txa
        popb = popb+popb*txb
        anos = anos+1
    return anos
valor = num_anos_A_ultrapasse_B(90000000,0.03,200000000,0.015)
print("qtde de anos =", valor)
print('\n''\n''\n''\n')





#2
print("Material radioativo")
def massa_material_radioativo(massa_i):
    print("Massa inicial:",massa_i)
    seg = 0
    while massa_i > 0.5: 
        seg = seg + 50
        massa_i = massa_i/2
    print("Massa final:",massa_i)
    hora = seg/3600
    minutos = seg/60
    seg = seg
    print("horas:",hora)
    print("minutos:",minutos)
    print("segundos:",seg)
    return seg
massa_material_radioativo(8796)
print('\n''\n''\n''\n')
    




#3
print("Função para determinar quando idade de Bob será o dobro da idade de Renata")
def idade_bob_renata(ibob,ire):
    anos = 0
    while(ibob > ire * 2 ):
        ibob = ibob+1
        ire  = ire+1
        anos = anos +1
    return anos
valor = idade_bob_renata(42,17)
print("qtde de anos será =",valor)
print('\n''\n''\n''\n')


#4
print("Quantidade de anos que idade de Didi igual a soma da idade dos filhos")
def idade_didi_igual_soma_idade_filhos(didi,filho1,filho2):
    anos = 0
    while(didi>filho1+filho2):
        didi = didi+1
        filho1 = filho1+1
        filho2 = filho2+1
        anos = anos+1
    return anos
valor = idade_didi_igual_soma_idade_filhos(52,10,12)
print("Quantidade de anos do didi séra :",valor)
print('\n''\n''\n''\n')



#5
print("Função quantidade de anos juca maior que chico")
def anos_juca_maior_chico(chico,cm1,juca,cm2):
    anos = 0
    while(juca<=chico):
        chico = chico+cm1
        juca = juca+cm2
        anos = anos+1
    return anos
valor = anos_juca_maior_chico(1.50,0.02,1.10,0.03)
print("Quantidade de anos séra :",valor)
print('\n''\n''\n''\n')



#6A
print("números de 1 a 100")
def numeros_um_a_cem():
     cont = 0
     while(cont<100):
         cont = cont+1
         print(cont)
     return cont
numeros_um_a_cem()
print('\n''\n''\n''\n')




#6B
print("pares de 10 a 50")
def numeros_pares_dez_a_cinq():
    cont = 10
    while(cont<50):
        cont = cont+2
        print(cont)
numeros_pares_dez_a_cinq()
print('\n''\n''\n''\n')


#6C
print("impares de 10 a 50")
def numeros_impares_dez_a_cinq():
    cont = 9
    while(cont<49):
        cont = cont+2
        print(cont)
numeros_impares_dez_a_cinq()
print('\n''\n''\n''\n')



#6D
print("numeros de 20 a 0")
def numeros_de_vinte_a_zero():
    cont = 21
    while(cont>0):
        cont = cont-1
        print(cont)
numeros_de_vinte_a_zero()
print('\n''\n''\n''\n')


#6E
print("somar números de 3 a 10")
def funcao_somar_tres_a_dez():
    cont = 3
    soma = 0
    while(cont<10):
        cont = cont+1
        soma = cont+soma
    return soma
v = funcao_somar_tres_a_dez()
print(v)
print('\n''\n''\n''\n')


#6F
print("somar pares de 4 a 20")
def funcao_somar_pares_de_quatro_a_vinte():
    cont = 4
    soma = 0
    while(cont<20):
        cont = cont+2
        soma = cont+soma
    return soma
v = funcao_somar_pares_de_quatro_a_vinte()
print(v)
print('\n''\n''\n''\n')



#6G
print("somar impares de 10 a 15")
def somar_impares_dez_a_quinze():
    cont = 10
    soma = 0
    while (cont<15):
        cont = cont+1
        soma = cont+soma
    return soma
v = somar_impares_dez_a_quinze()
print(v)
print('\n''\n''\n''\n')




#6H 
print("multiplicar números em intervalo fechado de 2 a 5")
def multiplicar_int_fechado():
     cont = 2
     mult = 1
     while (cont<5):
         cont = cont+1
         mult = mult*cont
     return mult
v = multiplicar_int_fechado() 
print(v)
print('\n''\n''\n''\n')




#6I 
print("Calcular média dos números de 1 a 10")
def calc_media_um_a_dez():
    cont = 1
    soma = 0
    while (cont<10):
        cont = cont+1
        soma = soma+cont 
    media = soma/cont
    return media
v = calc_media_um_a_dez()
print(v)
print('\n''\n''\n''\n')



#6J
print("Calcular média dos números ímpares de 10 a 50")
def calc_media_impares():
    cont = 11
    soma = 0
    while (cont<50):
        cont = cont+2
        soma = soma+cont
    media = soma/cont
    return media
v = calc_media_impares()
print(v)
print('\n''\n''\n''\n')




#6K
print("Calcular média  dos numeros divisiveis por 5 no intervalo de 10 a 50")
def media_div_por_cinco():
    cont = 10
    soma = 0
    while (cont<50):
        cont = cont+5
        soma = soma+cont
    media = soma/cont
    return media
v = media_div_por_cinco()
print(v)
print('\n''\n''\n''\n')        





#7
print("Função para exibir o resultado usando while e for = 10.0,11.1,12.2,13.3,,20.0")
def contagem_while():
    cont = 10.0
    print(cont)
    while(cont<20): 
        cont = cont+1.1
        print(cont)
contagem_while()
print('\n')

print("Usando for")
def contagem_for():
    cont = 10.0
    for valor in range(10):
        cont = cont+1.1
        print(cont)
contagem_for()
print('\n''\n''\n''\n')





#8
print("Função que receba dois numeros (A e B, onde a>b) e calcule o MDC")
def calc_MDC(a,b):
    while(a % b != 0):
        resto = a % b
        a = b
        b = resto
    return b
v = calc_MDC(48,30)
print("o valor do MDC é:",v)
print('\n''\n''\n''\n')



#9 dúvidas
print("Equação de Pell")
print('\n''\n''\n''\n')





#10
print("Faça uma função que receba n, onde n>=3, e calcule soma dos n primeiros termos fibonacci")
def fibonacci():
    penultimo = 0
    ultimo = 1
    print(penultimo)
    print(ultimo)
    while (ultimo<=10):
         aux = ultimo
         ultimo = ultimo+penultimo
         penultimo = aux
         print(ultimo)
fibonacci()
print('\n''\n''\n''\n')
        
        





















    










