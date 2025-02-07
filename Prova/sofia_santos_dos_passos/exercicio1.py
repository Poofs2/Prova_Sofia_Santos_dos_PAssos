"""
Exercício 01 – Análise de Vendas (tempo aproximado 10 a 13 min)

Objetivo:
Você recebeu um dicionário representando as vendas mensais de uma loja. Cada chave é o nome de um produto e o valor é uma lista de inteiros representando as vendas mensais.
Sua tarefa é:
  1. Criar uma função chamada `media_vendas` que calcule a média de vendas para cada produto.
  2. Retornar um novo dicionário contendo apenas os produtos cuja média de vendas seja maior ou igual a um valor mínimo (parâmetro da função).

Requisitos:
  - Utilize um dictionary comprehension para calcular as médias.
  - Use funções built-in como `sum` e `len` para calcular a média.
  - Utilize estruturas condicionais para filtrar os produtos de acordo com o valor mínimo fornecido.
  
Exemplo de uso:
    vendas = {
        "Produto A": [100, 200, 150],
        "Produto B": [50, 60, 70],
        "Produto C": [300, 250, 400]
    }
    resultado = media_vendas(vendas, 150)
    print(resultado)
    # Saída esperada (exemplo): {'Produto A': 150.0, 'Produto C': 316.67}
    
Observação: Formate a média como número float com duas casas decimais, se desejar.
"""
# Sua solução aqui

# --- Function ---  
def media_vendas(dic, min):
  values = dic.values()
  vendas_m = list( map(lambda x: sum(x)/len(x), values))
   vendas_medium = {
     'Produto A': vendas_m[0],
     'Produto B': vendas_m[1],
     'Produto C': vendas_m[2]
     }
  # for x in range(0, len(vendas_m)):
  #   if vendas_medium[???] >= min:
    return vendas_medium
# --- Function ---

# --- Main Code ---
vendas = {
        "Produto A": [100, 200, 150],
        "Produto B": [50, 60, 70],
        "Produto C": [300, 250, 400]
    }
# vendas_medium = vendas.keys()
# values = vendas.values()
# min = int(input("Qual o valor minimo?\n"))
# for key in vendas_medium:  
#   media = list(map(lambda x: sum(x) / len(x), values))
print(media_vendas(vendas, 150))



# --- Main Code ---
