<?php
// Chemin vers le fichier de log

$logFilePath = $_POST['path'];

// Vérification de l'existence du fichier de log
if (file_exists($logFilePath)) {
    // Suppression du fichier de log
    if (unlink($logFilePath)) {
        header("Location: Admin.php");
    } else {
        echo "Une erreur s'est produite lors de la suppression des logs.";
    }
} else {
    echo "Aucun fichier de log n'existe.";
}
