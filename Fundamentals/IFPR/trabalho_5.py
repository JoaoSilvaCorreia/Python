"""
    NOME : VDSOUG
    MESTRE PROFESSOR : CHARLES
    DATA: 27/06/2016

"""
import os
def trabalho():
    comando  = " "
    while comando != "SAIR" : # laço de repetiçao
        comando = input(">>> ") # comomando a ser execultado
        cha = comando.split(" ",10) # converte o texto para um vetor
        if len(cha) <= 2: # analiza as chamdads de sistemas
            if cha[0] == "SAIR": # comando para sair do programa
                break
            elif cha[0] == "DATA":# analiza as chamdads de sistemas
                os.system("date /t") # comando para mostra a Data do sistema

            elif cha[0] == "HORA":# analiza as chamdads de sistemas
                os.system("time /t") # comando para ver a hora do sistema

            elif cha[0] == "VER":# analiza as chamdads de sistemas
                os.system("ver ") #comando pra ver a versao do seu sistema

            elif cha[0] == "LIMPAR":# analiza as chamdads de sistemas
                os.system("cls ") # coamndo para limpar a tela

            elif cha[0] == "LISTAR":# analiza as chamdads de sistemas
                if len(cha) < 1: 
                    os.system("dir ")# comando para listar diretorio ou pasra do python
                else:
                    os.system("dir " + cha[1] + " * ")# comando para listar uma determinada pasta ou arquivo
            elif cha[0] == "AJUDA":
                print ("CRIAR    \t\t para criar um diretorio ou arquivo \n\t\t\t para CRIAR -d pasta_1\n \t\t\t para criar -a arquivo_1\n")
                print ("INSERIR  \t\t para inserir um texto em um arquivo. \n\t\t\t INSERIR \"texto 1 ...\" arquivo_1\n")
                print ("LISTAR   \t\t para listar arquivos e diretorios da pasta. \n\t\t\t LISTAR\n")
                print ("APAGAR   \t\t para apagar um arquivo ou diretorio. \n\t\t\t APAGAR -A \"arquivo\" -D \"Diretorio\" pasta_1\n")
                print ("RENOMEAR \t\t para renomear um arquivo ou diretorio. \n\t\t\t RENOMEAR pasta_2  pasta_3\n")
                print ("MOVER    \t\t para mover um arquivo ou diretorio. \n\t\t\t MOVER pasta_1 pasta_2\n")
                print ("DELETAR  \t\t para deletar um arquivo ou diretorio. \n\t\t\t DELETAR -A \"arquivo\" -D \"Diretorio\" pasta_1 pasta_2\n")
                print ("AJUDA    \t\t para imprimir o texto AJUDA\n")
                print ("VER      \t\t para imprimir na tela a versao do sistema.\n")
                print ("DATA     \t\t para imprimir na tela a data do sistema\n")
                print ("HORA     \t\t para imprimir na tela a hora do sistema\n")
                print ("LIMPAR   \t\t para limpar a tela \n")
                print ("SAIR     \t\t para finalizar o sistema\n")

            else:
                print("comando invalido -> digite AJUDA para abrir o menu de opçoes")

        elif len(cha) > 2:# comando para criar diretorio ou arquivos.
            if cha[0] == "CRIAR":
                if cha[1] == "-D":# comando para criar diretorio.
                    os.system("mkdir " + cha[2])
                elif cha[1] == "-A":# comando para criar arquivos.
                    os.system("echo > " + cha[2] + ".txt")

            elif cha[0] == "DELETAR" or cha[0] == "APAGAR":# commando para apagar um  arquivos ou pastas
                if cha[1] == "-D":# comando para apagar diretorio.
                    os.system("rmdir " + cha[2])
                elif cha[1] == "-A": # comando para apagar arquivos.
                    os.system("del " + cha[2])

            elif cha[0] == "MOVER":#comando para mover um arquivo ou diretorio existente
                os.system("move " + cha[1] + " " + cha[2])

            elif cha[0] == "RENOMEAR":#comando para renomear um arquivo ou diretorio existente.
                os.system("ren " + cha[1] + " " + cha[2])

            elif cha[0] == "INSERIR":#comando para inserir um texto dentro de um arquivo existente.
                os.system ("echo >> " + cha[1] + " " + cha[2])
                
        else:
            print("comando invalido -> digite AJUDA para abrir o menu de opçoes")

trabalho()

             


            
                
        
