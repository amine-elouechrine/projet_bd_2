import tkinter as tk
from tkinter import ttk
from utils import display

class Window(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(800, 500, self)
        self.title('Consultation des données de la base')
        display.defineGridDisplay(self, 1, 1)

        # Définition des onglets
        #TODO Q4 Créer des nouveaux onglets pour les nouvelles tables
        tabControl = ttk.Notebook(self)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)
        tab5 = ttk.Frame(tabControl)
        tab6 = ttk.Frame(tabControl)
        tab7 = ttk.Frame(tabControl)
        tab8 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Mesures (1000 1ères valeurs)')
        tabControl.add(tab2, text='Départements')
        tabControl.add(tab3, text='Régions')
        tabControl.add(tab4, text='Communes')
        tabControl.add(tab5, text='Traveaux ')
        tabControl.add(tab6, text='Isolation')
        tabControl.add(tab7, text='Chauffage')
        tabControl.add(tab8, text='Photovoltaique')
        display.defineGridDisplay(tab1, 1, 2)
        display.defineGridDisplay(tab2, 1, 2)
        display.defineGridDisplay(tab3, 1, 2)
        display.defineGridDisplay(tab4, 1, 2)
        display.defineGridDisplay(tab5, 1, 2)
        display.defineGridDisplay(tab6, 1, 2)
        display.defineGridDisplay(tab7, 1, 2)
        display.defineGridDisplay(tab8, 1, 2)
        tabControl.grid(row=0, column=0, sticky="nswe")

        # Mesures
        columns = ('code_departement', 'date_mesure', 'temperature_min_mesure', 'temperature_max_mesure', 'temperature_moy_mesure')
        query = """
            SELECT code_departement, date_mesure, temperature_min_mesure, temperature_max_mesure, temperature_moy_mesure
            FROM Mesures
            ORDER BY date_mesure
            LIMIT 1,1000
        """
        tree = display.createTreeViewDisplayQuery(tab1, columns, query)
        scrollbar = ttk.Scrollbar(tab1, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(row=0, sticky="nswe")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Départements
        columns = ('code_departement', 'nom_departement', 'code_region', 'zone_climatique')
        query = """
            SELECT code_departement, nom_departement, code_region, zone_climatique
            FROM Departements
            ORDER BY code_departement
        """
        tree = display.createTreeViewDisplayQuery(tab2, columns, query, 200)
        scrollbar = ttk.Scrollbar(tab2,orient='vertical',command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(row=0, sticky="nswe")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Régions
        columns = ('code_region', 'nom_region')
        query = """
            SELECT code_region, nom_region
            FROM Regions
            ORDER BY code_region
        """
        tree = display.createTreeViewDisplayQuery(tab3, columns, query, 250)
        scrollbar = ttk.Scrollbar(tab3,orient='vertical',command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(row=0, sticky="nswe")
        scrollbar.grid(row=0, column=1, sticky="ns")

        #traveaux
        columns = ('id_traveaux','cout_total_ht','cout_induit_ht','annee_traveaux','type_logement','annee_construction_logement','code_departement','code_region')
        query = """
            SELECT *
            FROM Traveaux
            ORDER BY  annee_traveaux
        """
        tree = display.createTreeViewDisplayQuery(tab5, columns, query, 200)
        scrollbar = ttk.Scrollbar(tab3, orient='verical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(row=0, sticky="nswe")
        scrollbar.grid(row=0, column=1, sticky="ns")

        #Communes
        columns = ('code_commune','code_departement','nom_commune','statue','altitude','population','supefecie','code_canton','code_arrondissement')
        query = """
            SELECT *
            FROM Communes
            ORDER BY code_commune
        """
        tree = display.createTreeViewDisplayQuery(tab4, columns, query, 200)
        scrollbar = ttk.Scrollbar(tab3, orient='verical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(row=0, sticky="nswe")
        scrollbar.grid(row=0, column=1, sticky="ns")

        #Isolation
        columns = ('id_traveaux','poste','isolant','epaisseur','surface')
        query = """
            SELECT *
            FROM Isolation
            ORDER BY  id_traveaux
        """
        tree = display.createTreeViewDisplayQuery(tab6, columns, query, 200)
        scrollbar = ttk.Scrollbar(tab3, orient='verical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(row=0, sticky="nswe")
        scrollbar.grid(row=0, column=1, sticky="ns")

        #Chauffage
        columns = ('id_traveaux','energie_avant_traveaux','energie_installe','generateur','type_chaudiere')
        query = """
            SELECT *
            FROM Chauffage
            ORDER BY  id_traveaux
        """
        tree = display.createTreeViewDisplayQuery(tab7, columns, query, 200)
        scrollbar = ttk.Scrollbar(tab3, orient='verical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(row=0, sticky="nswe")
        scrollbar.grid(row=0, column=1, sticky="ns")

        #Photovoltaique
        columns = ('id_traveaux','puissance_installe','type_panneau')
        query = """
            SELECT *
            FROM Photovoltaique
            ORDER BY id_traveaux
        """
        tree = display.createTreeViewDisplayQuery(tab8, columns, query, 200)
        scrollbar = ttk.Scrollbar(tab3, orient='verical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(row=0, sticky="nswe")
        scrollbar.grid(row=0, column=1, sticky="ns")