from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.DAO = DAO()

    def passStores(self):
        listStores = self.DAO.getStores()
        return listStores

    def createGraph(self, storeId, maxDays):
        graph = nx.DiGraph
        nodes = self.DAO.getNodes(storeId)
        graph.add_nodes_from(nodes)

