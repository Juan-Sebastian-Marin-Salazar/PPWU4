
# 1.- Función que reciba un diccionario y agregar una clave-valor, 
# retornar el diccionario modificado (Debe agregarlo al final)
def agregar_diccionario(diccionario, clave, valor):
    print("Diccionario inicial:", diccionario)
    diccionario[clave] = valor  
    print("Diccionario modificado:", diccionario)
    return diccionario

# 2.- Función que reciba un diccionario y elimine una clave-valor, 
# retornar el diccionario modificado
def eliminar_diccionario(diccionario, clave):
    print("Diccionario inicial:", diccionario)
    if clave in diccionario:
        del diccionario[clave]
        print("Diccionario modificado:", diccionario)
    else:
        print("Clave no encontrada.")
    return diccionario


# 3.- Función que reciba un diccionario y modifique el valor de una clave, 
# retornar verdadero si pudo modificar y falso si no pudo
def modificar_diccionario(diccionario, clave, nuevo_valor):
    print("Diccionario inicial:", diccionario)
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        print("Diccionario modificado:", diccionario)
        return True
    else:
        print("Clave no encontrada.")
        return False

# 4.- Función que combine dos diccionarios, 
# regresar el diccionario resultante
def combinar_diccionarios(dic1, dic2):
    print("Diccionario 1:", dic1)
    print("Diccionario 2:", dic2)
    combinado = {**dic1, **dic2}
    print("Diccionario combinado:", combinado)
    return combinado

# 5.- Función que agregue elementos a un conjunto, 
# retornar verdadero si pudo agregar y falso si no pudo.
def agregar_conjunto(conjunto, elemento):
    print("Conjunto inicial:", conjunto)
    if elemento in conjunto:
        print("Elemento ya existente.")
        return False
    conjunto.add(elemento)
    print("Conjunto modificado:", conjunto)
    return True

# 6.- Función que elimine un elemento de un conjunto, 
# retornar verdadero si pudo eliminar y falso si no pudo
def eliminar_conjunto(conjunto, elemento):
    print("Conjunto inicial:", conjunto)
    if elemento in conjunto:
        conjunto.remove(elemento)
        print("Conjunto modificado:", conjunto)
        return True
    print("Elemento no encontrado.")
    return False

# 7.- Función que combine dos conjuntos, regresar el conjunto resultante
def combinar_conjuntos(conjunto1, conjunto2):
    print("Conjunto 1:", conjunto1)
    print("Conjunto 2:", conjunto2)
    combinado = conjunto1.union(conjunto2)
    print("Conjunto combinado:", combinado)
    return combinado

# 8.- Función que regrese la diferencia de dos conjuntos
def diferencia_conjuntos(conjunto1, conjunto2):
    print("Conjunto 1:", conjunto1)
    print("Conjunto 2:", conjunto2)
    diferencia = conjunto1.difference(conjunto2)
    print("Diferencia de conjuntos:", diferencia)
    return diferencia

# 9.- Función que agregue un elemento a una tupla y 
# lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def agregar_tupla(tupla, elemento):
    print("Tupla inicial:", tupla)
    nueva_tupla = tupla + (elemento,)
    print("Tupla modificada:", nueva_tupla)
    return nueva_tupla

# 10.- Función que elimine un elemento a una tupla 
# y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def eliminar_tupla(tupla, elemento):
    print("Tupla inicial:", tupla)
    if elemento not in tupla:
        print("Elemento no encontrado.")
        return tupla
    nueva_tupla = tuple(x for x in tupla if x != elemento)
    print("Tupla modificada:", nueva_tupla)
    return nueva_tupla

# 11.- Función que concatene dos tuplas en una nueva, 
# regresar la nueva tupla
def concatenar_tuplas(tupla1, tupla2):
    print("Tupla 1:", tupla1)
    print("Tupla 2:", tupla2)
    nueva_tupla = tupla1 + tupla2
    print("Tupla concatenada:", nueva_tupla)
    return nueva_tupla

# 12.- Función que revertir el orden de una tupla y 
# lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def revertir_tupla(tupla):
    print("Tupla inicial:", tupla)
    nueva_tupla = tupla[::-1]
    print("Tupla revertida:", nueva_tupla)
    return nueva_tupla

# 13.- Función que recibe un diccionario y lo imprime
def imprimir_diccionario(diccionario):
    print("Diccionario:", diccionario)

# 14.- Función que recibe un tupla y la imprime
def imprimir_tupla(tupla):
    print("Tupla:", tupla)

# 15.- Función que recibe un conjunto y lo imprime
def imprimir_conjunto(conjunto):
    print("Conjunto:", conjunto)


# Para probar
dicc = {"nombre": "Juan", "edad": 20}
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print("1.- Agregar a diccionario")
agregar_diccionario(dicc, "ciudad", "Mexico")
print(" ")
print("2.- Eliminar valor diccionario")
eliminar_diccionario(dicc, "edad")
print(" ")
print("3.- Modificar diccionario")
modificar_diccionario(dicc, "nombre", "Carlos")
print(" ")
print("4.- Combinar diccionarios")
combinar_diccionarios(dicc, {"profesion": "Ingeniero"})
print(" ")
print("5.- Agregar al conjunto")
agregar_conjunto(conjunto1, 4)
print(" ")
print("6.- Eliminar del conjunto")
eliminar_conjunto(conjunto1, 2)
print(" ")
print("7.- Combinar conjuntos")
combinar_conjuntos(conjunto1, conjunto2)
print(" ")
print("8.- Regresar diferencia")
diferencia_conjuntos(conjunto1, conjunto2)
print(" ")
print("9.- Agregar a una tupla")
agregar_tupla(tupla1, 7)
print(" ")
print("10.- Eliminar de tupla")
eliminar_tupla(tupla1, 2)
print(" ")
print("11.- Concatenar tuplas")
concatenar_tuplas(tupla1, tupla2)
print(" ")
print("12.- Revertir tuplas")
revertir_tupla(tupla1)
print(" ")
print("13.- Imprimir diccionario")
imprimir_diccionario(dicc)
print(" ")
print("14.- Imprimir tupla")
imprimir_tupla(tupla1)
print(" ")
print("15.- Imprimir conjunto")
imprimir_conjunto(conjunto1)

