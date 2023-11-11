import sys
sys.path.insert(0, 'C:\\Users\\caioc\\OneDrive\\Documentos\\UFPE\\2023.2\\Bioinspirada\\bioinspiredComputing')
import utils

# Definindo parâmetros do problema da mochila
quant_items = 10
items = []
max_peso = 50 
max_valor = 1000
max_peso_mochila = 100
quant_individuos = 25
taxa_mutacao = 0.1
quant_geracoes = 100
quant_iteracoes = 100

items = utils.gerar_items(quant_items, max_peso, max_valor)
utils.limpar_tela()
utils.display_items(items, sorted_list=0)

# populacao = utils.gerar_populacao_inicial(quant_items, quant_individuos)
# print('individuos gerados:', len(populacao))

individuo = utils.gerar_individuo(quant_items, max_peso_mochila, items)
print('individuo:', individuo)
peso = utils.calcular_peso(individuo, items)
print('peso:', peso)
