<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Interface Administrateur</title>
    <link rel="icon" href="../Commun/Icon/FavIcon.ico" type="image/ico">
    <link href="../Commun/StyleCommun.css" rel="stylesheet" type="text/css">
    <link href="../PageGestionnaire/Style_gestionnaire_admin.css" rel="stylesheet" type="text/css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
</head>
<body>
<p class="logo">
        <div class="logo">
            <a href="../BaseDeDonnees/Deconnexion.php"><img class="image" src="../Commun/Icon/LogoSite.png" alt="Logo"></a>
        </div>
    </p>

    <a href="../BaseDeDonnees/Deconnexion.php" class="deconnexion"><img class="icon" src="../Commun/Icon/DeconnectionIcon.svg" alt="account_icon" width="20" height="20"> Déconnexion</a>
<h1 class='titre'>Interface Administrateur</h1>

<?php
require ("../BaseDeDonnees/VerificationSession.php");
// Chemin vers le fichier de log
$logPath = '../BaseDeDonnees/logs/';

// Vérification de l'existence du dossier
if (is_dir($logPath)) {
    // Obtenez la liste des fichiers du dossier
    $fichiers = scandir($logPath);
    echo"
    <div class='t_log'>
    <table>
    <th colspan='2'>Tableau logs Journaliers </th>
    <tr>
        <th> log </th>
        <th> supprimer </th>
    </tr>"; 

    // Parcourez la liste des fichiers
    foreach ($fichiers as $fichier) {
        // Affichez le nom du fichier
        if ($fichier != '.' && $fichier != '..') {
            // Affichez le nom du fichier
            $pathComplet = $logPath.$fichier;
            if (is_dir($pathComplet)){
                // si n'est pas un fichier
                $pathComplet = $pathComplet.'/';
                $fichiers2 = scandir($pathComplet);
                echo"<tr><th colspan='2'>tableaux log Mensuelle</th></tr>
                <tr>
                <th> log </th>
                <th> supprimer </th>
                </tr>"; 
                foreach ($fichiers2 as $fichier2) {
                    if ($fichier2 != '.' && $fichier2 != '..') {
                        $pathComplet = $pathComplet.$fichier2;
                        echo"<tr>";
                        echo"<th>
                        <form action='affichageLog.php' method='post'>
                            <input type='text' name='path' value='$pathComplet' hidden>
                            <button type='submit'>$fichier2</button>
                        </form>
                        </th>";
                        echo"<th>
                        <form action='supprimer_logs.php' method='post'>
                            <input type='text' name='path' value= '$pathComplet' hidden >
                            <button type='submit'><image src ='../Commun/Icon/Poubelle.png'></button>
                        </form>
                        </th>";
                        echo  '</tr>';
                    }
                }
            } else {
                // si est un fichier
                echo"<tr>";
                echo"<th>
                <form action='affichageLog.php' method='post'>
                    <input type='text' name='path' value='$pathComplet' hidden>
                    <button type='submit'>$fichier</button>
                </form>
                </th>";
                echo"<th>
                <form action='supprimer_logs.php' method='post'>
                    <input type='text' name='path' value= '$pathComplet' hidden >
                    <button type='submit'><image src ='../Commun/Icon/Poubelle.png'></button>
                </form>
                </th>";
                echo  '</tr>';
            }
        }
    }
    echo'
    </table>
    </div>';
    
}
?>

</body>
</html>
