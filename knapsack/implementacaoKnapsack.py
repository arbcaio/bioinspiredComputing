import utils

# Definindo parâmetros do problema da mochila
quant_items = 100 
max_peso = 50 # para cada item
max_valor = 1000 # para cada item
max_peso_mochila = 100 
quant_individuos = 20
porcentagem_selecionados = 0.1 # para o crossover
taxa_mutacao = 0.2 # a ser decidido
quant_geracoes = 500
quant_iteracoes = 100
prob_crossover = 0.3

items = utils.gerar_items(quant_items, max_peso, max_valor)
utils.display_items(items, sorted_list=0)
utils.salvar_items('items', items)

total_valor = []
total_peso = []
total_peso_melhor_individuo = []
total_valor_melhor_individuo = []
total_melhor_individuo = []

for i in range(quant_iteracoes):
    print(f'Geração: {i}')
    media_valor, media_peso, peso_melhor_individuo, valor_melhor_individuo, melhor_individuo = utils.geracoes(quant_items, quant_individuos, items, max_peso_mochila, prob_crossover, taxa_mutacao, quant_geracoes=quant_geracoes, porcentagem_selecionados=porcentagem_selecionados)
    total_valor.extend(media_valor)
    total_peso.extend(media_peso)
    total_peso_melhor_individuo.extend(peso_melhor_individuo)
    total_valor_melhor_individuo.extend(valor_melhor_individuo)
    total_melhor_individuo.extend(melhor_individuo)
utils.salvar_medias('medias', (total_peso), total_valor, total_peso_melhor_individuo, total_valor_melhor_individuo, total_melhor_individuo)
