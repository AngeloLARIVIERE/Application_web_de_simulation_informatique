<head>
    <meta charset="utf-8">
    <title>affichage log</title>
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
            <a href="Admin.php"><img class="image" src="../Commun/Icon/LogoSite.png" alt="Logo"></a>
        </div>
    </p>

    <a href="../BaseDeDonnees/Deconnexion.php" class="deconnexion"><img class="icon" src="../Commun/Icon/DeconnectionIcon.svg" alt="account_icon" width="20" height="20"> Déconnexion</a>
<h1 class='titre'>affichage log</h1>




<?php
// Lire le contenu du fichier de log
$logPath = $_POST['path'];

echo"$logPath";

// Lecture du fichier CSV
if (($fichierOuvert = fopen($logPath, "r")) !== FALSE) {
    // Lire la première ligne contenant les noms de colonnes
    if (($donnee = fgetcsv($fichierOuvert, 1000, ",")) !== FALSE) {
        // Commencer la construction du tableau HTML
        echo '<table>';
        echo '<thead><tr>';

        // Afficher les noms de colonnes
        foreach ($donnee as $columnName) {
            echo '<th>' . $columnName . '</th>';
        }

        echo '</tr></thead><tbody>';

        // Lire les lignes suivantes du fichier CSV
        while (($donnee = fgetcsv($fichierOuvert, 1000, ",")) !== FALSE) {
            echo '<tr>';

            // Afficher les valeurs de chaque ligne
            foreach ($donnee as $value) {
                echo '<td>' . $value . '</td>';
            }

            echo '</tr>';
        }

        echo '</tbody></table>';
    }

    fclose($fichierOuvert);
} else {
    echo "Impossible d'ouvrir le fichier CSV.";
}
?>
</body>
