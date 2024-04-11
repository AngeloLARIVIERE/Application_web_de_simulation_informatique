<?php
require_once ('../Commun/VariablesGlobal.php');

session_start();

$para = (string) $_POST['pseudo'];
$token = (bool)($connexion = mysqli_connect(HOSTNAME, USERNAME, PASSWORD));
// je verifie ma connexion
if ($token) {
    $token2 = ($bd = mysqli_select_db($connexion, DATABASE));
    if ($token2) {
        $table = T_UTILISATEUR;
        // requetes sql
        $sql = "delete from $table where pseudo = '$para'";
        mysqli_query($connexion,$sql);
        header("Location: GestionBD.php");
    }
}
