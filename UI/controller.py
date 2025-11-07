import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    def handler_dropdown_change_museo(self, e):
        self.museo_selezionato = self._view.dd_museo.value

    def handler_dropdown_change_epoca(self, e):
        self.epoca_selezionata = self._view.dd_epoche.value


    # POPOLA DROPDOWN
    # Queste due funzioni verranno chiamate nella View, itererò tra i loro item per popolare il dd_museo e dd_epoche
    def musei_dropdown(self):
        musei = self._model.get_musei()
        return musei

    def epoche_dropdown(self):
        epoche = self._model.get_epoche()
        return epoche

    # Questa funzione viene chiamata in view.mostra_artefatti_btn
    def show_artefatti(self, e):

        museo = self.museo_selezionato
        epoca = self.epoca_selezionata
        if museo and epoca:
            lista_artefatti = self._model.get_artefatti_filtrati(museo, epoca)
            print(len(lista_artefatti))                     # Utilizzo questa funzione per stampare nel terminale il numero di artefatti trovati,
                                                            # mi è utile per verificare che il programma funzioni correttamente, confrontando il risultato
                                                            # ottenuto dalla query su DBeaver

            if lista_artefatti:
                self._view.mostra_artefatti(lista_artefatti)
                self._view.update()
            else:
                self._view.show_alert("La ricerca non ha prodotto nessun risultato.")
        elif not museo or not epoca:
            self._view.show_alert("Inserisci i filtri necessari!")

