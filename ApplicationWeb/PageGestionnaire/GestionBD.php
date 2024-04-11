<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Gestionnaire</title>
    <link rel="icon" href="../Commun/Icon/FavIcon.ico" type="image/ico">
    <link href="../Commun/StyleCommun.css" rel="stylesheet" type="text/css">
    <link href="Style_gestionnaire_admin.css" rel="stylesheet" type="text/css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
</head>

<body>
    <p class="logo">
        <div class="logo">
            <a href="../index.html"><img class="image" src="../Commun/Icon/LogoSite.png" alt="Logo"></a>
        </div>
    </p>

    <a href="../BaseDeDonnees/Deconnexion.php" class="deconnexion"><img class="icon" src="../Commun/Icon/DeconnectionIcon.svg" alt="account_icon" width="20" height="20"> Déconnexion</a>

<?php
require ("../BaseDeDonnees/VerificationSession.php");
require_once ('../Commun/VariablesGlobal.php');
echo "<script src='SupprimerUtilisateur.js'> </script>";
$token = (bool)($connexion = mysqli_connect('localhost','user','test'));
// je verifie ma connexion
if($token){
    $token2 = ($bd=mysqli_select_db($connexion, 'notrebase'));
    if($token2){
        $table_user = T_UTILISATEUR;
        $table_mod = T_MODULES;
        $table_stat = T_STATISTIQUE;
        $table_hist = T_HISTORIQUE;
        // requetes sql
        // $sql="select pseudo,nom,prenom,statut from $table_user where pseudo != 'gestionnaire'";
        $sql2="select t1.nom_m,t1.categorie,t2.nb_gens,t2.nb_utilisation from $table_mod t1, $table_stat t2 where t1.id_m = t2.id_s";
        

        // $res = mysqli_query($connexion,$sql);
        $res2 = mysqli_query($connexion,$sql2);
        if (isset($_POST['pseudo'])){
            $pseudoFormUser = $_POST['pseudo'];
        }else{
            $pseudoFormUser = '';   
        }
        if (isset($_POST['pseudoStat'])){
            $pseudoFromStat = $_POST['pseudoStat'];
        }else{
            $pseudoFromStat = '';   
        }
        echo "
        <h1 class='titre'>Bienvenue sur la page Gestionnaire</h1>
        <div class='t_stat'>
        <div class='formulaire'>
        <table>
        <th colspan='6'>Tableau utilisateurs</th>
        <tr>
            <th colspan='6'>
                <form method='POST' action=''>
                <label for='pseudo'>Recherche par Pseudo :</label>
                <input type='text' id='pseudo' name='pseudo'>
                <button type='submit'><image src ='../Commun/Icon/Loupe.png'></button>
                <button type='submit'><image src ='../Commun/Icon/cross.png'></button>
            </th>

        </tr>
        <tr>
            <th> Pseudo </th>
            <th> Nom </th>
            <th> Prénom </th>
            <th> Groupe </th>
            <th>  </th>
        </tr>";

        
        $res = getUserSort($pseudoFormUser,$table_user);

        while($ligne = mysqli_fetch_row($res) ) {
            echo "<tr>";
            foreach ($ligne as $v) {

                echo "<td> " . $v . "</td>";
            }
            echo "
            <td>
            <form class='form1' method='post' action='SupprimerUtilisateur.php'>
            <input class='inputT' type='button' width='50%' id='$ligne[0]' onclick='deletUser($ligne[0])' name='Supprimer' value=''>
            </form>
            </td>
            </tr>";
        };

        echo "</table></div>";
        echo"<div class='formulaire'>";
        echo"<table>";
        echo "
     
        <th colspan='6'>Tableau statistiques</th>
        <tr>
            <th> Module </th>
            <th> Categorie </th>
            <th> Visites </th>
            <th> Utilisations </th>
        </tr>";
        while($ligne = mysqli_fetch_row($res2)) {
            echo "<tr>";
            foreach ($ligne as $v) {

                echo "<td> " . $v . "</td>";
            }
            echo "
            </tr>";
        };
        echo "</table></div>";

        echo"<div class='formulaire'>";
        echo"<table>";
        echo "
        <th colspan='3'>Tableau historique</th>
        <tr>
        <th colspan='3'>
            <form method='POST' action=''>
            <label for='pseudoStat'>Recherche par Pseudo :</label>
            <input type='text' id='pseudoStat' name='pseudoStat'>
            <button type='submit'><image src ='../Commun/Icon/Loupe.png'></button>
            <button type='submit'><image src ='../Commun/Icon/cross.png'></button>
        </th>
        <tr>
            <th> Module </th>
            <th> Utilisateur </th>
            <th> Fait le </th>
        </tr>";

        $res3 = getHistSort($pseudoFromStat);
        $size = 0;
        while($ligne = mysqli_fetch_row($res3) and $size<10) {
            echo "<tr>";
            foreach ($ligne as $v) {

                echo "<td> " . $v . "</td>";
            }
            echo "
            </tr>";
            $size ++;
        };
        echo "</table></div></div>";
    }
}
?>

</body>
</html>
