import tkinter as tk
from tkinter import ttk
from utils import display
from utils import db

class Window(tk.Toplevel):

    # Attributs de la classe (pour être en mesure de les utiliser dans les différentes méthodes)
    treeView = None
    input = None
    errorLabel = None

    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre et des lignes/colonnes
        display.centerWindow(600, 450, self)
        self.title('Q3 : départements pour une région donnée (version dynamique)')
        display.defineGridDisplay(self, 3, 3)
        self.grid_rowconfigure(3, weight=10) #On donne un poids plus important à la dernière ligne pour l'affichage du tableau
        ttk.Label(self, text="On a repris le code de F2. Modifier l'interface pour proposer un choix dynamique de la région (par exemple un menu déroulant avec les valeurs extraites de la base, ou toute autre idée).",
                  wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0,columnspan=3)

        # Affichage du label, de la case de saisie et du bouton valider
        ttk.Label(self, text='Veuillez indiquer une région :', anchor="center", font=('Helvetica', '10', 'bold')).grid(row=1, column=0)
        #TODO Q3 C'est cette partie que l'on souhaite changer pour un choix dynamique de la région
        cursor = db.data.cursor()
        cursor.execute("""SELECT  nom_region
                                            FROM Regions """)
        region =cursor.fetchall()
        options = [row[0] for row in region]


        self.title("Les regions:")
        selected_region = tk.StringVar(self)

        self.dropdown = ttk.Combobox(self, textvariable=selected_region,values=options)
        self.dropdown.grid(row=1,column=1)

        self.dropdown.bind("<<ComboboxSelected>>", self.searchRegion)




        # On place un label sans texte, il servira à afficher les erreurs
        self.errorLabel = ttk.Label(self, anchor="center", font=('Helvetica', '10', 'bold'))
        self.errorLabel.grid(columnspan=3, row=2, sticky="we")


        # On prépare un treeView vide pour l'affichage de nos résultats
        columns = ('code_departement', 'nom_departement',)
        self.treeView = ttk.Treeview(self, columns=columns, show='headings')
        for column in columns:
            self.treeView.column(column, anchor=tk.CENTER, width=15)
            self.treeView.heading(column, text=column)
        self.treeView.grid(columnspan=3, row=3, sticky='nswe')

    # Fonction qui récupère la valeur saisie, exécute la requête et affiche les résultats
    # La fonction prend un argument optionnel event car elle peut être appelée de deux manières :
    # Soit via le bouton Valider, dans ce cas aucun event n'est fourni
    # Soit via le bind qui a été fait sur la case de saisie quand on appuie sur Entrée, dans ce cas bind fournit un event (que l'on utilise pas ici)
    # TODO Q3 Modifier la fonction searchRegion pour un choix dynamique de la région
    def searchRegion(self, event = None):



        # On récupère la valeur saisie dans la case
        region=self.dropdown.get()

        # Si la saisie est vide, on affiche une erreur
        if len(region) == 0:
            self.errorLabel.config(foreground='red', text="Veuillez saisir une région !")



        # Si la saisie contient quelque chose
        else :

            # On essai d'exécuter notre requête
            try:
                cursor = db.data.cursor()
                result = cursor.execute("""SELECT code_departement, nom_departement
                                            FROM Departements JOIN Regions USING (code_region)
                                            WHERE nom_region = ?
                                            ORDER BY code_departement""", [region])

            # S'il y a une erreur, on l'affiche à l'utilisateur
            except Exception as e:
                self.errorLabel.config(foreground='red', text="Erreur : " + repr(e))

            # Si tout s'est bien passé
            else:

                # On affiche les résultats de la requête dans le tableau
                i = 0
                for row in result:
                    self.treeView.insert('', tk.END, values=row)
                    i += 1
                # On affiche un message à l'utilisateur en fonction du nombre de résultats de la requête
                if i == 0:
                    self.errorLabel.config(foreground='orange', text="Aucun résultat pour la région \"" + region + "\" !")
                else :
                    self.errorLabel.config(foreground='green', text="Voici les résultats pour la région \"" + region + "\" :")