<?php
require_once ('../../../BaseDeDonnees/VerificationSession.php');
require_once ('../../../Commun/VariablesGlobal.php');

// Appel de la fonction getIDHitorique qui est dans VariablesGlobal.php
$Id_m=getIDModule('Logistique régression');

// Appel de la fonction ajoutStatistique qui est dans VariablesGlobal.php
ajoutStatistique($Id_m, 'nb_gens');

?>

<!DOCTYPE html>

<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Simulation de machine learning</title>
    <link rel="icon" href="../../../Commun/Icon/FavIcon.ico" type="image/ico">
    <link href="StyleML.css" rel="stylesheet" type="text/css">
    <link href="../../../Commun/StyleCommun.css" rel="stylesheet" type="text/css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
    <script src='Chargement.js'> </script>
</head>

<body>
    <nav>
        <div class="titre">
            <h1>Bienvenue dans la simulation de machine learning</h1>
        </div>

        <div class="profil">
            Profile<br />
            <span><a href="../../../PagesCompte/PageModifMDP/ModifMDP.php" class="lien"><img class="icon" src="../../../Commun/Icon/CompteIcon.svg" alt="account_icon" width="20" height="20"> Compte</a></span>
            <span><a href="../../../BaseDeDonnees/Deconnexion.php" class="lien"><img class="icon" src="../../../Commun/Icon/DeconnectionIcon.svg" alt="account_icon" width="20" height="20"> Déconnexion</a></span>
        </div>
        <div class="logo">
            <a href="../../../AccueilSimulation/Simulation.php"><img class="image" src="../../../Commun/Icon/LogoSite.png" alt="Logo"></a>
        </div>
    </nav>
    <br>

    <h2>La Logistique régression : </h2>
    <form method='POST' action='MachineLearningParam.php'>
        <label for='lieu'>Recherche un lieu :</label>
        <input type='text' id='lieu' name='lieu' value="IUT de vélizy">
        <button type='submit' name='confirmer' onclick="chargement()"><image src ='../../../Commun/Icon/Loupe.png'></button>
        <button type='submit' name='supprimer'><image src ='../../../Commun/Icon/cross.png'></button>
    </form>
    <div id="loader"></div>

    <?php
    if (isset($_SESSION['charge'])) {
        if ($_SESSION['charge'] == "vrai"){
            echo "<div >Loading...</div>";
        }
        elseif ($_SESSION['charge'] == "csv"){
            $lieu = $_SESSION["lieu"];
            $fichierCSV = fopen("../Front/RecherchesEffectuees/" . $lieu . ".csv", "r"); // Spécifiez le chemin vers votre fichier CSV

            if ($fichierCSV !== false) {
                $enTetes = fgetcsv($fichierCSV);
                $indexAvis = array_search('avis', $enTetes);
                $indexSentiments = array_search('sentiment', $enTetes);
                $positif = 0;
                $avisTotal = 0;

                echo '<table>';
                echo '<tr><th>Avis</th><th>Sentiment</th></tr>';

                while (($ligne = fgetcsv($fichierCSV)) !== false) {
                    $avisTotal += 1;
                    $avis = $ligne[$indexAvis];
                    $sentiments = $ligne[$indexSentiments];
                    if ($sentiments == 1) {
                        $sentimentTexte = "<p style='color: green'><b> positif </b></p>";
                        $positif +=1;
                    } elseif ($sentiments == 0) {
                        $sentimentTexte = "<p style='color: red'><b> négatif </b></p>";
                    }

                    echo '<tr>';
                    echo '<td>' . $avis . '</td>';
                    echo '<td>' . $sentimentTexte . '</td>';
                    echo '</tr>';
                }

                echo '</table>';
                echo "<h1>Positif : ".round(($positif/$avisTotal)*100,2) ."%</h1>";
                echo "<h1>Négatif : ". round(100 - (($positif/$avisTotal)*100), 2) ."%</h1>";

                fclose($fichierCSV);
            } else {
                echo 'Impossible d\'ouvrir le fichier CSV.';
            }
    }
    else{
        echo "<h2>Faite une recherche pour afficher les données</h2>";
    }
}