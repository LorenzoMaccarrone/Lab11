import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        # riempio il dd dei colori
        colors = self._model.getColors()
        for c in colors:
            self._view._ddcolor.options.append(ft.dropdown.Option(text=c), )


    def handle_graph(self, e):
        #converto la stringa del'anno in numero
        nStr = self._view._ddyear.value
        try:
            n = int(nStr)
        except ValueError:
            self._view.txtOut.controls.append(
                ft.Text("Si è verificato un problema con la conversione dell'anno"))
            self._view.update_page()
            return
        self._model.createGraph(n,self._view._ddcolor.value)
        self._view.txtOut.controls.append(
            ft.Text("Il grafo è stato creato correttamente"))
        self._view.txtOut.controls.append(
            ft.Text(f"Il grafo ha {self._model.getNumNodi()} nodi e {self._model.getNumArchi()} archi "))
        coppiePesoMaggiore=self._model.getPesoMaggiore()
        i = 0
        for a in coppiePesoMaggiore:
            if i!=3:
                self._view.txtOut.controls.append(
                    ft.Text(f"Arco da {a[0]} a {a[1]} con peso {a[2]["weight"]} "))
                i+=1
        self._view.update_page()




    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
