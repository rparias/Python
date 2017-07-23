#sintaxis => nombreTupla = (elem1, elem2...)
miTupla=("Ronald","Gabby",6,2,2010)
print(miTupla[1])

#convertir a lista una tupla
miLista=list(miTupla)
print(miLista)

#convertir a tupla una lista
miTupla=tuple(miLista)
print(miTupla)

#devuelve true si es q encuentra
print("Ronald" in miTupla)

#devuelve el numero veces que se repite un elemento
print(miTupla.count(2010))

#longitud de la tupla, cantidad de elementos
print(len(miTupla))

#desempaquetar una tupla para cada variable en el mismo orden
novio, novia, dia, mes, anio=miTupla
print(novio)
print(novia)
print(dia)
print(mes)
print(anio)