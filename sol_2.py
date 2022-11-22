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


sabores = []
edges = []
caminhos = {}
aux_line = ""
copo2 = 0
copo3 = 0

start_time = tm.time()

for line in file:
    aux_line = line.replace("\n", "").split(" -> ")
    if (aux_line[0] not in sabores):
        sabores.append(aux_line[0])
    if (aux_line[1] not in sabores):
        sabores.append(aux_line[1])
    edges.append([aux_line[0], aux_line[1]])


# caminhamento
def dfs(nodo):
    marca[nodo] = 1
    for sabor in sabores:
        if [nodo, sabor] in edges and not (sabor in marca):
            dfs(sabor)


# o dict marca é todos os nodos que foram visitados, que posseum caminho
for sabor in sabores:
    marca = {}
    dfs(sabor)
    aux = []
    for nodo in marca:
        if nodo != sabor:
            aux.append(nodo)
    caminhos[sabor] = aux


for u in sabores:
    for v in sabores:
        if u != v:
            if v in caminhos[u]:
                copo2 += 1

for u in sabores:
    for v in sabores:
        for w in sabores:
            if u != v and u != w and v != w:
                if v in caminhos[u] and w in caminhos[v] and w in caminhos[u]:
                    copo3 += 1


total_time = round(tm.time() - start_time, 2)

print(file.name, "\n2 sabores:", copo2, "\n3 sabores:", copo3, "\nTempo de execução: %s segundos" % total_time)
