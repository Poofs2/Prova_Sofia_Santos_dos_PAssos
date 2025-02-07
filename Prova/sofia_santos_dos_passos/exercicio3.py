"""
Exercício 03 – Profundidade Máxima de Listas Aninhadas (Recursividade) - (tempo aproximado 15 a 20 min)

Objetivo:
Crie uma função recursiva chamada `max_depth` que receba uma lista e retorne a profundidade máxima de aninhamento de sublistas.

Requisitos:
1. Se a lista não contiver nenhuma sublista, retorne 1.
2. Se houver sublistas, a profundidade da lista será 1 + a maior profundidade encontrada entre as sublistas.
3. Considere que apenas elementos do tipo lista devem ser tratados como níveis de aninhamento.

Exemplos:
    - max_depth([1, 2, 3]) deve retornar 1.
    - max_depth([1, [2, 3], 4]) deve retornar 2.
    - max_depth([1, [2, [3, 4]], 5]) deve retornar 3.

Dicas:
    - Utilize a função `isinstance(x, list)` para verificar se um elemento é uma lista.
    - Percorra cada elemento da lista e, se for uma sublista, chame recursivamente a função `max_depth`.

Escreva sua solução abaixo.
"""
# Sua solução aqui.

# --- Function ---
def max_depth(array):
    counter = 0
    for n in array:
        if isinstance(n, list) == True:
            counter += 1
            return max_depth(array[:-1])
        else:
            return 1
# --- Function ---

# --- Main Code ---
print(max_depth([1, 2, 3]))
print(max_depth([1, [2, 3], 4]))
print(max_depth([1, [2, [3, 4]], 5]))
# --- Main Code ---

