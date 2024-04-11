<?php
    require('../../BaseDeDonnees/VerificationSession.php');
?>

<!DOCTYPE html>

<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Modification du mot de passe</title>
    <link rel="icon" href="../../Commun/Icon/FavIcon.ico" type="image/ico">
    <link href="StyleChangeMDP.css" rel="stylesheet" type="text/css">
    <link href="../../Commun/StyleCommun.css" rel="stylesheet" type="text/css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
</head>

<body>
<nav>
    <p class="logo">
    <div class="logo">
        <a href="../../AccueilSimulation/Simulation.php"><img class="image" src="../../Commun/Icon/LogoSite.png" alt="Logo"></a>
    </div>
    </p>

    <!-- Onglet profil -->
    <div class="profil">
        Profile<br />
        <span><a href="" class="lien"><img class="icon" src="../../Commun/Icon/CompteIcon.svg" alt="account_icon" width="20" height="20"> Compte</a></span>
        <span><a href="../../BaseDeDonnees/Deconnexion.php" class="lien"><img class="icon" src="../../Commun/Icon/DeconnectionIcon.svg" alt="account_icon" width="20" height="20"> Déconnexion</a></span>
    </div>
</nav>

<div class="div1">
    <h1>Changer votre mot de passe</h1>
    <form class="formChangeMDP" action="../../BaseDeDonnees/ModifMDP.php" method="post">
        <label for='Amdp' hidden>Amdp</label>
        <input class='ch1' type='password' id='Amdp' name='Amdp' minlength="1" placeholder='Ancien mot de passe' autofocus> <br>
        <label for='Nmdp' hidden>Nmdp</label>
        <input class='ch1' type='password' id='Nmdp' name='Nmdp' minlength="1" placeholder='Nouveau mot de passe'
        pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[<>]).{12,}$"
        title="Critères : au moins 1 majuscule, 1 minuscule, 1 chiffre, 12 caractères minimum"> <br>
        <label for='Nmdp2' hidden>Nmdp2</label>
        <input class='ch1' type='password' id='Nmdp2' name='Nmdp2' minlength="1" placeholder='Nouveau mot de passe'
        pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[<>]).{12,}$"
        title="Critères : au moins 1 majuscule, 1 minuscule, 1 chiffre, 12 caractères minimum"> <br>
        <input class="valider" type='submit' name='ok' value="Valider"> <br><br>
    </form>
</div>

</body>

</html>
