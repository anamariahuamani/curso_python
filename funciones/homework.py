## crear una funcion que reciba por argumento n numeros y retorna una lista con los numeros pares 

#def numeros_pares(n):
#    return [num for num in range(1, n + 1) if num % 2 == 0]

# Ejemplo de uso de la función
# n = 10
# resultado = numeros_pares(n)
# print(resultado)

## crear tres funciones para los siguiente casos
# calcular el numero menor 
# calcular el numero mayor
# calcular la suma de todos los numeros 
# se la pasara por argumneto n numeros 


# Función para calcular el número menor
#def numero_menor(*args):
#    menor=arsg[0]
#    for n in args:
#        if n<menor:
#            menor=n
#   return menor
# Función para calcular el número mayor
#def numero_mayor(*args):
#    mayor=arsg[0]
#    for n in arsg:
#        if>mayor:
#            mayor=n
#    return mayor

# Función para calcular la suma de todos los números
#def suma_numeros(*args):
#    suma=arsg[0]
#    for n in arsg:
#        if+suma:
#            suma +=n
#    return suma

# Ejemplo de uso de las funciones
#numeros = [10, 5, 20, 8, 15]
#print(numero_menor(*numeros))
#print(numero_mayor(*numeros))
#print(suma_numeros(*numeros))


tarea 24/06/2024
### crear una lista de alumnos con los siguientes campos
# nombre, apellido,edad,celular,email
## 1. actualizar los registros con un campo mas todas tendran el campoi de programa de estudios de enfermeria
# 2. buscar el segundo registro y actualizar su edad a 50 años

Crear una lista de alumnos con los campos solicitados
alumnos = [
    {"nombre": "ana", "huamani": "ayquipa", "edad": 25, "celular": "987654321", "email": "anamariahuamaniayquipa23.com", "programa_estudios": "Enfermería"},
    {"nombre": "María", "apellido": "Garcia", "edad": 30, "celular": "987654322", "email": "mariahuamani ayquipa23.com", "programa_estudios": "Enfermería"},
    {"nombre": "Pedro", "apellido": "Lopez", "edad": 35, "celular": "987654323", "email": "anamariahuamaniayquipa23.com", "programa_estudios": "Enfermería"},
]

# Buscar el segundo registro y actualizar su edad a 50 años
if len(alumnos) >= 2:
    alumnos[1]["edad"] = 50

# Imprimir la lista de alumnos actualizada
for alumno in alumnos:
    print(alumno)