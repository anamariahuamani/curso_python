# este es el script principal"""
import mayor_edad

def es_menor(lista:list):

    """funcion para saber el numero menor de una lista"""
    menor=lista[0]
    for n in lista:
         if n <menor:
            menor=n
    return menor
        
    

def es_mayor(lista:list): 
    """función para saber el número mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n > mayor:
             mayor=n
        return mayor
    
def cuenta_vocales(text:str):
    """funcion para contar la cantidad de voacles a que aparecen en un texto"""
    text_minusculas:str=text.lower()
    cantidad_vocales=0
    for n in text_minusculas:
        if n == "a":
            cantidad_vocales+=1
    return cantidad_vocales        
    
mayor_edad.funcion_mayor_edad(20)
print(es_menor([4,8,10,2,3,4,5]))
print(cuenta_vocales("mi mama mima yo amo a mi mama "))

""" este es el script principasl"""
import mayor_edad
import es_menor
import es_menor
import cuenta_vocal
mayor_edad.funcion_mayor_edad(20)
print(es_mayor.f_es mayor([7,4,2,1,0,8]))
print(es_menor.f_es menor([7,4,5,2,3,0]))
print(cuenta_vocal).f_cuenta_vocales("mi mama mima yo amo a mi mama")



                                    
    



      