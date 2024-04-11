<?php
session_start();
if (!isset($_SESSION['pseudo'])){
    header('Location:../PagesCompte/PageConnexion/Connexion.html');
}
?>