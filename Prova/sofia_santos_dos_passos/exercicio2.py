"""
Exercício 02 – Analisador de Argumentos Numéricos  (tempo aproximado 15 a 20 min)

Objetivo:
Crie uma função chamada `analisar_argumentos` que receba um número arbitrário de argumentos utilizando *args e analise quais deles são números (int ou float). 
A função deve retornar um dicionário com as seguintes chaves:
    - 'maior': o maior número encontrado.
    - 'menor': o menor número encontrado.
    - 'media': a média de todos os números considerados.
    - 'quantidade': a quantidade de números válidos analisados.

Requisitos:
  - Argumentos que não sejam números devem ser ignorados.
  - Se nenhum número for passado, retorne um dicionário com 'maior', 'menor' e 'media' iguais a None e 'quantidade' igual a 0.
  - Utilize estruturas condicionais e funções built-in como isinstance() para verificar os tipos.

Exemplo de uso:
    resultado = analisar_argumentos(10, "texto", 5.5, 3, [1,2], 8)
    print(resultado)
    # Saída esperada (exemplo): {'maior': 10, 'menor': 3, 'media': 6.125, 'quantidade': 4}
    
Dica: Use isinstance(x, (int, float)) para testar se x é numérico.
"""
# Sua solução aqui
from functools import reduce
# --- Function ---
def analisar_argumentos(array):
    array_num = []
    for item in array:  
     if isinstance(item, (int, float)) == True:
        array_num.append(item)
    maior = menor = array_num[0]
    for x in array_num:
      if maior <= x:
       maior = x
      if menor >= x:
       menor = x

      media = reduce(lambda x, y: x + y, array_num) / len(array_num)
      qnt = len(array_num)
    return {
        'maior': maior,
        'menor': menor,
        'media': media,
        'quantidade': qnt
    }
# --- Function ---

# --- Main Code ---
array = [10, "texto", 5.5, 3, [1,2], 8]
result = analisar_argumentos(array)
print(result)

# --- Main Code ---