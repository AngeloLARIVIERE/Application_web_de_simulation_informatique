<?php
session_start();
require_once ('../../../Commun/VariablesGlobal.php');

if (isset($_POST['confirmer'])){
    $lieu = $_POST['lieu'];
    echo "<h1>".$lieu."</h1>";
    $command = "python3 ../Back/MapScrapSelenium.py " . escapeshellarg($lieu);
    exec($command);
    $_SESSION["charge"] = "csv";
    $_SESSION["lieu"] = $lieu;
}

if (isset($_POST['supprimer'])){
    $_SESSION["charge"] = "Faite une recherche pour afficher les données";
}

$pseudo = $_SESSION['pseudo'];

// Appel de la fonction qui ets dans VariablesGlobal.php
$Id_u=getIDUtilisateur($pseudo);

// Appel de la fonction getIDHitorique qui est dans VariablesGlobal.php
$Id_m=getIDModule('Logistique régression');

// Appel de la fonction ajoutStatistique qui est dans VariablesGlobal.php
ajoutStatistique($Id_m, 'nb_utilisation');

// Appel de la fonction ajoutHisorique qui est dans VariablesGlobal.php
ajoutHistorique($Id_u, $Id_m);


header("Location: PageMachineLearning.php");