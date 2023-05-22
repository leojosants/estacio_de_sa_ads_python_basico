# Atribuição multipla

A, B = 1, 2

print('\nAntes da troca')
print(f"Valor das variáveis: A={A} e B={B}")

# Primeira troca
temp = A
A = B
B = temp

print('\nPrimeira troca')
print(f"Valor das variáveis: A={A} e B={B}")

# Segunda troca
A, B = B, A
print('\nSegunda troca')
print(f"Valor das variáveis: A={A} e B={B}")
