from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass


    def get_artefatti(self):

        try:
            artefatti = []
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM artefatto")
            for row in cursor:
                id = row['id']
                nome = row['nome']
                tipologia = row['tipologia']
                epoca = row['epoca']
                id_museo = row['id_museo']
                artefatti.append(Artefatto(id, nome, tipologia, epoca, id_museo))
            cnx.close()
        except Exception as e:
            return e
        return artefatti


    def get_artefatti_filtrati(self, nome):
        lista_artefatti = []
        if nome == "Nessun Filtro":
            nome = None     # Trasformo nome in NULL se "Nessun filtro" per fare in modo che COALESCE possa funzionare come si deve
        try:
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM artefatto WHERE epoca = COALESCE(%s, epoca)"""     # COALESCE mi permette di selezionare ogni riga
                                                                                        # della tabella se riceve NULL come parametro
            cursor.execute(query, (nome,))
            for row in cursor:
                id = row['id']
                nome = row['nome']
                tipologia = row['tipologia']
                epoca = row['epoca']
                id_museo = row['id_museo']
                lista_artefatti.append(Artefatto(id, nome, tipologia, epoca, id_museo))
            cnx.close()
        except Exception as e:
            raise e
        return lista_artefatti
