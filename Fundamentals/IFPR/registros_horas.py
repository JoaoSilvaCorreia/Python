class Horario:
	def __init__(self, horas, minutos, segundos):
		self.horas = horas
		self.minutos = minutos
		self.segundos = segundos

def transf_horas_segundos(horario):
	segundos = horario.horas * 3600
	segundos = segundos + horario.minutos * 60
	segundos = segundos + horario.segundos
	return segundos

#---------------Teste - Início ---------------
h = Horario(5,34,21)
v = transf_horas_segundos(h)
print("Transforma horas em segundos: ", v)
#---------------Teste - Fim ---------------

def somar_horarios(h1, h2):
	h_novo = Horario(0,0,0)
	h_novo.horas = h1.horas + h2.horas
	h_novo.minutos = h1.minutos + h2.minutos
	if h_novo.minutos > 60:
		h_novo.minutos = h_novo.minutos%60
		h_novo.horas = h_novo.horas + 1
	h_novo.segundos = h1.segundos + h2.segundos
	if h_novo.segundos > 60:
		h_novo.segundos = h_novo.segundos%60
		h_novo.minutos = h_novo.minutos + 1
	
	return h_novo

#---------------Teste - Início ---------------
h1 = Horario(2,45,12)
h2 = Horario(4,23,54)
h_novo = somar_horarios(h1,h2)
print("Somar horários: ")
print("Horas: ", h_novo.horas)
print("Minutos: ", h_novo.minutos)
print("Segundos: ", h_novo.segundos)
#---------------Teste - Fim ---------------

def le_horario():
	horario = input("Digite o horário na forma hh:mm:ss")
	horas = int(horario[:2])
	minutos = int(horario[3:5])
	segundos = int(horario[6:])
	h = Horario(horas,minutos,segundos)
	return h

#---------------Teste - Início ---------------
h_novo = le_horario()
print("Ler Horário: ")
print("Horas: ", h_novo.horas)
print("Minutos: ", h_novo.minutos)
print("Segundos: ", h_novo.segundos)
#---------------Teste - Fim ---------------

def exibir_horario(h):
	horario = str(h.horas)
	horario = horario + ":" + str(h.minutos)
	horario = horario + ":" + str(h.segundos)
	print(horario)

#---------------Teste - Início ---------------
print("Exibir Horário: ")
exibir_horario(h_novo)
#---------------Teste - Fim ---------------
