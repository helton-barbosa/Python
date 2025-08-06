# Precedência entre os operadores aritméticos - do maior para o menor
# 1. () -> Parênteses internos tem precedência maior
# 2. **
# 3. *,  /,  //,  %
# 4. +,  -
conta_1 = 1 + 1 ** 5 + 5 # Saída: 7
conta_2 = (1 + 1) ** 5 + 5 # Saída: 37
print(conta_1)
print(conta_2)

