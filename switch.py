salarioPresidente=input("Introduce salario presidente: ")
print("Salario del Presidente: "+str(salarioPresidente))

salarioDirector=input("Introduce salario director: ")
print("Salario del Director: "+str(salarioDirector))

salarioJefeArea=input("Introduce salario jefe de area: ")
print("Salario del Jefe de Area: "+str(salarioJefeArea))

salarioAdministrativo=input("Introduce salario administrativo: ")
print("Salario del Administrativo: "+str(salarioAdministrativo))

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")