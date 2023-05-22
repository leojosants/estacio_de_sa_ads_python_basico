print("\nEXEMPLO 01")

def multiplicador(numero):
    A = 2 # esta variável tem escopo local
    print(f"Dentro da função, A variável vale: {A}")
    return A * numero

A = 3 # esta variável tem escopo global
B = multiplicador(5)
print(f"Fora da função, A variável a vale: {A}")


print("\nEXEMPLO 02")

def multiplicador2(numero):
    return C * numero

C = 3 # esta variável tem escopo global
D = multiplicador2(5)
print(f"A variável B vale: {D}")


print("\nEXEMPLO 03")

def multiplicador3(numero):
    global E # todas as referências à variável E são para E global
    E = 2      # E global será alterado
    print(f"Dentro da função,  variável E vale: {E}")
    return E * numero

E = 3  # esta variável tem escopo global
F = multiplicador3(5)
print(f"A variável F vale: {F}")
print(f"Fora da função, a variável A vale: {E}")
