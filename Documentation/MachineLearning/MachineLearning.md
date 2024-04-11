
# Machine Learning

L'objectif de ce module de SAE est de générer les sentiments liés à du texte. Ce sentiment peut-être positif ou négatif. Notre objectif est de récupérer les avis laissés par les utilisateurs sur Google Maps pour prédire leur sentiment. Nous avons donc décidé d'utiliser la méthode de régression logistique.

Pour récupérer les avis, on utilise le framework Selenium. Une fois les avis récupérés, nous les enregistrons dans un fichier CSV puis on charge notre modèle de machine learning sur ces avis afin de prédire le sentiment. Il nous alors plus qu'à afficher le résultat à l'utilisateur.


## Badges

[![IUT](https://img.shields.io/badge/University-IUT&nbsp;de&nbsp;Vélizy-yellow)](https://www.iut-velizy-rambouillet.uvsq.fr/)
[![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)](https://www.debian.org/)
[![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white)](https://www.mozilla.org/en-US/firefox/new/)
[![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)


## Auteurs

- Erwan

Groupe :

- Quentin
- Erwan
- Angelo
- Khaoula

## Installation

Pour fonctionner, ce programme a besoin de plusieurs choses :
- Firefox
- Selenium
- plusieurs import pour python

Voici le code pour les installer :

```bash
  sudo apt-get update
  sudo apt-get install firefox-esr
  pip install selenium
  pip install pandas
  pip install scikit-learn==1.0.1
```
    
## Documentation

### MapScrapSelenium

Pour scraper les données, nous avons choisi d'utiliser Sélénium, car Google Maps est une page dynamique chargée avec du JavaScript. Avec les outils BeautifulSoup, Scrapy ou autres méthodes, nous serions confrontées à un problème de balises nous disponibles car ces outils scrapent la page HTML de base, donc s'il y a un appel de fichier JavaScript pour ajouter du contenu, celui-ci ne sera pas pris en compte.

Le code se présente en plusieurs parties :
- Les imports
- La déclaration des variables
- La fonction recherche()
- La partie d'exécution du code  

Nous avons choisi de faire notre scrapping sur Google Maps car les avis sont écrits par des utilisateurs. Nous avons utilisé un dataset pour Tweeter et comme les avis Google Maps sont écrit par la communauté, cela revient au même. Google Maps nous semblait original et une bonne idée. Nous cherchons également des avis en temps réel et l'utilisateur peut choisir librement l'établissement dont il veut récupérer les avis.  

C'est dans la fonction recherche() qui fait la plus grosse partie du travail. Elle va rentrer dans le champ de recherche de Maps le lieu que l'utilisateur a rentré, si plusieurs établissements sont trouvés, elle va cliquer sur le premier et ensuite elle va cliquer sur 'Avis' puis récupérer les avis laissés pour les rentrer dans le CSV qui portera le nom de la recherche de l'utilisateur.

Pour lancer Firefox sur le lien de Google Maps, on utilise le code suivant :
```python
driver = webdriver.Firefox(options=options)
  driver.get(URL)
```
options=options permet de mettre en paramètre les options rentrées précédemment et qui sert a lancer le programme en arrière-plan.

Ce qui permet de récupérer les différents éléments sur la page web sont les lignes suivantes :
```python
plusBtn = driver.find_elements("xpath", "//button[@class='w8nwRe kyuRq']")
```
Ici, ont stock dans la variable 'plusBtn' tous les éléments de type button avec la classe 'w8nwRe kyuRq'. Une fois cela fait, on va cliquer dessus pour afficher l'entièreté des avis.
```python
for plus in plusBtn:
  plus.click()
```

### loadModel
Dans ce programme python, nous utilisons le modèle généré par notre Notebook ainsi que le fichier CSV créé par *MapScrapSelenium.py*. On utilise donc le modèle pour prédire le sentiment de l'avis et nous l'ajoutons dans un CSV qui se présente en deux colonnes comme dans l'exemple ci-dessous :
|avis                  |sentiment   |
|----------------------|------------|
|Service impeccable et rapide ! Nous avions besoin de renouvellement + création de passeport/CNI pour plusieurs personnes.1 mois seulement de délai pour obtenir un RDV. Une fois sur place, on n'a même pas eu le temps de s'asseoir en salle d'attente, on a été reçu immédiatement. RDV fait en 10 mn. 1 mois après, tout était prêt. Pour les récupérer, pas besoin de RDV, la personne à l'accueil nous prépare le RDV. Temps passé en salle d'attente = moins de 10mn. Récupération de nos papiers en 5mn...super service et filles très gentilles. Bravo pour l'organisation|0           |
|Faudra me dire comment on peut décider de fermer 45mn avant l heure indiquée sur votre site ou en mairie sans aucune autre information ou justification. J ai appelé on m a dit d arriver 20a30mn avant la fermeture . Mais non , trop pressé de partir en week-end. 40mn de voiture pour rien.|0           |
|Très bien reçus par les 2 dames qui se sont occupées de nous. De plus, local très agréable. Bonne année au personnel et merci|1           |
|Petit message : Éviter de mettre des gamines a l’accueil !! Peu comprehensive et pour l’amabilité on repasse!! Afficher bien vos horaires également cela évitera des déconvenues. Bien a vous|1           |
|Très bon accueil, la mairie est très propre, endroit agréable, photomaton, distributeur de café,photos copieuse, Merci pour votre agréable accueil et bonne continuation.|1           |
|Le sourire et l'accueil c'est en option, si encore il. Y avait le service... Ça non plus. Je viens chercher une carte d'identité, je ils l'ont dans la main vous font payer le timbre fiscal puis "non vous devez refaire une démarche car le délais est dépassé de 24h" Alors qu'ils m'ont appelé la veille|0           |
|Mairie très propre et personnel agréable. Merci Monsieur THEVENOT qui est toujours à l’écoute.|1           |
|Merci, bon accueil. Très rapide pour déposer passeport|1           |
|Très bon accueil. Parking externe. Service de  passeport biométrique.|1           |
|Merci à M. Calios pour son accueil sa réactivité et son professionnalisme !|1           |


Pour généré ce fichier on doit tout d'abord charger notre modèle :
```python
with open("GenerationModel/model.pkl", "rb") as f:
    model = pickle.load(f)
```

On charge notre fichier CSV avec nos avis puis on prédit la colonne sentiment :
```python
y_hat = model.predict(df['avis'])
```

On termine par la réécriture du fichier avec la nouvelle colonne :
```python
with open(name, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['avis', 'sentiment']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(y_hat)):
        writer.writerow({'avis': df['avis'][i], 'sentiment': y_hat[i]})
```