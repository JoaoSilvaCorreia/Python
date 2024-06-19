class Data:
	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

class Pessoa:
	def __init__(self, cpf, nome, dn):
		self.cpf = cpf
		self.nome = nome
		self.dn = dn

def leitura():
	lista = []
	for i in range(1):
		cpf = input("Digite o CPF: ")
		nome = input("Digite o nome: ")
		data = input("Digite a data de nascimeto (Ex.: dd/mm/AAAA): ")
		dn = transforma_string_em_data(data)
		pessoa = Pessoa(cpf, nome, dn)
		lista.append(pessoa)
	return lista

def transforma_string_em_data(data_str):
	dia = int(data_str[:2])
	mes = int(data_str[3:5])
	ano = int(data_str[6:])
	data = Data(dia, mes, ano)
	return data

def transforma_data_em_string(data):
	dia = str(data.dia)
	mes = str(data.mes)
	ano = str(data.ano)
	data_final = dia + "/" + mes + "/" + ano
	return data_final

def calcula_idade(data_atual, data_nasc):
	anos = data_atual.ano - data_nasc.ano
	if data_atual.mes > data_nasc.mes:
		anos = anos + 1
	elif data_atual.mes == data_nasc.mes:
		if data_atual.dia <= data_nasc.dia:
			anos = anos + 1
	return anos

def media_idade():
	lista = leitura()
	data_atual = Data(21,6,2016)
	soma = 0
	for pessoa in lista:
		soma = soma + calcula_idade(data_atual,pessoa.dn)
	media = soma / len(lista)
	return media


def grava_registros(lista):
	# abre par escrita o arquivo
	arquivo = open("registros.txt", "w")

	for pessoa in lista:
		# transforma em string
		linha = str(pessoa.cpf) + " | " + pessoa.nome + " | " + transforma_data_em_string(pessoa.dn)

		# grava linha por linha no arquivo
		arquivo.write(linha + "\n")

	#fecha o arquivo
	arquivo.close()

def le_registros_arquivo():
        lista = []

        arquivo = open("registros.txt", "r") #abre para leitura
        linhas = arquivo.readlines() # lê todas as linhas
        arquivo.close() # fecha o arquivo

        for linha in linhas:
                linha = linha.rstrip() #elimina todos os espaços e \n do arquivos
                #print (linha)
                if linha != "":
                        lista_campos = linha.split("|") #split divide uma linha com base no pipe (quebra os campos das strings)
                        #cria um registro pessoa
                        dtnasc = transforma_string_em_data(lista_campos[2])
                        pessoa = Pessoa(lista_campos[0], lista_campos[1],dtnasc)
                        lista.append(pessoa)
        return lista
                        
                        


def main():
	lista_pessoas = leitura()
	grava_registros(lista_pessoas)



def main2():
        lista_pessoas = le_registros_arquivo()
        for pessoa in lista_pessoas:
                print("CPF: ", pessoa.cpf)
                print("Nome: ", pessoa.nome)
                print("Data de Nascimento: ", transforma_data_em_string(pessoa.dn))
                print("--------------------------------------------------------------")
