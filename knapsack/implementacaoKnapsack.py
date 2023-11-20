import utils

# Definindo parâmetros do problema da mochila
quant_items = 10 # somente para teste, tem que ser 100
max_peso = 50 # para cada item
max_valor = 1000 # para cada item
max_peso_mochila = 100 
quant_individuos = 20
porcentagem_selecionados = 0.2 # a ser decidido
taxa_mutacao = 0.1 # a ser decidido
quant_geracoes = 100
prob_crossover = 0.3

items = utils.gerar_items(quant_items, max_peso, max_valor)
utils.display_items(items, sorted_list=0)

populacao = utils.gerar_populacao_inicial(quant_items, quant_individuos, max_peso_mochila, items)

peso_medio = utils.peso_medio_populacao(populacao, items)
valor_medio = utils.valor_medio_populacao(populacao, items)
print(peso_medio, valor_medio)

media_valor, media_peso, peso_melhor_individuo, valor_melhor_individuo, melhor_individuo = utils.geracoes(populacao, items, max_peso_mochila, prob_crossover, taxa_mutacao, quant_geracoes=quant_geracoes, porcentagem_selecionados=porcentagem_selecionados)

utils.salvar_medias('medias', media_peso, media_valor, peso_melhor_individuo, valor_melhor_individuo, melhor_individuo)

utils.escolhe_melhor(populacao, items)