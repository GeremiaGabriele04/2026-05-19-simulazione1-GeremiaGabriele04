import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddGenre = None

    def handleCreaGrafo(self, e):
        if self._ddGenre is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione! Seleziona un genere.", color="red")
            )
            self._view.update_page()
            return

        self._model.buildGraph(self._ddGenre.GenreId)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text("Grafo correttamente creato.", color="green")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Contiene {self._model.getNumNodi()} nodi e {self._model.getNumArchi()} archi.")
        )
        self._view.update_page()

    def handleCammino(self,e):
        pass

    def fillDDGenre(self):
        for n in self._model.getListaGeneri():
            self._view._ddGenre.options.append(
                ft.dropdown.Option(data=n,
                                   key=n.Name,
                                   on_click=self._choiceGenre)
            )

    def _choiceGenre(self, e):
        self._ddGenre = e.control.data
