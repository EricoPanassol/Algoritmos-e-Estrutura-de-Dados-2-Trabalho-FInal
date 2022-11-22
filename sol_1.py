import networkx as nx
import time as tm

caso = int(input(""" Escolha o caso de teste:
[0] - caso0.txt 
[1] - caso10.txt 
[2] - caso20.txt 
[3] - caso30.txt 
[4] - caso40.txt 
[5] - caso50.txt 
[6] - caso60.txt      
"""))

match caso:
    case 0:
        print("abrindo casos/caso0.txt")
        file = open("casos/caso0.txt", "r")
    case 1:
        print("abrindo casos/caso10.txt")
        file = open("casos/caso10.txt", "r")
    case 2:
        print("abrindo casos/caso20.txt")
        file = open("casos/caso20.txt", "r")
    case 3:
        print("abrindo casos/caso30.txt")
        file = open("casos/caso30.txt", "r")
    case 4:
        print("abrindo casos/caso40.txt")
        file = open("casos/caso40.txt", "r")
    case 5:
        print("abrindo casos/caso50.txt")
        file = open("casos/caso50.txt", "r")
    case 6:
        print("abrindo casos/caso60.txt")
        file = open("casos/caso60.txt", "r")

comb_sorvetes = []
sabores = []
graph = nx.DiGraph()
copo2 = []
qtdCopo2 = 0
qtdCopo3 = 0

start_time = tm.time()

# adiciona cada linha numa pos de comb_sorvetes
for line in file:
    comb_sorvetes.append(line.strip())
            
# adiciona os sabores únicos em sabores
for sabor in comb_sorvetes:  
    for sab in sabor.split():
        if (sab != "->" and sab not in sabores):
            sabores.append(sab)
    
# para cadda sabor mais forte e mais fraco, add o forte ([0]) como pai do fraco ([2])
for comb in comb_sorvetes:
    graph.add_edge(comb.split()[0], comb.split()[2])

# para cada sabor, add no copo2 e ve se tem ancestral, se nao, passa pro prox sabor
# se sim, adiciona a lista de ancestrais em copo2
for sabor in sabores:
    copo2.append(sabor)
    if list(nx.ancestors(graph, sabor)) != []:
        copo2.append(list(nx.ancestors(graph, sabor)))


# o elem que está seguido de uma lista é o sabor que forma copinhos2 com seus ancestral
# print(copo2)

# se o elem for uma lista, ve o tamanho dela e incrementa o copo2, é quantidade de copos de 2 sabores
# capazes de formar o o elem que está antes da lista
for a in copo2:
    if type(a) == list:
        qtdCopo2 += len(a)

# para formar os copos3 percorro os sabores 3 vezes,
# vejo se os nodos não sao os mesmo, se não sao, vejo se tem caminhos entre eles
# e a cada caminho entre eles, adiciono na lista de copos3
for u in sabores:
  for v in sabores:
    for w in sabores:
      if u != v and u != w and v != w:
        if nx.has_path(graph, u, v) and nx.has_path(graph, u, w) and nx.has_path(graph, v, w):
          qtdCopo3 += 1

total_time = round(tm.time() - start_time, 2)

print(file.name, "\n2 sabores:", qtdCopo2, "\n3 sabores:", qtdCopo3, "\nTempo de execução: %s segundos" % total_time)


