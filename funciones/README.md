# funciones
matematicamente una funcion es una ioperacion que toma uno o mas valores llamados a argumentos y produce un valor denominado resultado
# FUNCIONES
matematicamente una funcion es una operacion 
que toma uno om mas valores llamados argumentos
y produce un valor denominado resultado.
f(x)=x/1+x**2
>[!NOTE]
>todos los lenguajes de programacion tienen 
funciones incorporadas (funciones internas), y funciones creadas por el usuario (fuciones externas)
en programacion una funcion es un subprograma, es una estrutura que nos permite agrupar codigo y sus principales objetivos son 
-no repetir fragmetos de codigos 
-reutilizar el codigo en distitos esenarios 
## estrutura de una funcion
una funcion viene definida por un nombre, k sus parametros y su valor de retorno.
una vez creada la funcion podemos solcitar su ejecucion 'invocado' la funcion por su 'nombre'
## definir una funcion en python
para definir una funcion en python primero utilizaremos la palabra reservada def seguida por el nombre de la funcion. a continuacion especificaremos los parametros con (si) es una funcion sin parametros (a) si es una funcion con parametros, si se tuviera mas de un parametro iran separados por ,, finalizremos con linea :, en la siguiente linea sin olvidar el identado, comenzara el cuerpo de la funcion (micro programa) que puede contener 1 o mas sentencias, finalmente devera retornar un resultado con la palabra reservada return.
[!tip]
como retorno tambien se puede utilizar la funcion interna, print, para depuracion de codigo no es recomendable usarlo en produccion.
*ejemplo:*
python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    reurn f"{saludo}, {saludo_dos}"
    #print(f"{saludo}, {saludo_dos}")
print(saludo())

### invocar una funcion
para invocar una funcion solom tendremos que escribir el nombre de la funcion seguido () parentesis.
python
def saludo():
    print("hola")

#invocando la funcion
saludo()

## retornar un valor
las funciones pueden retornar (o devolver) un valor.
python
def uno():
    return 1
uno()

> [!WARNING]
> no confundir print() con return,. el valor retornado por return nos permite usarlo fuera de su contexto. y print solo mostrara el literal por terminal.
*ejemplo*
*en el archivo lecture.py
## retornando multiples valores
el secreto es necesario hacerlo mediante un tipo de
```python
def varios():
    return 2,3,4
varios()
#retona(2,3,4)
def lista():
    return["hola",45]
#retona["hola",45]
def dicc():
    return("nombre","jose","edad":45)
dicc()
#retona ("nombre","jose","edad":45)
dicc()
´´´´
## Parámetros y argumentos.
si una funcion no dispusiera de valores  de entrada estaria limitada en su actuacion.
Es por ello ´parametros´ no permiten variar los datos que consume una funcion para obtener distintos resultados
** ejemplo**
* crear una funcion que recibe un valor numerico y retorna su raiz cuadrada*
´´´python
def sqrt(valor):
    return valor **(1/2)
    ##NOTA en este caso , el valor 4 es un argumento de la funcion
    sqrt(4)
    ´´´
    cuando llamamos a un funcion con ´argumentos´, los valores de estos argumentos se copian en los correspondientes ´parametros´ dentro de la funcion. 
    ´´´´ python
    def ejm(a,b,c):
        return a,b,c
        ejm(4,5,6):
´´´´
### Argumentos nominales 
En esta aproximacion los argumentos no son copiados en un orden especifico sino que 
*** se asignan por nombre a cada parametro**.
Ello nos permite evitar el problema de conocer o recordar cual es el orden de los parametros en la difinicion de la funcion. para utilizarlo, basta con realizar una asignacion de cada argumento en la propia llamada a la funcion
**ejemplo**
´´´python
def build_cpu(familia,num_core_frecuencia):
    print(f"""
    la cpu es de la familia {familia},
    con {num_core} cores y con una 
    frecuencia de {frecuencia}
""")
## haciendo uso de argumentos posiciones  
build_ cpu("intel",4,2.7)
´´´
### parametros por defecto
Es posible especificar **vlores por defecto** en los parametros de una funcion, en el caso de que no se proporcione un valor al argumento en la llamada a la funcion, en el parametro correpondiente tomara el valor defenido por defecto.
**ejemplo**
´´´python
def alumnos(nom,app,estado):

    alumnos("ruth","castillo")
    alumnos("antony","crucez","desaprobado")
´´´



 ### Desempaquetados/Empaquetado de argumetos(tarea)
Desempaquetar y empaquetar argumentos son conceptos comunes en programacion, especialmente en lenguajes como python.

*- Empaquetar argumentos*** : consiste en agrupar múltiples argumentos en una sola variable para pasarlos a una función de manera más conveniente.Por ejemplo, en Python, se pueden empaquetar argumentos en una tupla o un diccionario y luego pasar una estructura de datos a una función.

*- Desempaquetar argumentos*** : Por otro lado, desempaquetar argumentos significa tomar una estructura de datos que contiene múltiples valores (como una dupla o un diccionario) y pasar esos valores como argumentos individuales a una función. Esto es útil cuando se nesecita pasar múltiples argumentos a una función que espera argumentos separados.

En python,el desempaquetado de argumentos se puede realizar utilizando el operador  `* ` para desempaquetar una tupla o una lista, o ` ** ` para desempaquetar un diccionario.
 
Por ejemplo, en Python, si tenemos una función que espera tres argumentos  funcion(a, b, c) , y tenemos una tupla con esos valores ` (1, 2, 3)` , podemos desempaquetar los valores de la tupla y pasarlos como argumentos a la función de la siguiente manera:  funcion(*tupla) .

### Funciones internas python(tarea) 
Python tiene una variedad de funciones internas (built-in functions) que están disponibles para su uso sin necesidad de importar módulos adicionales. Aquí tienes algunos ejemplos de funciones internas de Python:

print(): Imprime un mensaje en la consola o en la salida estándar.
* len(): Devuelve la longitud de un objeto, como una cadena, lista o diccionario.
* type(): Devuelve el tipo de un objeto.
* input(): Lee una zentrada del usuario desde la consola.
* range(): Genera una secuencia de números dentro de un rango especificado.
* int(): Convierte un valor en un entero.
* float(): Convierte un valor en un número de punto flotante.
* str(): Convierte un valor en una cadena.
* list(): Convierte un objeto iterable en una lista.
* dict(): Crea un nuevo diccionario.

Estas son solo algunas de las funciones internas más comunes en Python, pero hay muchas más disponibles. 
Recuerda que las funciones internas son parte del lenguaje Python y están disponibles para su uso directo sin necesidad de importar módulos adicionales.

Return devuelve valores que podré hacer uso.
## Crear una función que retorne el número 10, y muestre por terminal si es par.
# Siempre que el valor que retorne mi función se utilize en más sentencias u operaciones hacer uso de return.
def diez():
    return 10
if diez()%2==0:
    print("Es par")
else:
    print("Es impar")
# Print solo muestra por terminal.
# 
#
# # Return cuándo queremos que nuestra función devuelva o retorne un tipo de dato o un tipo de dato estructurado.
# Crear una función que me muestre el producto de dos números.
def producto(a,b):
    return a*b

# Crear una función que me retorne una lista de tres números.
def lista_números():
    return{2,3,4}

# Crear un función que por parámetro reciba un nombre y retorne un mensaje de bienvenida con el nombre.
def mensaje(nombre):
    print(f"hola, {nombre}, bienvenido") 

# Crear una función que reciba por parámetro una lista de números y me devuelva el número menor,mostrar 
# por terminal el valor retornando por la función.
lista=[4,3,6,8]
def min(l):
    minimo=1[0]
    for n in l:
        if n < minimo:
            minimo=n
        return minimo
print(min(lista))

# Crear una función que reciba como parámetro el nombre y la edad de una persona, mi función deberá retornar un diccionario con los datos ,luego 
# mostrar por terminal el valor de retorno de mi función.
nombre="Yuliza"
edad=19
def persona(nombre,edad):
    return{"nombre":nombre,
           "edad":edad
           }
print(persona(nombre,edad))

##funcion internasde paython (tarea
-int()
-float()
##tipos de3 funciones
## funciones (funciones lambda)
una funcion que no tiene nombre
## funcion clusure
que una funcion que dentro tiene una funcion
## funciones de collaback
reciben por parametro otro funcion 

## programacion funcional 
no requiere que yo sepa lo que el programa
"""python
### programacion interactiva 
lista=[5,7,8,4,1]
def num_menimo(1):
    menimo=l[0]
    for n in  l: 
        if n < minimo:
            minimo=n
            return minimo
            ## programacion funcional
            min(lista)

            #### averiguar sobre map(),filter(),reduce()

       #### tarea 
       
        *MAP():*

La función *map()* en Python es una función integrada que se utiliza para aplicar una función dada a cada elemento de un iterable (como una lista, tupla, etc.) y devuelve un iterador que contiene los resultados. La sintaxis general de la función map() es la siguiente :
python
map(funcion, iterable)

* funcion: Es la función que se aplicará a cada elemento del iterable.
* iterable: Es el iterable (lista, tupla, etc.) al que se aplicará la función.
  
Aquí tienes un ejemplo básico de cómo se utiliza la función map():
python
# Definir una función para duplicar un número
def duplicar(x):
    return x * 2

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Utilizar la función map() para duplicar cada número en la lista
resultado = map(duplicar, numeros)

# Convertir el resultado a una lista
resultado_lista = list(resultado)

print(resultado_lista)  # Output: [2, 4, 6, 8, 10]

En este ejemplo, la función duplicar(x) duplica un número dado. Luego, utilizamos la función map() para aplicar la función duplicar a cada elemento de la lista numeros. El resultado es un iterador que contiene los números duplicados. Al convertir este iterador en una lista, obtenemos una lista con los números duplicados.

*FILTER()*

La función filter() en Python es una función integrada que se utiliza para filtrar elementos de un iterable (como una lista, tupla, etc.) según una función de filtro dada. La función filter() devuelve un iterador que contiene los elementos para los cuales la función de filtro devuelve True. La sintaxis general de la función filter() es la siguiente:

python
filter(funcion_filtro, iterable)

* funcion_filtro: Es la función que se utiliza para evaluar cada elemento del iterable. Debe devolver True o False.
* iterable: Es el iterable (lista, tupla, etc.) del cual se desean filtrar los elementos.
* 
Aquí tienes un ejemplo básico de cómo se utiliza la función filter():

python
# Definir una función para filtrar números pares
def es_par(x):
    return x % 2 == 0

# Crear una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utilizar la función filter() para filtrar los números pares de la lista
resultado = filter(es_par, numeros)

# Convertir el resultado a una lista
numeros_pares = list(resultado)

print(numeros_pares)  # Output: [2, 4, 6, 8, 10]

En este ejemplo, la función es_par(x) evalúa si un número dado es par. Luego, utilizamos la función filter() para filtrar los números pares de la lista numeros. El resultado es un iterador que contiene solo los números pares. Al convertir este iterador en una lista, obtenemos una lista con los números pares.


La función filter() es útil cuando se desea filtrar elementos de un iterable basado en una condición específica.

 Puede ser utilizada en combinación con funciones lambda para operaciones de filtrado rápidas y eficientes.

*REDUCE()*

La función reduce() en Python se encuentra en el módulo functools y se utiliza para aplicar una función de manera acumulativa a los elementos de un iterable, de izquierda a derecha, de manera que los elementos se reducen a un solo valor. La función reduce() requiere al menos dos argumentos: la función a aplicar y el iterable sobre el cual se aplicará la función. La sintaxis general de la función reduce() es la siguiente:
python
functools.reduce(funcion, iterable)

* funcion: Es la función que se aplica de manera acumulativa a los elementos del iterable.
* iterable: Es el iterable (lista, tupla, etc.) sobre el cual se aplicará la función de reducción.
* 
Es importante tener en cuenta que a partir de Python 3, la función reduce() se ha movido al módulo functools, por lo que primero debes importarla antes de poder utilizarla.

 Aquí tienes un ejemplo básico de cómo se utiliza la función reduce() para encontrar el producto de una lista de números:
 python
 from functools import reduce

# Definir una función para multiplicar dos números
def multiplicar(x, y):
    return x * y

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Utilizar la función reduce() para encontrar el producto de los números
resultado = reduce(multiplicar, numeros)

print(resultado)  # Output: 120 (1 * 2 * 3 * 4 * 5)

En este ejemplo, la función multiplicar(x, y) se utiliza para multiplicar dos números. Luego, utilizamos la función reduce() para aplicar esta función de manera acumulativa a los elementos de la lista numeros, lo que nos permite encontrar el producto de todos los números en la lista.

La función reduce() es útil cuando se desea realizar operaciones acumulativas en una secuencia de elementos y reducirlos a un solo valor. Puede ser una herramienta poderosa para ciertas operaciones matemáticas y de reducción de datos.

    


 



