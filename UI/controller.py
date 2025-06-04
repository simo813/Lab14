import flet as ft


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
        self._model.createGraph(self.view.ddcountryValue, self.view.ddyearValue)
        graph = self._model.graphMO
        nNodes = graph.number_of_nodes()
        nEdges = graph.number_of_edges()
        self.view.txt_result.controls.append(
            ft.Text(f"Numero di vertici: {nNodes} Numero di archi: {nEdges}"))
        self.view.update_page()


    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass
