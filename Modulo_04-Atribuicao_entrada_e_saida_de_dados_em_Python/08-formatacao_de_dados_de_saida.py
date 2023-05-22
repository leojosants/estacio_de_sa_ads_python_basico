hora = 10
minutos = 26
segundos = 18

print('\n' + str(hora) + ':' + str(minutos) + ':' + str(segundos))
print('{}:{}:{}'.format(hora, minutos, segundos))
print(f'{hora}:{minutos}:{segundos}')

primeiroNumero = 10
segundoNumero = 100

print(f'{primeiroNumero}, {segundoNumero}')
print(f'{primeiroNumero:4}, {segundoNumero:5}') # Delimitando o comprimento da impressão

print('{:8.5}'.format(10/3))

# Impreesão de sequencia
sequencia = [0, 1, 2]
print(sequencia)

# Substring
str = 'Hello World'
print(f'str = {str}')
print(f'str[0:4] = {str[0:4]}')
print(f'str[2:8] = {str[2:8]}')
print(f'str[::-1] = {str[::-1]}')    # sentido oposto
print(f'str[8:2:-1] = {str[8:2:-1]}')

print('\n')