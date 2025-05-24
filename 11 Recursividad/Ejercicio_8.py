# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
# y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero < 10 and numero == digito: # Si el numero ya no se puede recortar pero es igual al digito
        return 1
    elif numero < 10: # Si el numero ya no se puede recortar y es distinto al digito
        return 0
    
    num_recortado = numero // 10 # recorto el numero para "recorrerlo"
    digito_obtenido = numero % 10 # obtengo el ultimo digito a comparar

    if digito_obtenido == digito: # comparo el digito obtenido con el digito pasado como parametro
        return contar_digito(num_recortado, digito) + 1 # sumo si hay coincidencia
    else:
        return contar_digito(num_recortado, digito)

print(contar_digito(31223, 3))