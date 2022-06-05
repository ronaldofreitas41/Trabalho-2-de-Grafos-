class NetworkProfessor:# depois arrumar

  #Função Construtora da Network
  def __init__(self, num_vert = 0, lista_adj = None, mat_adj = None , arestas = None, mat_cap = None):

    self.num_vert = num_vert

    #Verificações acerca das srestas e Lista de Adjacencias
    #-------------------------------------------------------------------------------
    if lista_adj == None:
        self.lista_adj = [[]for _ in range(num_vert)]
    else: 
        self.lista_adj = lista_adj

    if mat_adj == None:
        self.mat_adj = [[0 for i in range(num_vert)] for j in range(num_vert)] 
    else:                                         
        self.mat_adj = mat_adj

    if mat_cap == None:
        self.mat_cap = [[0 for i in range(num_vert)] for j in range(num_vert)] 
    else:                                         
        self.mat_cap = mat_cap

    if arestas == None:
        self.arestas = [[]for _ in range(num_vert)]
    else:
        self.arestas = arestas

  #-------------------------------------------------------------------------------
  #Função criada para adicionar aresta com valor default (1) do vértice u ao vértice v
  #-------------------------------------------------------------------------------
  
  def add_aresta(self, u, v, w = 1, c = 0):

    self.num_arestas += 1

    if u < self.num_vert and v < self.num_vert:
        
        self.arestas.append((u, v, w))
        self.lista_adj[u].append((v, w)) 
        self.mat_adj[u][v].append(w)
        self.mat_cap[u][v].append(c)

    else:
      print("Aresta inválida!")

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
  
  #-------------------------------------------------------------------------------
  #Função criada para ler um arquivo no formato DIMACS
  #-------------------------------------------------------------------------------
  
  def ler_arquivo(self, nome_arq):

    try:
        arq = open(nome_arq)

        #Leitura do cabeçalho
        #-------------------------------------------------------------------------------
        str = arq.readline()
        str = str.split(";")
        self.num_vert = int(str[0])
        self.num_arestas = int(str[1])

        #-------------------------------------------------------------------------------
        #Inicialização da Estrutura de Dados
        #-------------------------------------------------------------------------------
        
        self.lista_adj = [[] for _ in range(self.num_vert)]

        for _ in range(0,self.num_arestas):
            str = arq.readline()
            str = str.split(" ")

            u = int(str[0])
            v = int(str[1])
            p1 = str[2]
            p2 = str[3]
            p3 = str[4]
            
            if len(str) > 5:
                p4 = str[5]
            if len(str) > 6:
                p5 = str[6]

            self.add_aresta(u, v, 0)
        #-------------------------------------------------------------------------------
    
    except IOError:
        print("Nao foi possivel encontrar ou ler o arquivo!")
    
    #Nao sei quais metodos tem que por no codigo a partir daqui