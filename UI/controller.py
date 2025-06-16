from logging import disable

import flet as ft

from testModel import maxPathWeight


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model

    def fillDD(self):
        listStores = self.model.passStores()
        for store in listStores:
            self.view.ddStore.options.append(ft.dropdown.Option(key=store[1], text=store[0]))
        self.view.update_page()

    def handleCreaGrafo(self, e):
        self.view.txt_result.clean()
        self.model.createGraph(self.view.ddStoreValue, self.view.txtIntK.value)
        self.view._btnRicorsione.disabled = False
        graph = self.model.graphMO
        nNodes = graph.number_of_nodes()
        nEdges = graph.number_of_edges()
        self.view.txt_result.controls.append(
            ft.Text(f"Numero di vertici: {nNodes} Numero di archi: {nEdges}"))
        for node in graph.nodes():
            self.view.ddNode.options.append(ft.dropdown.Option(key=node, text=node))
        self.view.ddNode.disabled = False
        self.view.update_page()


    def handleCerca(self, e):
        source = self.view.ddNodeValue
        path = self.model.getLongestPathFrom(int(source))
        for element in path:
            self.view.txt_result.controls.append(
                ft.Text(f"{element}"))
        self.view.update_page()

    def handleRicorsione(self, e):
        maxPath, maxPathWeight = self.model.getMaxPath()
        self.view.txt_result.controls.append(
            ft.Text(f"{maxPath}"
                    f"{maxPathWeight}"))
        self.view.update_page()
