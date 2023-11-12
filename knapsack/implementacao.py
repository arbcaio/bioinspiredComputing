import sys
import utils

# Definindo parâmetros do problema da mochila
quant_items = 10 # somente para teste, tem que ser 100
max_peso = 50 
max_valor = 1000
max_peso_mochila = 100
quant_individuos = 2
porcentagem_selecionados = 0.5 # a ser decidido
taxa_mutacao = 0.25 # a ser decidido
quant_geracoes = 100
quant_iteracoes = 100

items = utils.gerar_items(quant_items, max_peso, max_valor)
utils.limpar_tela()
utils.display_items(items, sorted_list=0)

populacao = utils.gerar_populacao_inicial(quant_items, quant_individuos, max_peso_mochila, items)
print(populacao)
filhos = utils.crossover(populacao[0], populacao[1], items, max_peso)
print(filhos, '\npeso, valor filho 1:', utils.calcular_peso(filhos[0], items), utils.calcular_valor(filhos[0], items), '\npeso, valor filho 2:', utils.calcular_peso(filhos[1], items), utils.calcular_valor(filhos[1], items)) 


#crossover entre a populacao agora
for i in range(0, len(populacao), 2):
    solucao1 = populacao[i]
    solucao2 = populacao[i + 1]

    filhos = utils.crossover(solucao1, solucao2, items, max_peso)

    #substituir os pais pelos filhos na população
    populacao[i] = filhos[0]
    populacao[i + 1] = filhos[1]

print("apos o crossover da populacao",populacao)

populacao_mutada = utils.mutacao(populacao, taxa_mutacao, max_peso_mochila, items)

#apos a mutacao
print("População após mutação:", populacao_mutada)
