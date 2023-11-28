import random 
import os
import pandas as pd

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def salvar_medias(nome_csv, media_peso, media_valor, peso_melhor_individuo, valor_melhor_individuo, melhor_individuo):
    df = pd.DataFrame({
        'media_peso': media_peso, 
        'media_valor': media_valor, 
        'peso_melhor_individuo': peso_melhor_individuo, 
        'valor_melhor_individuo': valor_melhor_individuo, 
        'melhor_individuo': melhor_individuo
        })
    nome_arquivo = f'{nome_csv}.csv'
    df.to_csv(nome_arquivo, index=False)
    print(f'Gerações salvas em {nome_arquivo}')

def salvar_items(nome_csv, items):
    peso = []
    valor = []
    peso = [i[0] for i in items]
    valor = [i[1] for i in items]
    df = pd.DataFrame({
        'peso': peso,
        'valor': valor
        })
    nome_arquivo = f'{nome_csv}.csv'
    df.to_csv(nome_arquivo, index=False)
    print(f'Items salvos em {nome_arquivo}')

def gerar_individuo(quant_items, max_peso_mochila, items):
    individuo = [random.choice([0, 1]) for _ in range(quant_items)]
    if checar_individuo(max_peso_mochila, individuo, items):
        return individuo
    else:
        individuo = corrigir_peso(individuo, max_peso_mochila, items)
        return individuo
    
def gerar_populacao_inicial(quant_items, quant_individuos, max_peso_mochila, items):
    return [gerar_individuo(quant_items, max_peso_mochila, items) for _ in range(quant_individuos)]

def display_populacao(populacao, items):
    for i in range(len(populacao)):
        print(f'{i}: peso {calcula_peso(populacao[i], items)} val {calcula_valor(populacao[i], items)}')

def print_populacao(str, populacao, items):
    print(f'\n{str}:\n', end='\n')
    for i in range(len(populacao)):
        print(f'{i}: {populacao[i]} {calcula_peso(populacao[i], items)} {calcula_valor(populacao[i], items)}')
    
def print_individuo(individuo, i, items):
    print(f'Melhor da geração {i}: {calcula_peso(individuo, items)} {calcula_valor(individuo, items)}')

def calcula_valor(individuo, items):
    return sum(items[i][1] for i in range(len(individuo)) if individuo[i] == 1)

def calcula_peso(individuo, items):
    return sum(items[i][0] for i in range(len(individuo)) if individuo[i] == 1)

def escolhe_melhor(populacao, items):
    populacao = calcular_valor_populacao(populacao, items)
    populacao = sorted(populacao, key=lambda x: x[1], reverse=True)
    melhor_individuo = populacao[0][0]
    return melhor_individuo

def escolhe_individuos(populacao, items, sorted_key=1, porcentagem_selecionados=1):
    populacao = calcular_valor_populacao(populacao, items)
    populacao = sorted(populacao, key=lambda x: x[sorted_key], reverse=True)
    indice_divisao = int(len(populacao) * porcentagem_selecionados)    
    selecionados = populacao[:indice_divisao]
    restante = populacao[indice_divisao:]
    selecionados_novos = []
    restante_novos = []
    for i in range(len(selecionados)):
        selecionados_novos.append(selecionados[i][0])
    for i in range(len(restante)):
        restante_novos.append(restante[i][0])

    return selecionados_novos, restante_novos

def escolhe_individuos_ponderado(populacao, items, sorted_key=1, porcentagem_selecionados=1):
    # print('pop ', len(populacao), end=' ')
    populacao = calcular_valor_populacao(populacao, items)
    populacao = sorted(populacao, key=lambda x: x[sorted_key], reverse=True)
    indice_divisao = int(len(populacao) * porcentagem_selecionados)    

    soma_aptidao = sum(individuo[sorted_key] for individuo in populacao)

    probabilidades = [individuo[sorted_key] / soma_aptidao for individuo in populacao]

    selecionados = random.choices(populacao, weights=probabilidades, k=indice_divisao)
    restante = populacao[len(selecionados):]

    selecionados_novos = [individuo[0] for individuo in selecionados]
    restante_novos = [individuo[0] for individuo in restante]
    # print(len(selecionados + restante)) 

    return selecionados_novos, restante_novos

def calcular_valor_populacao(populacao, items):
    nova_populacao = []
    for individuo in populacao:
        valor_individuo = calcula_valor(individuo, items)
        nova_lista_individuo = [individuo, valor_individuo]
        nova_populacao.append(nova_lista_individuo)
    return nova_populacao

def checar_individuo(max_peso, individuo, items):
    peso_total = calcula_peso(individuo, items) 

    if peso_total <= max_peso:
        return True  
    else:
        return False 

def crossover(solucao1, solucao2, items, max_peso_mochila, prob_crossover=0.5): 
    filho1 = solucao1.copy()
    filho2 = solucao2.copy()
    
    for i in range(len(solucao1)):
        probabilidade = random.random()
        if probabilidade < prob_crossover:
            filho1[i] = solucao2[i]
            filho2[i] = solucao1[i]

    filho2 = corrigir_peso(filho2, max_peso_mochila, items)
    filho1 = corrigir_peso(filho1, max_peso_mochila, items)

    return filho1, filho2

def crossover_populacao(populacao, items, max_peso_mochila, prob_crossover=0.5):
    nova_populacao = []

    if len(populacao) % 2 == 1:
        nova_populacao.append(populacao[0])
        populacao = populacao[1:]

    for i in range(0, len(populacao), 2):
        solucao1 = populacao[i]
        solucao2 = populacao[i + 1]

        filho1, filho2 = crossover(solucao1, solucao2, items, max_peso_mochila, prob_crossover)

        nova_populacao.append(filho1)
        nova_populacao.append(filho2)

    return nova_populacao

def corrigir_peso_aleatorio(individuo, max_peso_mochila, items): # remove item aleatorio, enquanto peso > max_peso
    peso_total = calcula_peso(individuo, items)
    if peso_total == 0:
        individuo = gerar_individuo(len(items), max_peso_mochila, items)
        return individuo
    while peso_total > max_peso_mochila:
        indice_item = random.randint(0, len(individuo) - 1)
        individuo[indice_item] = 0
        peso_total = calcula_peso(individuo, items)
    return individuo

def corrigir_peso(individuo, max_peso, items): # remove item com menor valor / peso, enquanto peso > max_peso
    peso_total = calcula_peso(individuo, items)
    
    ordem = calcula_ordem_items(items)

    while peso_total > max_peso:
        ordem, individuo = retira_item(ordem, individuo)
        peso_total = calcula_peso(individuo, items)
    # print('novo peso:', calcula_peso(individuo, items))
    return individuo

def retira_item(ordem, individuo):
    if ordem and individuo:
        indice_a_remover = ordem.pop(0)
        # print('individuo', individuo)
        # if 0 <= indice_a_remover < len(individuo):
        individuo[indice_a_remover] = 0
    return ordem, individuo

def calcula_ordem_items(items):
    # Função de chave personalizada para a função sorted
    def razao_valor_peso(item):
        peso, valor = item[0], item[1]
        return valor / peso

    # Adiciona índices aos items para preservar a ordem original durante a ordenação
    items_enum = list(enumerate(items))
    # Ordena os items com base na razão valor/peso em ordem decrescente
    ordenados = sorted(items_enum, key=lambda x: razao_valor_peso(x[1]), reverse=True)
    # for i in range(len(items)):
    #     print('razao:', i)
    #     print(razao_valor_peso(items[i]))
    ordem = [i[0] for i in ordenados]

    return ordem 

def calcula_peso(individuo, items):
    peso_total = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            peso_total += items[i][0]
    return peso_total

def peso_medio_populacao(populacao, items):
    if not populacao:
        return 0  
    soma_pesos = sum(calcula_peso(individuo, items) for individuo in populacao)
    media_peso = soma_pesos / len(populacao)
    
    return media_peso

def valor_medio_populacao(populacao, items):
    if not populacao:
        return 0  
    soma_valor = sum(calcula_valor(individuo, items) for individuo in populacao)
    media_valor = soma_valor / len(populacao)
    
    return media_valor

def geracoes(quant_items, quant_individuos, items, max_peso_mochila, prob_crossover, taxa_mutacao, quant_geracoes=100, porcentagem_selecionados=0.2):
    media_peso = []
    media_valor = []
    peso_melhor_individuo = []
    valor_melhor_individuo = []
    melhor_individuo = []
    populacao = gerar_populacao_inicial(quant_items, quant_individuos, max_peso_mochila, items)
    populacao.extend(gerar_populacao_inicial(quant_items, quant_individuos, max_peso_mochila, items))
    melhor = escolhe_melhor(populacao, items)
    # print_individuo(melhor, 0, items)
    for _ in range(quant_geracoes):
        sobrevivem, _ = escolhe_individuos(populacao, items, porcentagem_selecionados=0.5)
        selecionados, restante = escolhe_individuos(sobrevivem, items, porcentagem_selecionados=porcentagem_selecionados)
        populacao = crossover_populacao(selecionados, items, max_peso_mochila, prob_crossover=prob_crossover) + mutacao(restante, taxa_mutacao, max_peso_mochila, items) + sobrevivem
        melhor = escolhe_melhor(populacao, items)
        valor_medio = valor_medio_populacao(populacao, items)
        peso_medio = peso_medio_populacao(populacao, items)
        media_valor.append(valor_medio)
        media_peso.append(peso_medio)
        melhor_individuo.append(melhor) 
        peso_melhor_individuo.append(calcula_peso(melhor, items))
        valor_melhor_individuo.append(calcula_valor(melhor, items))
    # print_individuo(melhor, quant_geracoes, items)
    return media_valor, media_peso, peso_melhor_individuo, valor_melhor_individuo, melhor_individuo

def mutacao(populacao, taxa_mutacao, max_peso, items):
    nova_populacao = []

    for individuo in populacao:
        if random.random() < taxa_mutacao:
            novo_individuo = gerar_individuo(len(individuo), max_peso, items)
            while not checar_individuo(max_peso, novo_individuo, items):
                novo_individuo = gerar_individuo(len(individuo), max_peso, items)
        else:
            novo_individuo = individuo.copy()

        nova_populacao.append(novo_individuo)

    return nova_populacao

