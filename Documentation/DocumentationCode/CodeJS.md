# Documentation du code php de notre application Web

Groupe de SAE :

- Angelo
- Khaoula
- Erwan
- Quentin

Dans ce docment nous allons expliquer nos fichiers javascript avec leur contenue ainsi que leur place dans notre architecture. Nous avons fait le choix de mettre les fichiers js dans le repértoire dans les quelles ils seront appelées. Peut être que pour le prochain semestre nous les regrouperons dans un dossier qui leur sera propre.


- SupprimerUtilisateur.js

Ce fichier est appelé quand le gestionnaire clique sur le bouton pour supprimer un utilisateur. Ce fichier contient une fonction qui va envoyer l'id de l'utilisateur à supprimer à un fichier php (DeleteUser.php). Ensuite quand le fichier php a fini ces actions notre programme js recharge la page.


- LoiNormale.js 

Ce docuement nous permet de modifier les valeurs du fichier html pour la loi normal. Il a une fonction description qui permet lorsqu'on clique sur un champ du menu pour choisir sa méthode de calcule affiche sa déscription ainsi que la formule associer.  Dès l'ouverture de la page web si aucune méthode n'est sélectionné nous mettons une valeur par défault. Elle utilise un fichier JSON qui est une liste de méthode avec le nom de la methode, sa déscription et sa formule mathématique.
