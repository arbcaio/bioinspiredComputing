import utils

# Definindo parâmetros do problema da mochila
quant_items = 10 # somente para teste, tem que ser 100
max_peso = 50 
max_valor = 1000
max_peso_mochila = 100
quant_individuos = 10
porcentagem_selecionados = 0.2 # a ser decidido
taxa_mutacao = 0.01 # a ser decidido
quant_geracoes = 100
quant_iteracoes = 100
prob_crossover = 0.6

items = utils.gerar_items(quant_items, max_peso, max_valor)
utils.display_items(items, sorted_list=0)

populacao = utils.gerar_populacao_inicial(quant_items, quant_individuos, max_peso_mochila, items)
utils.print_populacao('populacao', populacao, items)

selecionados, restante = utils.escolher_individuos(populacao, items, porcentagem_selecionados=porcentagem_selecionados)
utils.print_populacao('selecionados', selecionados, items)

utils.print_populacao('restante', restante, items)

nova_populacao = utils.crossover_populacao(selecionados, items, max_peso, prob_crossover=prob_crossover) + utils.mutacao(restante, taxa_mutacao, max_peso, items)

utils.print_populacao('nova_populacao', nova_populacao, items)
