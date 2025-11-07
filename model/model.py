from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""

        artefatti = self._artefatto_dao.get_artefatti_filtrati(epoca)
        musei = self._museo_dao.get_musei_filtrati(museo)
        lista_artefatti = []
        for museo in musei:
            for artefatto in artefatti:
                if museo.id == artefatto.id_museo:
                    lista_artefatti.append(f"{artefatto.nome} | {museo} | {artefatto.tipologia} | {artefatto.epoca}")
        return lista_artefatti


    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        lista_epoche = []
        artefatti = self._artefatto_dao.get_artefatti()
        for item in artefatti:
            if item.epoca not in lista_epoche:
                lista_epoche.append(item.epoca)
        return lista_epoche


    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        lista_musei = []
        musei = self._museo_dao.get_musei()
        for item in musei:
            if item.nome not in lista_musei:
                lista_musei.append(item.nome)
        return lista_musei


