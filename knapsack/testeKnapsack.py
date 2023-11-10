import utilsKnapsack

# Definindo parâmetros do problema da mochila
quant_items = 10
items = []
max_peso = 50 
max_valor = 1000
max_peso_mochila = 100
quant_individuos = 25
taxa_mutacao = 0.25
quant_geracoes = 100
quant_iteracoes = 100

items = utilsKnapsack.gerar_items(quant_items, max_peso, max_valor)
utilsKnapsack.limpar_tela()
utilsKnapsack.display_items(items, sorted_list=0)

# populacao = utilsKnapsack.gerar_populacao_inicial(quant_items, quant_individuos)
# print('individuos gerados:', len(populacao))

individuo = utilsKnapsack.gerar_individuo(quant_items, max_peso_mochila, items)
print('individuo:', individuo)
peso = utilsKnapsack.calcular_peso(individuo, items)
print('peso:', peso)
