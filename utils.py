import random 
import os

# Limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para gerar items 
def gerar_items(quant_items, max_peso, max_valor):
    items = [(random.randint(1, max_peso), random.randint(1, max_valor)) for _ in range(quant_items)]
    return items

def display_items(items, items_por_vez=5, sorted_list=False, sorted_key=0):
    limpar_tela()
    print('-+-'*((items_por_vez)+2), 'Items:', '-+-'*((items_por_vez)+ 2))
    if sorted_list:
        items = sorted(items, key=lambda x: x[sorted_key])
    for i in range(0, len(items), items_por_vez):
        grupo = items[i:i + items_por_vez]
        for item in grupo:
            print(f'({item[0]:<{2}},', f'{item[1]:<{3}})', end=' ')
        print()
    print('-+-'*((items_por_vez*2)+7),)
    
    return items

# Função para gerar individuos
def gerar_individuo(quant_items, max_peso_mochila, items):
    while True:
        individuo = [random.choice([0, 1]) for _ in range(quant_items)]
        if checar_individuo(max_peso_mochila, individuo, items):
            return individuo

def gerar_populacao_inicial(quant_items, quant_individuos, max_peso_mochila, items):
    return [gerar_individuo(quant_items, max_peso_mochila, items) for _ in range(quant_individuos)]

def display_populacao(populacao, items):
    for i in range(len(populacao)):
        print(f'{i}: peso {calcular_peso(populacao[i], items)} val {calcular_valor(populacao[i], items)}')

def calcular_valor(individuo, items):
    return sum(items[i][1] for i in range(len(individuo)) if individuo[i] == 1)

def calcular_peso(individuo, items):
    return sum(items[i][0] for i in range(len(individuo)) if individuo[i] == 1)

def escolher_individuos(populacao, items, sorted_key=1, porcentagem_selecionados=1):
    populacao = calcular_valor_populacao(populacao, items)
    populacao = sorted(populacao, key=lambda x: x[sorted_key], reverse=True)
    indice_divisao = int(len(populacao) * porcentagem_selecionados)    
    selecionados = populacao[:indice_divisao]
    restante = populacao[indice_divisao:]
    return selecionados, restante

def calcular_valor_populacao(populacao, items):
    nova_populacao = []
    for individuo in populacao:
        valor_individuo = calcular_valor(individuo, items)
        nova_lista_individuo = [individuo, valor_individuo]
        nova_populacao.append(nova_lista_individuo)
    return nova_populacao

def checar_individuo(max_peso, individuo, items):
    peso_total = calcular_peso(individuo, items) 

    if peso_total <= max_peso:
        return True  
    else:
        return False 

def crossover(solucao1, solucao2, items, max_peso, prob_crossover=0.5): # por enquanto, não checa se os filhos são factiveis
    filho1 = solucao1.copy()
    filho2 = solucao2.copy()
    
    for i in range(len(solucao1)):
        probabilidade = random.random()
        if probabilidade < prob_crossover:
            filho1[i] = solucao2[i]
            filho2[i] = solucao1[i]
    if not checar_individuo(max_peso, filho1, items) or not checar_individuo(max_peso, filho2, items):
        print(filho1, 'max_peso:', max_peso, 'peso, valor filho 1:', calcular_peso(filho1, items), calcular_valor(filho1, items))
        print(filho2, 'max_peso:', max_peso, 'peso, valor filho 2:', calcular_peso(filho2, items), calcular_valor(filho2, items))
    return filho1, filho2

def mutacao(individuo, taxa_mutacao): # ainda n funciona
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]
    return individuo
