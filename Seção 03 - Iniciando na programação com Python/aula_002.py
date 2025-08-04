# A função print() é uma das funções mais utilizadas e fundamentais em Python.
# Sua principal finalidade é exibir é exibir informações na tela (ou em outro
# local).
# Sintaxe: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# *objects - representa um ou mais objetos que se deseja imprimir.
# sep - especifica como os objetos serão separados, por padrão ' '.
# end - especifica o que será impresso no final da linha, por padrão '\n'.
# file - permite que seja redirecionado a saída da função para um arquivo em
# vez da tela.
# flush - é um booleano que especifica se a saída deve ser descarregada
# (forçada a ser escrita) imediatamente. O valor padrão é False, o que
# significa que a saída é armazenada em um buffer e escrita em lotes.

# \r\n --> CRLF
# \n ----> LF
print(12, 34, 1011, sep="-", end='##')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

