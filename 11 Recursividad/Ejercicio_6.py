#1 2 3 4
def suma_digitos(n):
    if n < 10: # Si es menor a 2 digitos no se va a sumar con nada.
        return n # Devuelve el mismo numero
    
    ultimo_digito = n % 10 
    numero_recortado = n // 10
    print(ultimo_digito, " ", numero_recortado)

    return ultimo_digito + suma_digitos(numero_recortado) #Sumo el ultimo digito + el ultimo digito del numero recortado

print(suma_digitos(1234))
