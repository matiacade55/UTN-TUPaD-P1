# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva 
#    su representación en binario como una cadena de texto.

def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return str(decimal_a_binario(num // 2)) + str(num % 2)

# Funcion a parte para devolver correctamente el cero.  
def convertir_a_binario(num):
    if num == 0:
        return "0"
    return decimal_a_binario(num)

print(convertir_a_binario(10))