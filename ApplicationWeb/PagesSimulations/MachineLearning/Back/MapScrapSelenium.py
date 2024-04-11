import csv
import sys
import time
import pandas as pd
import pickle
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

# -- VARIABLES --

URL = "https://www.google.fr/maps/"

# -- FONCTION --

def recherche():
    """Récupère des données (avis) sur google Maps
    :return : Création d'un CSV avec une colonne 'avis' avec les avis scrappé.
    """
    options = Options()
    options.add_argument("--headless")
    options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(options=options) # lancement de selenium (sur firefox)

    driver.get(URL)
    time.sleep(0.2)

    driver.find_element("xpath", "//button[@aria-label='Tout refuser']").click()  # Accepter cookie google

    searchBar = driver.find_element("xpath", "//input[@id='searchboxinput']") # Champ de saisie
    searchBar.send_keys(rechercheU) # Ecriture de la recherche utilisateur dans la barre de recherche
    driver.find_element("xpath", "//button[@id='searchbox-searchbutton']").click() # Bouton loupe
    time.sleep(3)

    try:
        driver.find_element("xpath", "//a[@class='hfpxzc']").click() # Bouton recherche quand plusieurs etablissement disponible
        time.sleep(1)
        driver.find_element("xpath", "//button[@class='hh2c6 ']").click() # Bouton avis fenetre en plus
        time.sleep(2)
    except NoSuchElementException:
        print("Il n'y a pas plusieurs trucs")
        try:
            driver.find_element("xpath", "//button[@class='hh2c6 ']").click() # Bouton avis recherche exacte
            time.sleep(2)
        except NoSuchElementException:
            print("Il n'y a pas 1 seul truc")

    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    except NoSuchElementException:
        print("Scroll impossible")

    plusBtn = driver.find_elements("xpath", "//button[@class='w8nwRe kyuRq']")
    for plus in plusBtn:
        plus.click()

    time.sleep(1)

    with open('../Front/RecherchesEffectuees/' + rechercheU + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['avis']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        try:
            elements = driver.find_elements("xpath", "//div[@class='MyEned']")
        except NoSuchElementException:
            print("Pas d'avis trouvés")

        for avis in elements:
            writer.writerow({'avis': avis.text})
    time.sleep(2)
    driver.close()


# -- CODE D'EXECUTION --
# rechercheU = input("Entrez votre recherche : ")
rechercheU = str(sys.argv[1]) #On récupère le premier argument (indice 0) qui est lieu
recherche()
print('Recherche Terminée')

# Chargement du model
with open("../Back/model.pkl", "rb") as f:
    model = pickle.load(f)

# Chargement du CSV
name = "../Front/RecherchesEffectuees/" + rechercheU + ".csv"
df = pd.read_csv(name, delimiter=";", encoding='utf-8')
# print(df)

# Prédiction sur les avisdu CSV
y_hat = model.predict(df['avis'])

# Enregistrement dans un nouveau CSV
with open(name, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['avis', 'sentiment']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(y_hat)):
        writer.writerow({'avis': df['avis'][i], 'sentiment': y_hat[i]})
# 0 = negative, 1 = positive

print('CSV fini')