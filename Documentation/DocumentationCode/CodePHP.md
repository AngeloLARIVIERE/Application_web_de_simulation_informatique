**Documentation du code php de notre application Web**
Groupe de SAE : 
- Angelo
- Khaoula
- Erwan
- Quentin

Dans ce document nous allons expliquer nos choix d'implementation ainsi que nos methodes.

Nous allons commencer par vous expliquer notre choix d'architecture. Nous avons décidé de mettre tous nos fichiers php qui interagissent avec notre base de donnée dans le dossier "Base_De_Donnee". 
Nous trouvons que cela est plus simple pour les redirections (tout est au même endroit) aisni en cas de problème nous savon direcement ou chercher  

Nous allons maintenant expliquer ce que font chacun de nos fichiers php. 


- Connexion.php


Ce fichier a pour objectif de se connecter a notre application. Comment cela fonctionne ? On commence par recuperer le pseudo ainsi que le mot de passe de notre utilisateur grâce au formulaire de connexion. Nous etablissons une connexion avec notre serveur de base de donnée où nous allons pouvoir verifier si utilisateur existe dans notre base de donnée. S´il existe nous allons ensuite verifier si son mot de passe correspond bien a celui de notre BD. Il faut savoir que les mots de passe sont tous hachés. Si les informations renseigner par l'utilisateur sont identiques que celles que nous avons trouvé dans notre table, alors on établie la connexion avec sa session et on le redirige vers la page de simulation. Dand le cas où le mot de passe ou le pseudo ne sont pas trouvés en base alors on envoie une pop up informant l'utilisateur du problème. C'est également dans ce fichier que nous créons ou ajoutons les informations dans le fichier de log quand l'utilisateur tente une connexion qui échoue.


-  CreationUser.php


Ce fichier contient le code nous permettant de créer un nouvel utilisateur dans notre base de donnée. Pour créer un nouvel utilisateur nous avons besoin du pseudo, de son mot de passe, de son prénom et de son nom. Toutes ces informations nous sont fournis grâce au formulaire html (crea_compte.php). On commence par créer la connexion avec notre serveur de basse de donnée, ensuite nous hachons le mot de passe donné par l’utilisateur. Nous utilisons une requête sql préparer pour éviter les injections sql (le fait de pouvoir entrer une commande sql dans un champ texte). Une fois l’utilisateur créé, on le redirige sur la page de simulation avec son propre compte. Dans le cas où une erreur se produit, on le redirige vers la page html pour créer son compte et on lui affiche une pop-up expliquant le problème. L'utilisateur doit également valider un CAPTCHA. Avant de faire les actions d'ajout de l'utilisateur dans la base de données, on vérifie que le résultat du CAPTCHA est correct, sinon on affiche un message d'erreur en JavaScript.  


- Crea_compte.php  


Ce fichier est un formulaire pour que l'utilisateur puisse créer un compte. La partie PHP de ce code est la création de 2 variables aléatoire pour le CAPTCHA et la récupération du résultat fourni par l'utilisateur.


- GestionBD.php 


Ce fichier est réservé exclusivement pour le gestionnaire. Son objectif est d’afficher la liste des utilisateurs qui se sont connectés sur l’application. Dans un premier temps nous effectuons une requête sql afin d’avoir le pseudo, le nom, le mot de passe. Nous construisons ensuite un tableau en html nous permettant de visualiser les informations. Dans ce tableau il y a un bouton à chaque ligne pour pouvoir supprimer un utilisateur (appel une fonction JavaScript). 


- DeleteUser.php


Ce fichier est appelé grâce à une requête Ajax (SupprimerUtilisateur.js) qui a pour paramètre le pseudo de l’utilisateur à supprimer. Ensuite on récupère le paramètre, on vérifie la connexion avec le serveur puis on supprime l’utilisateur de notre base de données. 

- Deconnexion.php  


Dans ce fichier, l'objectif est de casser la liaison entre la base de données et l'utilisateur. Pour ce faire on ferme la session SQL de manière à bien déconnecter la personne de la base pour éviter tout problème par la suite. Il faut noter que nous ne supprimons pas les cookies.  


- Simulation.php  


Il s'agit ici du fichier sur lequel l'utilisateur connecté arrive. Nous récupérons la variable pseudo afin d'afficher 'Bonjour [pseudo]' et il peut depuis cette page, accéder aux différents modules qui se trouvent dans des 'div'.

- LoiNormal.php

Ce fichier nous permet de faire la liason entre le code python de la loi normal et la page html où l'utilisateur va entrer les données qui nous interessent tel que La moyenne, l'Ecart type, la borne inferieur et superieur de l interval et le nombre de sous interval. Dans ce fichier nous utilisons aussi le principe de session pour garder en mémoire les données entrée par l'utilisateur. C'est aussi dans ce fichier que nous executons le fichier Loi_Normal.py.

- ModifMDP.php

Ce fichier php noue permet de modifier les mot de passe que nous avons dans notre base de données. Tout d'abord nous recuperons le pseudo de l'utilisateur concerner. Ensuite nous récupérons son ancien mot de passe, le nouveau ainsi que la confirmation du nouveau mot de passe. Après avoir établie la connexion à notre base de données et hacher les mots de passes nous allons pouvoir les comparers. Si l'ancien mot de passe correspond on va préparer notre requête sql pour mettre à jour le mot de passe. Dans le cas où nous avons une erreur nous alertons l'utilisateur à l'aide d'une pop up adapté.
