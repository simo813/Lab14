import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.DAO = DAO()
        self.graphMO = None
        self.longestPath = None
        self.longestPathLenght = None
        self.maxPath = None
        self.maxPathWeight = None

    def passStores(self):
        listStores = self.DAO.getStores()
        return listStores

    def createGraph(self, storeId, maxDays):
        graph = nx.DiGraph()
        self.graphMO = graph
        nodes = list(self.DAO.getNodes(storeId))
        graph.add_nodes_from(nodes)
        edges = list(self.DAO.getEdge(storeId, maxDays))
        graph.add_weighted_edges_from(edges)

    def getLongestPathFrom(self, source):
        self.longestPath = []
        self.longestPathLenght = 0
        parziale = [source]

        for n in self.graphMO.neighbors(source):
            parziale.append(n)
            self._ricorsione(parziale)
            parziale.pop()

        return self.longestPath

    def _ricorsione(self, parziale):

        for n in self.graphMO.neighbors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                if len(parziale) > self.longestPathLenght:
                    self.longestPathLenght = len(parziale)
                    self.longestPath = copy.deepcopy(parziale)
                self._ricorsione(parziale)
                parziale.pop()

    def getMaxPath(self):
        self.maxPath = []
        self.maxPathWeight = 0
        graph = self.graphMO

        for node in graph.nodes:
            self.recursion(
                node=node,
                partial=[node],
                partialWeight=0,
                weightPrec = None
            )

        return self.maxPath, self.maxPathWeight

    def recursion(self, node, partial, partialWeight, weightPrec):
        graph = self.graphMO

        if partialWeight > self.maxPathWeight:
            self.maxPathWeight = partialWeight
            self.maxPath = copy.deepcopy(partial)  # copia della lista

        for successor in graph.neighbors(node):
            if successor not in partial:
                weight = graph.get_edge_data(node, successor).get('weight', 0)
                if weightPrec is None:
                    partial.append(successor)
                    self.recursion(successor, partial, partialWeight + weight, weight)
                    partial.pop()

                else:
                    if weight < weightPrec:
                        partial.append(successor)
                        self.recursion(successor, partial, partialWeight + weight, weight)
                        partial.pop()



