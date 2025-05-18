# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
#    y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
#    para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / altura
    return imc

# Programa Principal

peso = float(input("Por favor, ingresá tu peso en kg: "))
altura = float(input("Por favor, ingresá tu altura en metros: "))

imc = calcular_imc(peso, altura)

# imc:.2f formatea el imc a un float de 2 decimales
print(f"Su Indice de Masa Corporal (IMC) es: {imc:.2f}")