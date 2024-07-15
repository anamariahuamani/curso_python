n Python, el operador de módulo se denota con el símbolo de porcentaje (%). El operador de módulo devuelve el resto de la división entre dos números. Aquí tienes algunos ejemplos de cómo se utiliza el operador de módulo en Python:
 
1. Ejemplo básico de operador de módulo:
 
a = 10
b = 3
resultado = a % b
print(resultado)  # Esto imprimirá 1, que es el resto de la división de 10 entre 3
 
2. Usos comunes del operador de módulo:
 
- Verificar si un número es par o impar:
 

numero = 17
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

 
- Obtener el último dígito de un número:
 

 
numero = 456
ultimo_digito = numero % 10
print("El último dígito es:", ultimo_digito)

 
- Generar secuencias cíclicas:
 

secuencia = [1, 2, 3, 4, 5]
for i in range(10):
    elemento_actual = secuencia[i % len(secuencia)]
    print(elemento_actual)