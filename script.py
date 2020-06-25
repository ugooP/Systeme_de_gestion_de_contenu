# -*- coding: utf-8 -*-

# -----------------------------------------------------------------
# fonctions
# -----------------------------------------------------------------

def exportation_pages_web():
    """Cette fonction a pour but de créer un nouveau dossier dans lequel
    les pages web créées par l'utilisateur se trouverons ainsi que de
    ramener les images du modèle sélectionner dans ce dossier""" 
    
    # Importation du module shutil
    import shutil

    # Création du nouveau dossier et imporation des images du modèle choisi
    try:
        shutil.copytree(src="Modeles/" + modele_nb + "/img/", dst='Mes pages web/' + modele_nb + '/img')
    except:
        print("dossier déjà créé")
    
    # Lancement de la fonction de modification de fichier HTML
    modif_fichier_html()

def modif_fichier_html():
    """Cette fonction a pour but de mofifier le contenu d'un fichier HTML grâce à des
    variables rentrées préalablement par l'utilisateur"""
    
    # Enregistrement des lignes du fichier HTML dans une variable
    page_html = open("Modeles/"+ modele_nb +"/index.html", "r")
    lignes = page_html.readlines()
    page_html.close()

    # Modification des lignes consernées
    lignes[10] = "      <h1>" + titre1.get() + "</h1>\n"
    lignes[20] = "      <h1>" + titre2.get() + "</h1>\n"
    lignes[32] = "          <p>" + para_services.get() + "</p>\n"
    lignes[37] = "          <p>" + para_actu.get() + "</p>\n"
    lignes[43] = "          <p>" + para_propos.get() + "</p>\n"
    lignes[49] = "          <p>" + para_contact.get() + "</p>\n"
    lignes[54] = "          <li><a href=" + lien_linkedin.get() + " target='_blank'><img src='img/logo_linkedin.svg'></a></li>\n"
    lignes[55] = "          <li><a href=" + lien_facebook.get() + " target='_blank'><img src='img/logo_facebook.svg'></a></li>\n"
    lignes[56] = "          <li><a href=" + lien_twitter.get() + " target='_blank'><img src='img/logo_twitter.svg'></a></li>\n"
    lignes[57] = "          <li><a href=" + lien_instagram.get() + " target='_blank'><img src='img/logo_instagram.svg'></a></li>\n"

    # Enregistrement du nouveau fichier HTML
    page_html = open("Mes pages web/"+ modele_nb +"/index.html", "w")
    page_html.writelines(lignes)
    page_html.close()

    # Lancement de la fonction de modification de fichier CSS
    modif_fichier_css()

def modif_fichier_css():
    """Cette fonction a pour but de mofifier le contenu d'un fichier CSS grâce à des
    variables Choisies préalablement par l'utilisateur"""

    # Enregistrement des lignes du fichier CSS dans une variable
    page_css = open("Modeles/"+ modele_nb +"/style.css", "r")
    lignes = page_css.readlines()
    page_css.close()
    
    # Modification des lignes consernées
    lignes[8] = "    font-family: " + police.get() + ";\n"
    lignes[30] = "   " + style_titre1.get() + "\n"
    lignes[63] = "   " + style_titre2.get() + "\n"

    # Enregistrement du nouveau fichier CSS
    page_css = open("Mes pages web/"+ modele_nb +"/style.css", "w")
    page_css.writelines(lignes)
    page_css.close()

    # Lancement de la fonction de validation
    msg_validation()

def msg_validation():
    """Cette fonction a pour but de confirmer à l'utilisateur
    que sa page web a bien été créée"""

    msg.configure(text = "Votre page web a bien été créée !\nVous pouvez la retrouver dans le dossier\n'Mes pages web'")

def modele1():
    """Cette fonction à pour but de fournir les variables nécessaires à la fenêtre 1
    afin que l'utilisateur puisse modifier le modèle 1"""

    global modele_nb
    global modele_path
    modele_nb ='m1'
    modele_path = 'f1_screenshot_m1'
    fenetre2.destroy()

def modele2():
    """Cette fonction à pour but de fournir les variables nécessaires à la fenêtre 1
    afin que l'utilisateur puisse modifier le modèle 2"""

    global modele_nb
    global modele_path
    modele_nb ='m2'
    modele_path = 'f1_screenshot_m2'
    fenetre2.destroy()

def modele3():
    """Cette fonction à pour but de fournir les variables nécessaires à la fenêtre 1
    afin que l'utilisateur puisse modifier le modèle 3"""

    global modele_nb
    global modele_path
    modele_nb ='m3'
    modele_path = 'f1_screenshot_m3'
    fenetre2.destroy()

# --------------------------------------------------------------------------
# Programme principal
# --------------------------------------------------------------------------

# importation de l'ensemble des modules
from tkinter import *
from random import randrange


# ----------- Fenêtre 2 -----------

# Initialisation de la fenêtre graphique
fenetre2 = Tk()
fenetre2.geometry('800x450+20+40')
fenetre2.title('Choix du modèle')
fenetre2.config(bg = "white")

choix_modele = Label(fenetre2, text = "Choisissez votre modèle")
choix_modele.config(font = "montserrat 14", bg = "white")
choix_modele.grid(row = 0, column = 0, columnspan = 3, pady = 20)

# création du bouton du modèle 1
photo_m1 = PhotoImage(file='screenshots/f2_screenshot_m1.png')
btn_m1 = Button(fenetre2, image=photo_m1, bg = 'white', highlightthickness = 0, command=modele1)
btn_m1.grid(row=1, column=0, padx=40, pady=10)

# création du bouton du modèle 2
photo_m2 = PhotoImage(file='screenshots/f2_screenshot_m2.png')
btn_m2 = Button(fenetre2, image=photo_m2, bg = 'white', highlightthickness = 0, command=modele2)
btn_m2.grid(row=1, column=1, padx=20)

# création du bouton du modèle 3
photo_m3 = PhotoImage(file='screenshots/f2_screenshot_m3.png')
btn_m3 = Button(fenetre2, image=photo_m3, bg = 'white', highlightthickness = 0, command=modele3)
btn_m3.grid(row=1, column=2, padx=20)

# démarrage de la fenêtre 2
fenetre2.mainloop()


# ----------- Fenêtre 1 -----------


# Initialisation de la fenêtre graphique
fenetre1 = Tk()
fenetre1.geometry("+10+10")
fenetre1.title("Créer sa page Web")
fenetre1.config(bg = "white")

# création des widgets Label(), Entry(), et button()
Label(fenetre1, text= "Titre 1 :", bg = "white").grid(row = 0)
Label(fenetre1, text= "Titre 2 :", bg = "white").grid(row = 2)
Label(fenetre1, text= "Paragraphe 'services' :", bg = "white").grid(row = 4)
Label(fenetre1, text= "Paragraphe 'actualité' :", bg = "white").grid(row = 6)
Label(fenetre1, text= "Paragraphe 'a propos' :", bg = "white").grid(row = 8)
Label(fenetre1, text= "Paragraphe 'contact' :", bg = "white").grid(row = 10)
Label(fenetre1, text= "lien Linkedin :", bg = "white").grid(row = 12)
Label(fenetre1, text= "lien Facebook :", bg = "white").grid(row = 14)
Label(fenetre1, text= "lien Twitter :", bg = "white").grid(row = 16)
Label(fenetre1, text= "lien Instagram :", bg = "white").grid(row = 18)

titre1 = Entry(fenetre1, width = 50, bg = "#fcfcfc")
titre2 = Entry(fenetre1, width = 50, bg = "#fcfcfc")
para_services = Entry(fenetre1, width = 50, bg = "#fcfcfc")
para_actu = Entry(fenetre1, width = 50, bg = "#fcfcfc")
para_propos = Entry(fenetre1, width = 50, bg = "#fcfcfc")
para_contact = Entry(fenetre1, width = 50, bg = "#fcfcfc")
lien_linkedin = Entry(fenetre1, width = 50, bg = "#fcfcfc")
lien_facebook = Entry(fenetre1, width = 50, bg = "#fcfcfc")
lien_twitter = Entry(fenetre1, width = 50, bg = "#fcfcfc")
lien_instagram = Entry(fenetre1, width = 50, bg = "#fcfcfc")

titre1.grid(row = 1)
titre2.grid(row = 3)
para_services.grid(row = 5, padx = 20)
para_actu.grid(row = 7, padx = 20)
para_propos.grid(row = 9, padx = 20)
para_contact.grid(row = 11, padx = 20)
lien_linkedin.grid(row = 13, padx = 20)
lien_facebook.grid(row = 15, padx = 20)
lien_twitter.grid(row = 17, padx = 20)
lien_instagram.grid(row = 19, padx = 20)

# Séléction du style du titre 1
Label(fenetre1, text = 'Style du titre 1 :', bg = "white").grid(row = 0, column = 2, columnspan = 2)

style_titre1 = StringVar()

radio1 = Radiobutton(fenetre1, text="Normal", variable=style_titre1, value='font-style: normal;', bg = 'white')
radio1.grid(row = 1, column = 1)
radio1.select()
radio1 = Radiobutton(fenetre1, text="Gras", variable=style_titre1, value='font-weight : 800;', bg = 'white')
radio1.grid(row = 1, column = 2)
radio1.deselect()
radio1 = Radiobutton(fenetre1, text="Italique", variable=style_titre1, value='font-style: italic;', bg = 'white')
radio1.grid(row = 1, column = 3)
radio1.deselect()
radio1 = Radiobutton(fenetre1, text="Souligné", variable=style_titre1, value='text-decoration: underline;', bg = 'white')
radio1.grid(row = 1, column = 4)
radio1.deselect()

# Séléction du style du titre 2
Label(fenetre1, text = 'Style du titre 2 :', bg = "white").grid(row = 3, column = 2, columnspan = 2)

style_titre2 = StringVar()

radio2 = Radiobutton(fenetre1, text="Normal", variable=style_titre2, value='font-style: normal;', bg = 'white')
radio2.grid(row = 4, column = 1)
radio2.select()
radio2 = Radiobutton(fenetre1, text="Gras", variable=style_titre2, value='font-weight : 800;', bg = 'white')
radio2.grid(row = 4, column = 2)
radio2.deselect()
radio2 = Radiobutton(fenetre1, text="Italique", variable=style_titre2, value='font-style: italic;', bg = 'white')
radio2.grid(row = 4, column = 3)
radio2.deselect()
radio2 = Radiobutton(fenetre1, text="Souligné", variable=style_titre2, value='text-decoration: underline;', bg = 'white')
radio2.grid(row = 4, column = 4)
radio2.deselect()

# Séléction de la police
select_police = Label(fenetre1, text = "Police de la page web :", bg = "white")
select_police.grid(row = 6, column = 1, columnspan = 4)

police = StringVar(fenetre1)
police.set("Montserrat")

menu = OptionMenu(fenetre1, police, "Montserrat", "Sans-sérif", "Sérif", "Georgia", "Times New Roman", "Brush Script MT")
menu.grid(row = 7, column = 2, columnspan = 2)

# Bouton de validation
btn1 = Button(fenetre1, text='Créer ma page web', command=exportation_pages_web)
btn1.grid(row = 20)

msg = Label(fenetre1, fg="green")
msg.config(font = "montserrat 9", bg = "white")
msg.grid(row = 21, rowspan = 4)

# création du canvas
model = Canvas(fenetre1, width = 800, height = 750, bg ='white', bd = 0, highlightthickness = 0)
photo = PhotoImage(file ='screenshots/'+ modele_path +'.png')
model.create_image(400, 380, image = photo)
model.grid(row =0, column =5, rowspan =25, padx =1, pady =5)
model.config(bg = "white")

# démarrage de la fenêtre 1
fenetre1.mainloop()
