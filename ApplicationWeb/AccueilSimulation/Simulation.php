<?php
require_once ('../BaseDeDonnees/VerificationSession.php')
?>

<!DOCTYPE html>

<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Accueil simulation</title>
    <link rel="icon" href="../Commun/Icon/FavIcon.ico" type="image/ico">
    <link href="StyleAccueilSimulation.css" rel="stylesheet" type="text/css">
    <link href="../Commun/StyleCommun.css" rel="stylesheet" type="text/css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
</head>

<body>
    <nav>
        <p class="logo">
            <div class="logo">
                <img class="image" src="../Commun/Icon/LogoSite.png" alt="Logo">
            </div>
        </p>

        <!-- Onglet profil -->
        <div class="profil">
            Profile<br />
            <span><a href="../PagesCompte/PageModifMDP/ModifMDP.php" class="lien"><img class="icon" src="../Commun/Icon/CompteIcon.svg" alt="account_icon" width="20" height="20"> Compte</a></span>
            <span><a href="../BaseDeDonnees/Deconnexion.php" class="lien"><img class="icon" src="../Commun/Icon/DeconnectionIcon.svg" alt="account_icon" width="20" height="20"> Déconnexion</a></span>
        </div>
        
        </nav>

    <?php
    echo "<h1 class='bv'>Bonjour ";
    echo $_SESSION['pseudo'];
    echo "</h1>"
    ?>
        
        <hr>

        <div class="categorie">
            <p class="p_cat"><img class="icon" src="../Commun/Icon/FiltreIcon.svg" alt="account_icon" width="20" height="20"> Catégories</p>
        </div>
        
        <div class='tb_sim'>
            <div class='sim1'><button class="blockProba" onclick="window.location.href='../PagesSimulations/LoiNormale/Front/PageLoiNormale.php'">Probabilité</button></div>
            <div class='sim1'><button class="blockMachineLearning" onclick="window.location.href='../PagesSimulations/MachineLearning/Front/PageMachineLearning.php'">Machine Learing</button></div>
            <div class='sim1'><button class="block" onclick="window.location.href='../404/Page404.html'">Autre Simulation</button></div>
            <div class='sim1'><button class="block" onclick="window.location.href='../404/Page404.html'">Autre Simulation</button></div>
            <div class='sim1'><button class="block" onclick="window.location.href='../404/Page404.html'">Autre Simulation</button></div>
            <div class='sim1'><button class="block" onclick="window.location.href='../404/Page404.html'">Autre Simulation</button></div>
        </div>
</body>

</html>
