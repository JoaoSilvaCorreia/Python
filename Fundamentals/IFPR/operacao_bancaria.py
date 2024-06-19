class Conta:
      def __init__(self,propietario,num_conta,senha,saldo):
              self.propietario = propietario
              self.num_conta = num_conta
              self.saldo = saldo
              self.senha = senha

from datetime import datetime

def info():
      print('\n')
      print("||| CAIXA ECONÔMICA FEDERAL |||\n")
      Conta.saldo = 0
      Conta.propietario = str(input("Digite o nome do propietario: "))
      Conta.num_conta = str(input("Digite o número da sua conta: "))
      Conta.senha = input("Digite sua senha: ")
      vag = Conta.propietario.split(" ",10)
      print("\nBem - Vindo",vag[0],"!\n")
      print("Para Finalizar Digite","(SAIR)")
     
      

      


def menu():
      print("Operações: 1 --> Depositos | 2 --> Saques | 3 --> Extratos | 4 --> Saldos")
      opcao = input("Selecione a operacão desejada (1 | 2 | 3 | 4 |): ")
      if(opcao == "1"):
            deposit()
            sair()
      elif(opcao == "2"):
            saq()
            sair()
      elif(opcao == "3"):
            extrato()
            #menu()
            sair()
      elif(opcao == "4"):
            saldo()
            sair()
      elif(opcao == "SAIR"):
            sair()
            
      else:
            print("Operação Incorreta ! ")
            menu()

def deposit():
      deposito = float(input("Insira o valor a ser depositado R$: "))
      Conta.saldo = Conta.saldo + deposito
      print("Operação Realizada com Sucesso ! \n")

      


def saq():
      saque = float(input("Insira o valor a ser sacado R$: "))
      if(saque > Conta.saldo):
            print("Saldo Insuficiente !")
            
      else:
            Conta.saldo = Conta.saldo - saque
            print("Operação Realizada com Sucesso ! \n")
            

def saldo():
      print('\n')
      print("||| CAIXA ECONÔMICA FEDERAL |||\n")
      print("    Titular:",Conta.propietario)
      print("    Conta:",Conta.num_conta)
      print("    Saldo Atual:",Conta.saldo)
      print("\n||| Para mais informações ligue | SAC - 0800 726 0101 |||")
      print("||| Ou acesse nosso site | www.caixa.gov.br |||\n")
     


def extrato():
      now = datetime.now()
      print('\n')
      print("||| CAIXA ECONÔMICA FEDERAL |||\n")
      print("    Extrato Atualizado |","Data:",now.day,"/",now.month,"/",now.year,"| Hora:",now.hour,":",now.minute,":",now.second)
      print("    Usúario:",Conta.propietario,"| Conta:",Conta.num_conta)
      print("    Saldo Atual:",Conta.saldo)
      print("\n||| Para mais informações ligue | SAC - 0800 726 0101 |||")
      print("||| Ou acesse nosso site | www.caixa.gov.br |||\n")
      #gravar()



def gravar():
      arquivo = open("operacao.txt","w")
      texto = ((Conta.propietario)  + "|"+ float(Conta.num_conta) +"|"+(Conta.saldo))
      arquivo.write(texto+"\n")
      arquivo.close()



def ler():
      arquivo = open("operacao.txt",'r')
      texto = arquivo.read()
      print(texto)
      arquivo.close()
      
 
      
def sair():
      nova = input("Deseja realizar outra  operação ? (A --> SIM | B --> NÃO ): ")
      if(nova == "A"):
            return menu()
      else:
            print("Obrigado !")
            exit()
def main():
      info()
      menu()
      #gravar()
main()
