"""
   Data: 22/06/2016
   Máteria: Registros-Atividade Livros

1 .Faça uma função para gravar registros Livro em arquivo texto.

"""





class Livros:
    def __init__(self,titulo,autor,area):
        self.titulo = titulo
        self.autor = autor
        self.area = area
       



def ajuda():
    print('\n')
    print("------------------------------")
    print("A --> Adicionar livro")
    print("B --> Remover livro")
    print("C --> Pesquisar livro título")
    print("D --> Pesquisar autor")
    print("E --> Listar todos livros")
    print("F --> Gravar coleção arquivo")
    print("G --> ler coleção arquivo")
    print("H --> Para sair do programa")
    print("------------------------------")
    print('\n')



def leitura():
    lista = []
    novo = "sim"
    while(novo == "sim"):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        area = input("Digite a aréa do livro: ")
        livro = Livros(titulo,autor,area)
        lista.append(livro)
        novo = input("Deseja registrar outro livro ? :")
    return lista






def remover():
    remov = input("Digite o livro para ser removido: ")
    for livro in lista_livros:
        if(remov == livro.titulo):
            del(remov)
        else:
            print("Livro não encontrado !")




def menu():
    opcao = input("Digite a opção desejada (A, B, C , D , E , F, G, H , AJUDA) : ")
    #while(opcao != "H"):
    for i in range(1):
        if(opcao == "AJUDA"):
            ajuda()
        elif(opcao == "A"):
            return leitura()
        elif(opcao == "B"):
            return remover()
        #elif(opcao == "C"):
            #return
        elif(opcao == "E"):
            return main2()
        #elif(opcao == "F"):
            
        elif(opcao == "H"):
            exit()
        else:
            print("Opcão Incorreta !")
        menu()
        
    
  
    

    
def grava_registros(lista):
    arquivo = open("registros_de_livros.txt", "w")
    for livro in lista:
        linha = str(livro.titulo + " | " + livro.autor + " | " + livro.area)
        arquivo.write(linha + "\n")

    arquivo.close()




def le_registros_arquivo():
    lista = []
    arquivo = open("registros_de_livros.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        #linha = linhas.rstrip()
        if linha!="":
            lista_campos = linha.split("|")
            livro = Livros(lista_campos[0],lista_campos[1],lista_campos[2])
            lista.append(livro)
    return lista


def main():
    menu()
    listass = menu()
    grava_registros(listass)


def main2():
    lista_livros = le_registros_arquivo()
    for livro in lista_livros:
        print("Título:",livro.titulo)
        print("Autor:",livro.autor)
        print("Area:",livro.area)



















































        
  



