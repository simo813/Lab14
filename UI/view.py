from logging import disable

import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff


        self._page = page
        self._page.title = "TdP Lab 14 - simulazione esame"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.bgcolor = "#ebf4f4"
        self._page.window_height = 800
        page.window_center()
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._txt_name = None
        self._txt_result = None
        self._btnCreaGrafo = None
        self.txtIntK = None
        self.ddStore = None
        self.ddStoreValue = None
        self.ddNode = None
        self.ddNodeValue = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP Lab 14 - simulazione esame", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddStore = ft.Dropdown(label="Store", on_change=self.on_dropdownStore_change)
        self.txtIntK = ft.TextField(label="Numero giorni massimo K")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo)
        cont = ft.Container(self.ddStore, width=250, alignment=ft.alignment.top_left)
        row1 = ft.Row([cont, self.txtIntK, self._btnCreaGrafo], alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)



        self._btnCerca = ft.ElevatedButton(text="Cerca Percorso Massimo",
                                           on_click=self._controller.handleCerca)

        self.ddNode = ft.Dropdown(label="Node", disabled=True, on_change=self.on_dropdownNode_change)
        cont2 = ft.Container(self.ddNode, width=250, alignment=ft.alignment.top_left)
        row2 = ft.Row([cont2, ft.Container(self._btnCerca, width=250)
        ], alignment=ft.MainAxisAlignment.CENTER)

        self._btnRicorsione = ft.ElevatedButton(text="Ricorsione",
                                           on_click=self._controller.handleRicorsione, disabled=True)

        row3 = ft.Row([ft.Container(self._btnRicorsione, width=250)
                       ], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._controller.fillDD()
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def on_dropdownStore_change(self, e):
        self.ddStoreValue = self.ddStore.value
        self.update_page()

    def on_dropdownNode_change(self, e):
        self.ddNodeValue = self.ddNode.value
        self.update_page()

    def update_page(self):
        self._page.update()