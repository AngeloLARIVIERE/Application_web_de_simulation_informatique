import os
import csv 
from datetime import datetime
from time import sleep

datem = datetime.today().strftime('%h_%Y')
# merging the files


if os.path.isdir('logs/'):
    list_files = os.listdir('logs/')
    if not os.path.isdir('logs/Mois/'):
        os.mkdir('logs/Mois/')
    if not os.path.isfile('logs/Mois/' + datem + ".csv"):
        with open('logs/Mois/' + datem + ".csv", "a") as moisFile:
            writer = csv.writer(moisFile, dialect="unix")
            writer.writerow(['pseudo', 'Mot_de_passe', 'Date', 'IP_Client', 'IP_Serveur'])
    with open('logs/Mois/' + datem + ".csv", "a") as moisFile:
        writer = csv.writer(moisFile, dialect="unix")
        for fichier in list_files:
            if ".csv" not in fichier:
                continue
            with open('logs/' + fichier, newline='') as csvfile:
                spamreader = csv.DictReader(csvfile)
                for row in spamreader:
                    writer = csv.writer(moisFile, dialect="unix")
                    writer.writerow([row["pseudo"], row["Mot_de_passe"], row["Date"], row["IP_Client"], row["IP_Serveur"]])
            os.remove('logs/' + fichier)


