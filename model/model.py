from networkx import Graph

from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._allProducts = DAO.getAllProducts()
        self._idMap = {}
        for a in self._allProducts:
            self._idMap[a.Product_number] = a
    def getColors(self):
        return DAO.getColors()

    def createGraph(self,anno, colore):
        # creiamo qui il grafo perchè ci conviene visto che abbiamo solo alcuni elementi del
        # database da prendere e non tutti
        self._grafo = nx.Graph()
        #passando la mappa posso già salvarmi in nodes tutti gli oggetti
        #anche se mi sembra ridondante...non avrei comunque una lista di oggetti anche senza la idMap
        self._nodes = DAO.getNodes(colore, self._idMap)
        self._grafo.add_nodes_from(self._nodes)
        self.addEdges(anno)

    def addEdges(self,year):
        #faccio un doppio ciclo perchè i nodi sono pochi...
        for v0 in self._nodes:
            for v1 in self._nodes:
                if v0!=v1:
                    pesoInt=0
                    peso = list()
                    #la funzione getpeso resituisce una lista con il peso contenuto come primo valore
                    # da v0 a v1
                    peso=DAO.getPeso(v0.Product_number,v1.Product_number,year)
                    if len(peso)!=0:#-->controlliamo che ci sia un peso tra i due
                        pesoInt=peso[0]
                        peso.clear()
                    #da v1 a v0
                    peso = DAO.getPeso(v1.Product_number,v0.Product_number,year)
                    if len(peso)!=0:
                        pesoInt+=peso[0]
                        peso.clear()
                    if pesoInt!=0:#creo un arco solo se il peso tra i due è diverso da 0 come da specifiche dell'esercizio
                        self._grafo.add_edge(v0,v1,weight=pesoInt)

    def getPesoMaggiore(self):
        edges=list(self._grafo.edges(data=True))
        edges.sort(key=lambda x: x[2]["weight"], reverse=True)
        return edges
    def printGraphDetails(self):
        print(f"Num nodi: {len(self._grafo.nodes)}")
        print(f"Num archi: {len(self._grafo.edges)}")

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)
