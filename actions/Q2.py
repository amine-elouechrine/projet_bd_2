import tkinter as tk
from utils import display
from tkinter import ttk

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(600, 400, self)
        self.title('Q2 : département le plus froid par région')
        display.defineGridDisplay(self, 2, 1)

        columns = ('nom_region','nom_departement','temperature_min_mesure')
        query = """SELECT R.nom_region,D.nom_departement AS departement_plus_froid,M.temperature_min_mesure AS temperature_minimale
                    FROM  Regions R JOIN Departements D ON R.code_region = D.code_region
                    JOIN Mesures M ON D.code_departement = M.code_departement
                    GROUP BY R.nom_region, D.nom_departement
                    HAVING M.temperature_min_mesure = MIN(M.temperature_min_mesure);"""
        
        tree = display.createTreeViewDisplayQuery(self, columns, query,200)
        tree.grid(row=0, sticky="nswe")
        
    
        #TODO Q2 Modifier la suite du code (en se basant sur le code de F1) pour répondre à Q2

        # On définit les colonnes que l'on souhaite afficher dans la fenêtre et la requête

        # On utilise la fonction createTreeViewDisplayQuery pour afficher les résultats de la requête
