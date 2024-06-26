# return devuelve valores que podre hacer uso 
# crear un funcion que retorne el nombre 10 y muestre por terminal si es par
# siempre que el valor que mi funcion se utiliza en mas sentensias u operaciones hacer uso de return 
def dies():
    return 10
if diez()%2==0:
    print("es par") 
else:
    print("es impar")
    # print solo muestra por terminal

# return cuando queremos que nuestra funcion devuelva o retorne un tipo de dato  o un tipo de dato estructurado
# crear una funcion que me muestre el producto de dos numeros
def producto(a,b):
    return a*b

# crear una funcion que me retorne una lista de tres numeros
def lista_numeros():
    return [3,2,6]

#print usaremos cada vez que nuestra funcion retorne un mensaje   .....

# crear una funcion que por parametro reciba un nombre y retorno un mensaje de bienvenida con el nombre.
def mensaje (nombre):
    print(f"hola,) {nombre},bienvenido al chongo")
    mensaje()

    ## crear una funcion que reciba como parametro el nombre y la edad de una persona mi funcion debera retornar una diccion con los datos luego mostrar por terminal el valor de retorno de mi funcion
    lista=[4,3,6,78,7]
    def min(1):
        minimo=1[0]
        forn n in l:
        if n <minimo:
            minimo=n
            return minimo
        print(min(lista))

        ## crear una funcion que reciba como parametro el nombre y la edad de una persona mi funcion debra retornar un diccionario con los
        datos juego 
        # mostrar por terminal el valor de retorno de mi funcion
        return {
            "nombre":nom,
            "edad":edad
        }
       return dict(
           nombre=nom,
           edad=edadgit stastus

           24/06/2024
           ###EJEMPLOS DE LAMBDA
           saludo=lambda n,a:f"hola, [n] , [a]"
           print(saludo("ruth","catillo"))
           
           #crear un programa anonimo que reciba como parametro una liasta de de 5 numeros y retorne dos listas una con los numeros pares y otra con numeros pares
           y otro con numeros impares
           
        lista=[4,7,5,3,47,2,10,8]
        pares=lambda l:[n for n in lista if   n%2==0]
         impares=lambda l:[n for n in lista if   n%2!=0]
         print(pares(lista))
         print(impares(lista))

       ## funcion collaback  
def mensaje(m)
  rint(m)
def pedir_nombre ():
    nombre=input("ingresa tu nombre")
    return nombre
    mensaje(pedir_nombre())

    ### MAP
    lista =[4,7,8,5,2]
    map(lambda x:x+1,lista))  # pedir defecto retorna una lista
    print(nueva_lista)
    #tengo una lista de alumnos que todos ellos aprobaron y pasan al tercer semestre, 
    ## problema en mi lista todos estan con el segundo semestre por lo que tendremos que crear una solucion que cambie anthonny el campo de semes tre  de2 a 3

    "nombre":"abel",
    "edad":36,
    "semestre":2

"nombre":"antony",
"edad":40,
"semestre":2
},
{
"nombre":"edith",
"edad":50,
"semestre":2
},
alumnos_actualizados=list(map(lambda el:el["semestre"]+1,lista_alumnos))
print(semestre_actualizados)



