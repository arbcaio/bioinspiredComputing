import random
import utils

# Definindo parâmetros do problema da mochila
quant_items = 100
items = []
max_peso = 50 
max_valor = 1000
max_peso_mochila = 100
quant_individuos = 25
taxa_mutacao = 0.25
quant_geracoes = 100
quant_iteracoes = 100

# Algoritmo genético para resolver o problema da mochila
def algoritmo_genetico():
    # Inicialização da população
    populacao = [utils.gerar_individuo() for _ in range(quant_individuos)]

    # Loop de gerações
    for geracao in range(quant_geracoes):
        # Avaliação da aptidão da população
        aptidoes = [utils.calcular_valor(solucao) for solucao in populacao]

        # Seleção dos pais com base na aptidão
        pais = random.choices(populacao, weights=aptidoes, k=quant_individuos)

        # Criação da nova geração usando crossover e mutação
        nova_populacao = []
        for i in range(0, quant_individuos, 2):
            pai1, pai2 = pais[i], pais[i + 1]
            filho = utils.crossover(pai1, pai2)
            filho = utils.mutacao(filho)
            nova_populacao.extend([pai1, pai2, filho])

        populacao = nova_populacao

    # Encontrar a melhor solução
    melhor_individuo = max(populacao, key=utils.calcular_valor)
    melhor_valor = utils.calcular_valor(melhor_individuo)
    melhor_peso = utils.calcular_peso(melhor_individuo)

    print(f'Melhor solução: {melhor_individuo}')
    print(f'Valor: {melhor_valor}')
    print(f'Peso: {melhor_peso}')

# Executar o algoritmo genético
algoritmo_genetico()
