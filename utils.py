import random 
import os

# Limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para gerar items 
def gerar_items(quant_items, max_peso, max_valor):
    items = [(random.randint(1, max_peso), random.randint(1, max_valor)) for _ in range(quant_items)]
    return items

def display_items(items, items_por_vez=5, sorted_list=0, sorted_key=0):
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
        print(calcular_peso(individuo, items))
        if checar_individuo(max_peso_mochila, individuo, items):
            return individuo

def gerar_populacao_inicial(quant_items, quant_individuos):
    return [gerar_individuo(quant_items) for _ in range(quant_individuos)]

# Função para calcular o valor de uma solução
def calcular_valor(individuo, items):
    return sum(items[i][1] for i in range(len(individuo)) if individuo[i] == 1)

# Função para calcular o peso de uma solução
def calcular_peso(individuo, items):
    return sum(items[i][0] for i in range(len(individuo)) if individuo[i] == 1)

def checar_individuo(max_peso, individuo, items):
    peso_total = calcular_peso(individuo, items) 

    if peso_total <= max_peso:
        return True  
    else:
        return False 

# Função para realizar o crossover entre duas soluções
def crossover(solucao1, solucao2):
    ponto_corte = random.randint(1, len(solucao1) - 1)
    nova_solucao = solucao1[:ponto_corte] + solucao2[ponto_corte:]
    return nova_solucao

# Função para realizar a mutação em uma solução
def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]
    return individuo
