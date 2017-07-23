print("Programa de evaluacion de notas")
nota=input("Ingrese nota: ")

def evaluar(nota):
	valoracion=""
	if nota<5:
		valoracion="suspenso"
	elif nota<7:
		valoracion="con las justas"
	else:
		valoracion="PASASTE!"

	return valoracion

print(evaluar(int(nota)))