# **Recueil des exigences**

### **I./ Chapitre 1 – Objectif et portée**

**(a) Quels sont la portée et les objectifs généraux ?**

L'objectif principal du projet est de mettre en place un serveur qui héberge un site web permettant de réaliser des simulations de calcul en différents domaines avec sa base de données comme par exemple des conversions binaires, du cryptage, des calculs mathématiques, calcul des probas, etc.

**(b) Les intervenants.**

Les principaux intervenant sont l'équipe de développement et le client:

- L'équipe est constitué de 4 personnes: Quentin Rocher, Erwan Barbier, Angelo Larrivière et Khaoula Hajbi.
- Notre client est l'équipe pédagogique de l'iut mais le client référant à qui on envoie les livrables est Mr. Hoguin.

**(c) Qu’est-ce qui entre dans cette portée ? Qu’est-ce qui est en dehors ?**

Notre équipe de développement est mené à respecter quelques exigences : On doit mettre en place un serveur web Apache ou Nginx porté par un Raspberry Pi4 et un serveur SGBD. Et l'application doit être programmée en php et mysql.

### **II./ Chapitre 2 – Terminologie employée / Glossaire**

### **III./ Chapitre 3 – Les cas d’utilisation**

**(a) Les acteurs principaux et leurs objectifs généraux.**

L'application Web a essentiellement trois acteurs : le visiteur , l'utilisateur et le gestionnaire. Chacun de ces acteurs ont un objectif différent.

- Le visiteur : accède seulement à la page d’accueil (qui contient un texte et une vidéo de démonstration des fonctionnalités) et à un formulaire d’inscription validé avec un captcha.
- L’utilisateur : se connecte et accède aux différents menus de simulation ou à son profil où il peut changer son mot de passe, puis il se déconnecte.
- Le gestionnaire : se connecte et accède à la page des simulations ainsi qu'à une page de gestion des utilisateurs à partir de laquelle il peut consulter l'historique et ses statistiques, supprimer un ou des utilisateurs. Il a un sign out pour se déconnecter.

**(b) Les cas d’utilisation métier (concepts opérationnels).**

Les principaux opérations que les acteurs peuvent faire :

- Visiter le site
- Visualiser la vidéo
- Résoudre le captcha
- S'inscrire
- Se connecter
- Lancer une simulation
- Changer le mot de passe
- Consulter l'historique de l'application et ses statistiques
- Supprimer un ou des utilisateurs.
- Se déconnecter

**(c) Les cas d’utilisation système.**

- Afficher le site, les texte, la vidéo, les différentes pages de l'application.
- Cliquer sur les boutons (connexion, s'inscrire, déconnexion, compte, valider,...)
- Valider le captcha
- Afficher le résultat des simulations
- Sélectionner les catégories, la simulation, les utilisateurs à supprimer, etc.
- Redirection vers les autres pages

### **IV./ Chapitre 4 – La technologie employée**

**(a) Quelles sont les exigences technologiques pour ce système ?**

- Créer un compte Gitlab
- Programmer l’application en PHP et MySQL
- Installer un serveur web apache
- Installer le serveur sur un Raspberry Pi 4
- Mettre en place un serveur SGBD (MySQL) et la base de données

**(b) Avec quels systèmes ce système s’interfacera-t-il et avec quelles exigences ?**

### **V./ Chapitre 5 – Autres exigences**
