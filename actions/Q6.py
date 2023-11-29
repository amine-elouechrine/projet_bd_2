import tkinter as tk
from utils import display
from tkinter import ttk
from utils import db
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(600, 400, self)
        self.title('Q6 : Graphique correlation temperatures minimales - coût de travaux (Isère / 2022)')
        display.defineGridDisplay(self, 2, 1)
        ttk.Label(self, text="""Pour l’Isère et l'année 2022, donner deux courbes sur le même graphique  :
        - par mois, l’évolution de la moyenne des températures minimales
        - par mois, l’évolution des totaux de coûts de travaux tout type confondu""",
                  wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0)
        query="""SELECT AVG(temperature_min_mesure) AS moyenne_temperature, strftime('%Y-%m', date_mesure) AS mois
                    FROM Mesures
                    WHERE code_departement = 38 AND strftime('%Y', date_mesure) = '2022'
                    GROUP BY strftime('%Y-%m', date_mesure);"""

        query2=""""""
        # Extraction des données et affichage dans le tableau
        result = []
        self.title('F5 : températures en isère en 2020')
        try:
            cursor = db.data.cursor()
            result = cursor.execute(query)
        except Exception as e:
            print("Erreur : " + repr(e))

        tab_temp_min = []
        tab_x = []
        tab_cout_tot = []


        for row in result:
            tab_temp_min.append(row[0])
            tab_x.append(row[1])

        # Formatage des dates pour l'affichage sur l'axe x
        datetime_dates = [datetime.strptime(date, '%Y-%m') for date in tab_x]

        # Ajout de la figure et du subplot qui contiendront le graphique
        fig = Figure(figsize=(10, 6), dpi=100)
        plot1 = fig.add_subplot(111)

        # Affichage des courbes
        plot1.plot(range(len(datetime_dates)), tab_temp_min, color='g', label='temp min')

        # Ajouter ces lignes après la création du graphique pour définir les étiquettes sur l'axe x
        plot1.set_xticks(range(len(datetime_dates)))  # Définir les emplacements des marqueurs
        plot1.set_xticklabels(tab_x, rotation=45)

        # Affichage du graphique
        canvas = FigureCanvasTkAgg(fig,  master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)
'''
requete sql par rapport a l'evolution de la moyenne des temperatures minimales

SELECT  AVG(temperature_min_mesure) AS moyenne_temperature, strftime('%Y-%m', date_mesure) AS mois
FROM Mesures
Where code_departement=38 and strftime('%Y')
GROUP BY strftime('%Y-%m', date_mesure);'''
