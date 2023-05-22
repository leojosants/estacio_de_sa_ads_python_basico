"""
    calcular e informar o IMC (índice de massa corpórea) do usuário, que deverá fornecer seu peso e sua altura. 
    Lembre-se de que o IMC é calculado pela fórmula: IMC=peso/altura
"""

nome = input("\nNome: ")
peso = eval(input("Peso [kg]: "))
altura = eval(input("Altura [m]: "))

imc = peso / (altura ** 2)

print(f"\nNome: {nome} | Peso: {peso}kg | Altura: {altura}m | IMC: {imc} \n")