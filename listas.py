#sintaxis => nombreLista = [elem1, elem2...]
miLista=["Ronald","Gabby","Erick","Noemi","Pepe"]
#[:] imprime toda la lista
print(miLista[:])
#[1] imprime un elemento de la posicion
print(miLista[1])
#[-2] imprime desde el ultimo elemento hacia la izq desde -1
print(miLista[-2])
#[0:3] imprime una porcion de la lista de 0 a 3 con 3 excluido
print(miLista[0:3])
#[:3] imprime una porcion de la lista de 0 a 3 con 3 excluido
print(miLista[0:3])
#[2:] imprime una porcion de la lista desde 2do indice
print(miLista[2:])

#agregar elementos a la lista al final
miLista.append(78.32)
print(miLista[:])

#agregar elementos a la lista a posicion especifica
miLista.insert(3,"Diana")
print(miLista[:])

#agregar varios elementos a la lista
miLista.extend(["Moises",True])
print(miLista[:])

#saber el indice de un elemento
print(miLista.index("Pepe"))

#devuelve true si encuentra un elemento
print("Noemi" in miLista)
print("Maria" in miLista)

#eliminar elementos
miLista.remove("Diana")
print(miLista[:])

#eliminar ultimo elemento de la lista
miLista.pop()
print(miLista[:])

#sumar otra lista, concatenar
miLista2=["Azul","Rojo"]
miLista3=miLista+miLista2
print(miLista3[:])

#repetidor de una lista
print(miLista2[:]*3)