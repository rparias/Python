#sintaxis => nombreDiccionario = {elem1, elem2...}
#este diccionario almacenara paises y capitales
miDiccionario={"Alemania":"Berlin",23:"Goodman","Ecuador":11, "Espana":"Madrid"}

#imprimir todo el diccionario
print(miDiccionario)

#busca a su respectivo valor asociado
print(miDiccionario["Ecuador"])

#agregar elemento a diccionario
miDiccionario["Bolivia"]="Lima"
print(miDiccionario)

#modificar un dato, por ejemplo el erroneo de arriba
miDiccionario["Bolivia"]="La Paz"
print(miDiccionario)

#eliminar un elemento
del miDiccionario["Espana"]
print(miDiccionario)


miTupla=("España","Francia","Peru","Argentina")
miDiccionario={miTupla[0]:"Madrid", miTupla[1]:"Paris",miTupla[2]:"Lima",miTupla[3]:"Buenos Aires"}
print(miDiccionario["Peru"])


#guardar una tupla en un diccionario en anillos
miDiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(miDiccionario)
print(miDiccionario["Equipo"])
print(miDiccionario["anillos"])


#guardar un diccionario dentro de otro diccionario
miDiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario["anillos"])


#devuelve las claves principales de cada elemento
print(miDiccionario.keys())
#devuelve los valores de cada elemento
print(miDiccionario.values())
#devuelve la longitud del diccionario
print(len(miDiccionario))