from calendar import c
from configparser import NoOptionError


class NetworkProfessor:

    #Função Construtora da Network
    def __init__(self, num_vert = 0, lista_adj = None, mat_adj = None , arestas = None, mat_cap = None, mat_weight = None, list_b = None, professores = None):
        self.dic = {}
        self.infosProfessores = []
        self.infosDisciplinas = []

        self.num_vert = num_vert

        #Verificações acerca das arestas e Lista de Adjacencias
        #-------------------------------------------------------------------------------
        if lista_adj == None:
            self.lista_adj = [[]for _ in range(num_vert)]
        else: 
            self.lista_adj = lista_adj

        if mat_adj == None:
            self.mat_adj = [[0 for _ in range(num_vert)] for j in range(num_vert)] 
        else:                                         
            self.mat_adj = mat_adj

        if mat_cap == None:
            self.mat_cap = [[0 for _ in range(num_vert)] for j in range(num_vert)] 
        else:                                         
            self.mat_cap = mat_cap

        if mat_weight == None:
            self.mat_weight = [[0 for _ in range(num_vert)] for j in range(num_vert)] 
        else:
            self.mat_weight = mat_weight

        if arestas == None:
            self.arestas = [[]for _ in range(num_vert)]
        else:
            self.arestas = arestas

  
    #função pra preencher as matrizes com 0
    def criaMats(self):
        self.mat_cap = [[0 for _ in range(self.num_vert)] for _ in range(self.num_vert)]
        self.mat_adj = [[0 for _ in range(self.num_vert)] for _ in range(self.num_vert)]
        self.mat_weight = [[0 for _ in range(self.num_vert)] for _ in range(self.num_vert)]

  #-------------------------------------------------------------------------------
  #Função criada para adicionar aresta com valor default (1) do vértice u ao vértice v
  #-------------------------------------------------------------------------------
    def add_aresta(self, u, v, w = 1, c = 'inf'):

        self.arestas.append((u, v, w, c))
        self.mat_adj[u][v] = 1
        self.mat_weight[u][v] = w
        self.mat_cap[u][v] = c

    def addDic(self, valor, key):#Função pra criar o dicionario de professores e de disciplinas com SO e SD
        self.dic[valor] = key 
         
    #-------------------------------------------------------------------------------
    #Função criada para remover uma aresta do vértice u ao vértice v (caso exista)
    #-------------------------------------------------------------------------------
  
    def remove_aresta(self, u, v):

        if u < self.num_vert and v < self.num_vert:

            if self.mat_adj[u][v] != 0:

                self.num_arestas += 1
                self.mat_adj[u][v] = 0

                for (v2, w2) in self.lista_adj[u]:

                    if v2 == v:
                        self.lista_adj[u].remove((v2, w2))
                        break

            else:
                print("Aresta inexistente!")

        else:
            print("Aresta invalida!")
    
    #Função para Criar o Dicionário e gerar a Network
    def makeNetwork(self):
        cont = 0 
        self.infosProfessores[-1][1] = int(self.infosProfessores[-1][1])
        self.addDic(self.infosProfessores[-1][1], cont)
        cont += 1
        for x in range(len(self.infosProfessores)):
            self.addDic(self.infosProfessores[x][0], cont)
            cont += 1
        
        for x in range(len(self.infosDisciplinas)): 
            self.addDic(self.infosDisciplinas[x][0],cont)
            cont += 1
            
        
        self.infosDisciplinas[-1][2] = - int(self.infosDisciplinas[-1][2])
        self.addDic(self.infosDisciplinas[-1][2], cont)

        self.num_vert = len(self.dic)
        self.criaMats()

        #Gerar Network
        #1 - Ligação do SuperOferta
        for x in range(len(self.infosProfessores)):
            self.add_aresta(self.dic[self.infosProfessores[-1][1]], self.dic[self.infosProfessores[x][0]], 0, self.infosProfessores[x][1])
           
        #Ligação Professor -> disciplina
        for x in range(len(self.infosProfessores)):
            cont = 2
            for _ in range(5):#5 poie é o maximo de disciplinas alocadas a um professor
                match cont:
                    case 2:#Preferencia 1
                        self.add_aresta(self.dic[self.infosProfessores[x][0]], self.dic[self.infosProfessores[x][cont]],0)
                    case 3:#Preferencia 2
                        self.add_aresta(self.dic[self.infosProfessores[x][0]], self.dic[self.infosProfessores[x][cont]],3)
                    case 4:#Preferencia 3
                        self.add_aresta(self.dic[self.infosProfessores[x][0]], self.dic[self.infosProfessores[x][cont]],5)
                    case 5:#Preferencia 4
                        if(self.infosProfessores[x][cont]!= ''):
                            self.add_aresta(self.dic[self.infosProfessores[x][0]], self.dic[self.infosProfessores[x][cont]],8)
                    case 6:#preferencia 5
                        if(self.infosProfessores[x][cont]!= ''):
                            self.add_aresta(self.dic[self.infosProfessores[x][0]], self.dic[self.infosProfessores[x][cont]],10)
                cont+=1
            
        #Ligação Discuplina-> superdemanda
        for x in range(len(self.infosDisciplinas)):
            self.add_aresta(self.dic[self.infosDisciplinas[x][0]], self.dic[self.infosDisciplinas[len(self.infosDisciplinas)-1][2]], 0, self.infosDisciplinas[x][1])
    #-------------------------------------------------------------------------------
    #Função criada para ler um arquivo no formato CSV
    #-------------------------------------------------------------------------------
    def ler_arquivo(self, nome_arqprof, nome_arqdisc):
        try:
            
            #Leitura do Arquivo de Professores
            #-------------------------------------------------------------------------------
            arq = open(nome_arqprof)
            arq2 = open(nome_arqprof)#arquivo com a função unica de servir pra contar as linhas

            str = arq.readline()
            str = str.split(";")
            lines = int(len(arq2.read().split(";"))/6) - 1 #Quantidade de linhas sem o cabeçalho     
            
            for _ in range (lines):

                str = arq.readline()
                str = str.split("\n")
                str = str[0].split(";")
                self.infosProfessores.append(str)
    
            #Leitura do Arquivo de Disciplinas
            #-------------------------------------------------------------------------------------------
            arq = open(nome_arqdisc)
            arq2 = open(nome_arqdisc)#arquivo com a função unica de servir pra contar as linhas

            str = arq.readline()
            str = str.split(";")
            lines = int(len(arq2.read().split(";"))/2) - 1 #Quantidade de linhas sem o cabeçalho 
           
            for _ in range(lines):

                str = arq.readline()
                str = str.split("\n")
                str = str[0].split(";")
                self.infosDisciplinas.append(str)
            
            self.makeNetwork()

        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")
    
    def bellmanFord(self, s):

        dist = [ float("inf") for _ in range(self.num_vert) ]
        pred = [None for _ in range(self.num_vert)]

        dist[s] = 0
    
        for _ in range(self.num_vert - 1):
            trocou = False

            for (u,v,w) in self.arestas:

                if dist[v] >  dist[u]+w:
                    dist[v] = dist[u]+w
                    pred[v] = u
                    trocou = True
      
        #Otimização do algoritmo para evitar descobertas desnecessárias
        #-------------------------------------------------------------------------------
                if(trocou == False):
                    break
        #-------------------------------------------------------------------------------

        return dist,pred

    def scm(self, s, t):

        F = [[0 for i in range(len(self.mat_adj))] for j in range(len(self.mat_adj))]
        C = self.bellmanFord(s, t)

        while len(C) != 0 and self.list_b[s] != 0:

            f = float('inf')

            for i in range(1, len(C)):
                u = C[i - 1]
                v = C[i]

                if self.mat_cap[u][v] < f:
                    f = self.mat_cap[u][v]

            for i in range(1, len(C)):
                u = C[i - 1]
                v = C[i]

                F[u][v] += f
                self.mat_cap[u][v] -= f
                self.mat_cap[v][u] += f

                self.list_b[s] -= f
                self.list_b[t] += f

                if self.mat_cap == 0:
                    self.mat_adj[u][v] = 0
                    self.arestas.remove((u, v, self.mat_weight[u][v])) #Verificar esta linha
                
                if self.mat_adj[v][u] == 0:
                    self.mat_adj[v][u] = 1
                    self.arestas.append((v, u, -self.mat_weight[u][v]))#Verificar esta linha
                    self.mat_weight[v][u] = -(self.mat_weight[u][v])
                
            C = self.bellmanFord(s, t)
        
        return F