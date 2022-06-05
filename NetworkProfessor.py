from configparser import NoOptionError


class NetworkProfessor:

    #Função Construtora da Network
    def __init__(self, num_vert = 0, lista_adj = None, mat_adj = None , arestas = None, mat_cap = None, mat_weight = None, professores = None):

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

        if mat_weight == None:
            self.mat_weight = [[0 for i in range(num_vert)] for j in range(num_vert)] 

        if arestas == None:
            self.arestas = [[]for _ in range(num_vert)]
        else:
            self.arestas = arestas

  #-------------------------------------------------------------------------------
  #Função criada para adicionar aresta com valor default (1) do vértice u ao vértice v
  #-------------------------------------------------------------------------------
  
    def add_aresta(self, u, v, w = 1, c = 'inf'):

        self.arestas.append((u, v, w, c))
        #self.mat_aeightdj[u][v].append(w)
        #self.mataadjt_wej[u]].append(w)
        #self.mat_weight[u]v].append(c)


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
  
    def ler_arquivo(self, nome_arqprof, nomearqdisc):
        try:
            arq = open(nome_arqprof)
            arq2 = open(nome_arqprof)#arquivo com a função unica de servir pra contar as linhas(ver se tem otimização disso)
            arq3 = open(nomearqdisc)
            arq4 = open(nomearqdisc)#arquivo com a função unica de servir pra contar as linhas(ver se tem otimização disso)
            
            #Leitura do cabeçalho
            #-------------------------------------------------------------------------------
            str = arq.readline()
            str = str.split(";")
            
            lines = int(len(arq2.read().split(";"))/6) - 1#Quantidade de linhas sem o cabeçalho 


            #-------------------------------------------------------------------------------
            #Inicialização da Estrutura de Dados
            #-------------------------------------------------------------------------------
            sum = 0
            for _ in range(lines - 1):
                self.num_vert+=1

                str = arq.readline()
                str = str.split(";")
                
                p = str[0]
                c = int(str[1])
                
                sum += c
                p1 = str[2]
                self.add_aresta(p,p1,0)
                
                p2 = (str[3],3)
                self.add_aresta(p,p2,3)

                p3 = (str[4],5)
                self.add_aresta(p,p3,5)

                if len(str) > 5:#Isso pois nem todos professores podem lecionar mais de 3 disciplinas
                    p4 = (str[5],8)
                    self.add_aresta(p,p4,0)

                if len(str) > 6:#Isso pois nem todos professores podem lecionar mais de 3 disciplinas
                    p5 = (str[6],10)
                    self.add_aresta(p,p5,10)
            #-------------------------------------------------------------------------------------------
            print("s1 =>", sum)
            str = arq3.readline()
            str = str.split(";")
            sum  = 0
            lines = int(len(arq4.read().split(";"))/2) - 1#Quantidade de linhas sem o cabeçalho 
            #---------------------------------------------------------------------------------------------
            for _ in range(lines - 1):
                self.num_vert+=1

                str = arq3.readline()
                str = str.split(";")
                
                c =  str[0]
                n =  str[1]
                q =  int(str[2])
                sum+=q
                print("s2 =>", sum)


        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")
    
    def scm(self,w,c,b,s,t):   
       F = [[0 for i in range(len(self.mat_adj))] for j in range(len(self.mat_adj))]  
       C = self.bellmanFord(s, t)
       return
    def bellmanFord(self, s, t):

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