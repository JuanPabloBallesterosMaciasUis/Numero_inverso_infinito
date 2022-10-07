# Ejercicio de suma de los dijitos

print("________________________________________")
print("|        Numero inverso infinito        |")
print("|_______________________________________|")
print("")

#input
n = int(input("Digite un numero entero positivo: "))
n0 = n
inverso = 0

if n>= 0:
    while n > 0:
        n1 = n%10
        inverso = (inverso * 10)+ n1
        n = n //10
        
    print("La inversa del numero",n0,"es",inverso)
else:
    print("Numero no valido")