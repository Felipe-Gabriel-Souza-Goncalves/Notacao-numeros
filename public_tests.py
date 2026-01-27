from main import *

# TESTES PARA FILTRAR STRING

# Todos esperados que retorne 2000
print(filterStringNum(2000))
print(filterStringNum(-2000))
print(filterStringNum("2000"))
print(filterStringNum("2.000"))
print(filterStringNum("-2.0.0.0"))
print(filterStringNum("+.2.0..0..0   "))

# TESTES COM NÚMEROS MAIORES + NECESSIDADE DE FILTRO

# Input ideal
print(transformNum(25643454)) # Esperado: 25.6 milhões

# Strings
# negativo
print(transformNum("-67234526373")) # Esperado: -67.2 bilhões
# com notações
print(transformNum("200.265.764.834")) # Esperado: 200.2 bilhões
# formato incorreto
print(transformNum('9.2.6.2.7.9.2.1')) # Esperado: 92.6 milhões
# espaços desnecessários
print(transformNum('  486753905729098762457904143144      ')) # Esperado: 486.7 octilhões

# Número grande demais
print(transformNum(123000000000000000000000000000000000000000000000)) # Esperado: 123.0e45