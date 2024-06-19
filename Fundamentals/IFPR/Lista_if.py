"""
    Descrição: Lista de exercícios - Condicional
    Autor: João Vitor Da Silva Correia
    Data: 13/04/2016
"""



#if = se
#else = então
#elif = senão se


#1A
print("Retornar numero maior entre dois numeros:")
def retornar_maior_entre_dois_numeros(n1,n2):
    if n1>n2:
       return n1
    else:
        return n2
print(retornar_maior_entre_dois_numeros(1,3))
print('\n''\n')



#1B
print("verifcar se n é par:")
def verificar_n_par(n):
    if  n % 2 == 0:
        return "O número é par"
    else:
        return "O número não é par"
print(verificar_n_par(4))
print('\n''\n')


#1C
print("verifcar se n é impar:")
def verificar_n_impar(n):
    if n % 2 == 1:
        return "O numero é impar"
    else:
        return "O numero não é impar"
print(verificar_n_impar(6))
print('\n''\n')



#1D
print("Retornar valor absoluto:")
def valor_absoluto(n):
    if n<0 :
        return n*(-1)
    else:
        return n
print(valor_absoluto(-5))
print('\n''\n')


#1E
print("Verificar se dois numeros sao iguais:")
def verificar_se_numeros_sao_iguais(n1,n2):
    if n1 == n2:
        return "Os números são iguais"
    else:
        return "Os  números não são iguais"
print(verificar_se_numeros_sao_iguais(5,6))
print('\n''\n')




#1F
print("Verificar se duas palavras são iguais:")
def verificar_se_palvras_sao_iguais(p1,p2):
    if p1==p2:
        return "As palavras são iguais"
    else:
        return "As palavras não são iguais"
print(verificar_se_palvras_sao_iguais("a","b"))
print('\n''\n')




#1G
print("Verificar se um número é divisivel por 2 e por 10:")
def n_divisivel_por_dois_e_dez(n):
    if(n%2==0) and (n%10==0):
        return  "Número é divisivel por 2 e por 10"
    elif(n%2==0):
        return"Número é divisivel por 2"
    elif(n%10==0):
        return "Número é divisivel por 10"
    else:
        return "Número não é divisivel por 2 e por 10"
print(n_divisivel_por_dois_e_dez(7))
print('\n''\n')



#1H
print("Verificar se um número é divisivel por 11 ou por 13:")
def n_divisivel_por_onze_e_treze(n):
    if(n%11==0):
        return"Número é divisivel por 11"
    elif(n%13==0):
        return"Número é divisivel por 13"
    else:
        return "Número não é divisivel por 11 e por 13"
print(n_divisivel_por_onze_e_treze(11))
print('\n''\n')





#2
print("Função que indique a taxa de correção para um dado valor aplicado:")
def taxa_correcao(valor):
    if(valor <= 2000):
        return "Taxa será de 10%"
    elif (valor >= 2000) and (valor <= 5000):
        return "Taxa será de 12%"
    else :
        return "Taxa será de 13%"
print(taxa_correcao(2000))
print('\n''\n')


#3
print("Função que verifique  se 3 medidas podem constituir um triângulo:")
def tres_medidas_triangulo(a,b,c):
    if(b > a+c) or (a > b+c) or (c > a+b):
        return "nao é triangulo"
    else:
        return " é triangulo"
print(tres_medidas_triangulo(10,40,20))
print('\n''\n')



#4 
print("Função que analise os lados de um triângulo  e retorne sua classificação:")
def tipo_triangulo(a,b,c):
    if (a==b==c):
        return "Equilatero"
    if(a==b)or(a==c)or(b==c):
        return "Ísoceles"
    if(a!=b)and(b!=c)and(a!=c):
        return "Escaleno"
print(tipo_triangulo(9,10,15))
print('\n''\n')



#5
print("Função que  calcule o novo salário a partir do salário final:")
def calc_novo_salario(salario):
    if(salario <=1200):
        aumento = salario*10/100
        return salario + aumento
    if(salario > 1200)and (salario <=3000):
        aumento = salario*7/100
        return salario + aumento
    if (salario >3000) and (salario <= 8000):
        aumento = salario*3/100
    elif(salario > 8000):
        return salario
print(calc_novo_salario(1300))
print('\n''\n')



#6 Dúvidas
print("Verifique se número é palindromo:")
def palindromo(n):
    variavel1 = n%100
    sobra = n//100
    dezena = sobra%10
    unidade = sobra//10
    variavel2 =(unidade*10)+dezena
    if(variavel2 == variavel1):
        return True
    return False
print( palindromo(9119))
print('\n''\n')    




#7
print("Calcule a média final e o resultado.")
def media_final(n1,n2,n3):
    media = (n1+n2+n3/3)
    if(media >=70):
        return print("Média:",media,"Aluno Aprovado!")
    if(media<50<70):
        return print("Média:",media,"Aluno de Recuperação!")
    elif (media<50):
        return print("Média:",media,"Aluno Reprovado!")
media_final(80,70,90)
print('\n''\n')





#8
print("Função que receba três números reais e retorne o menor:")
def n_reais(n1,n2,n3):
    if(n1<n2) and(n1<n3):
        return n1
    elif(n2<n1)and(n2<n3):
        return n2
    elif(n3<n1) and(n3<n2):
        return n3
print(n_reais(9.58,19.19,7.15))
print('\n''\n')





#9
print("Calculo da multa:")
def calc_multa(vmaxi,vmoto):
    if(vmoto==vmaxi+10):
        return"Pagar R$50"
    elif(vmoto>=vmaxi+11)and(vmoto<=vmaxi+30):
        return "Pagar R$100"
    else:
        return "Pagar R$200"
print(calc_multa(40,50))
print('\n''\n')


#10
print("Receba 3 valores e imprima em ordem crescente")
def valores_crescente(a,b,c):
    if(a>b)and(b>=c):
        return(c,b,a)
    elif(b>=a)and(b>c)and(a>=c):
        return(c,a,b)
    elif(b>a)and(b>=c)and(a<=c):
        return(a,c,b)
    elif(b>a)and(b<=c):
        return(a,b,c)
    elif(b<a)and(a<c):
        return(b,a,c)
    elif(b<c)and(c<=a):
        return(b,c,a)
    else:
        return(a,b,c)
print(valores_crescente(100,101,99))
print('\n''\n')


#11
print("Calcular e retornar quociente do primeiro pelo segundo:")
def quociente(n1,n2):
    div = n1//n2
    if(div):
        return(div)
    else:
        return "Divisão por zero"
print(quociente(10,2))
print('\n''\n')


#12 
print("Equação do segundo grau")
def equacao_2grau(a,b,c):
   delta1 = +b**2-4*a*c
   delta2 = -b**2-4*a*c
   if (delta1<0):
        return "Não há Solução real"
   elif(delta1==0):
        return delta1
   elif(delta1>0):
        return delta1,delta2
print(equacao_2grau(1,10,4))
print('\n''\n')



#13 - muitas duvidas
print("Receba 4 números inteiros e calcule a soma dos que forem par")
def calc_soma_pares(n1,n2,n3,n4):
    if(n1%2==0)and(n2%2==0)and(n3%2==0)and(n4%2==0):
        return n1+n2+n3+n4
    
    elif(n1%2==0)and(n2%2==0)and(n3%2==0)and(n4%2==1):
         return n1+n2+n3

    elif(n1%2==0)and(n2%2==0)and(n3%2==1)and(n4%2==1):
        return n1+n2

    elif(n1%2==0)and(n2%2==1)and(n3%2==0)and(n4%2==1):
        return n1+n3
   
    elif(n1%2==1)and(n2%2==0)and(n3%2==0)and(n4%2==0):
        return n2+n3+n4
    
    elif(n1%2==1)and(n2%2==1)and(n3%2==0)and(n4%2==0):
        return n3+n4
    
    elif(n1%2==1)and(n2%2==1)and(n3%2==1)and(n4%2==0):
        return n4
    
    elif(n1%2==1)and(n2%2==1)and(n3%2==1)and(n4%2==1):
        return "Não são pares"
print(calc_soma_pares(2,2,2,2))
print('\n''\n')



#14
print("Verificar se ano é bissexto:")
def bissexto(ano):
    if(ano%400==0)or(ano%4==0)and(ano%100!=0):
        return print(ano,"é bissexto")
    else:
        return print(ano,"não é bissexto")
bissexto(2016)
print('\n''\n')



#15 - dúvidas
print("idade")
def calc_idade(diaN,mesN,anoN,diaAT,mesAT,anoAT):
    idade = anoAT - anoN
    meses = mesN - mesAT
    dias = diaAT - diaN
    if(anoAT > anoN):
        return idade
    else:
        return "Data invalída"
print(calc_idade(7,11,1998,7,11,2016))
print('\n''\n')






#16
print("Função que receba 2 valores e um simbolo, e efetue os calculos:")
def operacao_matemat(v1,v2,simb):
    if(simb=="+"):
        soma = v1+v2
        return print(v1,"+",v2,"=",soma)
    elif(simb=="-"):
        subtracao = v1-v2
        return print(v1,"-",v2,"=",subtracao)
    elif(simb=="*"):
        vezes = v1*v2
        return print(v1,"*",v2,"=",vezes)
    else:
        divisao = v1/v2
        return print(v1,"/",v2,"=",divisao)
operacao_matemat(8,2,"+")
print('\n''\n')





#17




#18
print("Resolver equação:")
def calc_equacao(a,b,c):
    equacao = a**2 + b + c
    if(a!=0)and(b!=0)and(c!=0):
        return equacao
    elif(a==0)and(b==0)and(c==0):
        return "Equação sem solução"
    elif(a==0)or(a==0)and(b==0):
        return equacao
print(calc_equacao(5,4,2))
print('\n''\n')




#19
print("Conversor de Moedas")
def conversor_moedas(reais,cambio):
    if(cambio=="dólar"):
        dolar = reais/3.5387
        return print("R$",reais,"->","US$",dolar)
    
    elif(cambio=="euros"):
        euro = reais/3.9932
        return print("R$",reais,"->","€",euro)
    
    elif(cambio=="libras"):
        libra = reais/5.0267
        return print("R$",reais,"->","£",libra)
    else:
        return"Impossível realizar conversão com essa moeda"
conversor_moedas(10,"euros")
print('\n''\n')




#20
print("Receba um número e retorne o mês:")
def retorne_mes(numero):
    if(numero==1):
        return "Janeiro"
    elif(numero==2):
        return "Fevereiro"
    elif(numero==3):
        return "Março"
    elif(numero==4):
        return "Abril"
    elif(numero==5):
        return "Maio"
    elif(numero==6):
        return "Junho"
    elif(numero==7):
        return "Julho"
    elif(numero==8):
        return "Agosto"
    elif(numero==9):
        return "Setembro"
    elif(numero==10):
        return "Outubro"
    elif(numero==11):
        return "Novembro"
    elif(numero==12):
        return "Dezembro"
    else:
        return "Mês invalido"
print(retorne_mes(11))
print('\n''\n')




#21
print("Receba letra e retorne classificação:")
def alfabeto(letra):
    if(letra=="A")or(letra=="E")or(letra=="I")or(letra=="O")or(letra=="U"):
        return print(letra,"é vogal")
    else:
        return print(letra,"é consoante")
alfabeto("A")
print('\n''\n')





#22
print("Peso ideal:")
def informe(nome,sexo,altura):
    if(sexo=="masculino"):
        homen=(72.7*altura)-58
        return print(nome,"seu peso ideal é :",homen)
    elif(sexo=="feminino"):
        mulher=(62.1*altura)-44.7
        return print(nome,"seu peso ideal é :",mulher)
informe("João","masculino",1.73)
print('\n''\n')



#23
print("Consumo  de combústivel em litros:")
def consumo(km,combustivel):
    A=km/8
    D=km/5
    G=km/14 
    if(combustivel=="Álcool"):
       return A        
    elif(combustivel=="Diesel"):
        return D        
    elif(combustivel=="Gasolina"):
        return G
    else:
        return"Combústivel invalido"
print(consumo(14,"Gasolina"))
print('\n''\n')


    
  
#24
print("Função que verifica se a data é valida ou não:")
def verific_data(dia,mes,ano):
    if(dia<=31) and(mes<=12) and(ano>750):
        print(dia,"/",mes,"/",ano)
        return"É valida"
    else:
        print(dia,"/",mes,"/",ano)
        return "Não é valida"
print(verific_data(7,11,1998))
print('\n''\n''\n')




#25
print("Dose do remedio conforme idade e peso:")
def dosagem(idade,peso):
    if(idade>12)and(peso==60)or(peso>60):
      #1000mg = 2ml = 40 gotas
        dose = 1000/500*20
        return print(dose,"gotas")
    
    elif(idade>12)and(peso<60>24):
      #875mg = 1,75ml = 35 gotas
        dose = 875/500*20
        return print(dose,"gotas")
    
    elif(idade<12)and(peso>24):
      #750mg = 1,5ml = 30 gotas
        dose = 750/500*20
        return print(dose,"gotas")
    
    elif(idade<12)and(peso>16.1<24):
       #500mg = 1ml = 20 gotas
        dose = 500/500*20
        return print(dose,"gotas")
    
    elif(idade<12)and(peso>9.1<16):
        #250mg = 0,5ml = 10 gotas
        dose = 250/500*20
        return print(dose,"gotas")
    
    elif(idade<12)and(peso>5<9):
        #125mg = 0,25ml = 5 gotas
        dose = 125/500*20
        return print(dose,"gotas")
    else:
        return "invalido"
dosagem(10,6)









    


        
    
    






