import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    # Creo una funzione che mi permetta di trasformare la lista artefatti da una stringa ad un testo di Flet,
    # questa funzione verrà poi chiamata in controller.show_artefatti

    def mostra_artefatti(self, lista_artefatti):
        self.lista_artefatti.controls.clear()
        for item in lista_artefatti:
            self.lista_artefatti.controls.append(ft.Text(item))
            self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        musei = self.controller.musei_dropdown()        # Chiamo la funzione di controller che ritorna i musei
        self.dd_museo = ft.Dropdown(label = "Museo",
                                    # Dall'archivio di Flet trovo un modo per unire diverse istruzioni all'interno di Options
                                    options = [ft.dropdown.Option("Nessun Filtro")] + [ft.dropdown.Option(museo) for museo in musei],
                                    width = 400,
                                    on_change = self.controller.handler_dropdown_change_museo)

        epoche = self.controller.epoche_dropdown()      # Chiamo la funzione di controller che ritorna le epoche
        self.dd_epoche = ft.Dropdown(label = "Epoca",
                                     options = [ft.dropdown.Option("Nessun Filtro")] + [ft.dropdown.Option(epoca) for epoca in epoche],
                                     width = 200,
                                     on_change = self.controller.handler_dropdown_change_epoca)

        row = ft.Row(controls = [self.dd_museo, self.dd_epoche],
                     alignment = ft.MainAxisAlignment.CENTER)


        # Sezione 3: Artefatti

        self.lista_artefatti = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        self.mostra_artefatti_btn = ft.ElevatedButton(text = "Mostra Artefatti",
                                                 width = 200,
                                                 on_click = self.controller.show_artefatti)


        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            row,
            ft.Divider(),

            # Sezione 3: Artefatti
            self.mostra_artefatti_btn,
            self.lista_artefatti,
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
