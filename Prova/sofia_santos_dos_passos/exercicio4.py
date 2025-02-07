"""
Exercício 04 – Corrigir e Acrescentar Linhas de Código para Processamento de Números  (tempo aproximado 15 a 20 min)

Objetivo:
O código a seguir tem a intenção de:
  1. Solicitar ao usuário uma lista de números separados por vírgula.
  2. Converter essa entrada em uma lista de inteiros.
  3. Utilizar a função map para calcular o cubo de cada número.
  4. Utilizar a função filter para selecionar apenas os cubos que são pares.
  5. Utilizar a função reduce para somar todos os cubos impares.
  6. Acrescentar 2 linhas de código para calcular e exibir o maior cubo par e menor ímpar.

Contudo, o código apresenta diversos erros de conversão de tipos, sintaxe e lógica.  
** Sua tarefa: **  
  - Identificar e corrigir todos os erros presentes.
  - Adicionar as linhas necessárias para calcular e exibir o maior cubo par.
  - Insira comentários explicando cada correção realizada e as novas linhas adicionadas.

Dicas:
  - Converta cada elemento da lista para inteiro antes de aplicar a função map.
  - No lambda do filter, utilize a comparação correta (==) para testar se o número é par.
  - Na chamada de reduce, certifique-se de separar a função lambda e o iterável por uma vírgula.
  - Utilize a função print() com parênteses, conforme a sintaxe do Python 3.
  - Para calcular o maior valor, você pode utilizar a função built-in max().
"""
# Código com erros:
#--------------------------------------------------
from functools import reduce
# # Adicionado o import da função reduce

numbers_input = input("Digite uma lista de números separados por vírgula: ")

# Converte a entrada para uma lista de inteiros (erro: conversão ausente)
numbers_list = list(numbers_input.strip(","))
numbers_list_2 = []
for n in numbers_list:
    if isinstance(n, (int, float)):
        numbers_list_2.append(n)
print(numbers_list_2)

# Calcula o cubo de cada número (erro: os elementos não foram convertidos para int)
# # Adicionado o int()
squared_numbers = filter(lambda x: int(x) ** 2, numbers_list)

# Filtra apenas os cubos pares (erro: sintaxe incorreta no lambda)
# # Corrigido o lambda e o sinal de igual e o int()
even_squares = filter(lambda x: int(x) % 2 == 0, squared_numbers)

# Soma os cubos pares utilizando reduce (erro: sintaxe incorreta na chamada de reduce)
# # Corrigido a utilização da função reduce
total = reduce(lambda a, b: a + b, even_squares)


# # Adicionados parênteses para corrigir
print("A soma dos cubos pares é: " + soma_total)

# Adicione duas linhas para calcular e exibir o maior cubo par.
#--------------------------------------------------
"""
Exemplo de execução esperada (para entrada: "1,2,3,4,5"):
  - Quadrados: [1, 4, 9, 16, 25]
  - Quadrados pares: [4, 16]
  - Soma: 20
  - Maior quadrado par: 16

Boa sorte e boa prova!
"""
# Sua solução abaixo.
