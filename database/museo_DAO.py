import mysql

from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass


    def get_musei(self):

        try:
            musei = []
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM museo")
            for row in cursor:
                id = row['id']
                nome = row['nome']
                tipologia = row['tipologia']
                musei.append(Museo(id, nome, tipologia))
            cnx.close()
        except Exception as e:
            return e
        return musei

    def get_musei_filtrati(self, nome):
        lista_musei = []
        if nome == "Nessun Filtro":
            nome = None     # Trasformo nome in NULL se "Nessun filtro" per fare in modo che COALESCE possa funzionare come si deve
        try:
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM museo WHERE nome = COALESCE(%s, nome)"""    # COALESCE mi permette di selezionare ogni riga
                                                                                 # della tabella se riceve NULL come parametro
            cursor.execute(query, (nome,))
            for row in cursor:
                id = row['id']
                nome = row['nome']
                tipologia = row['tipologia']
                lista_musei.append(Museo(id, nome, tipologia))
            cnx.close()
        except Exception as e:
            raise e
        return lista_musei

