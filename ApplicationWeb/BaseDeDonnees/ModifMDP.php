<?php
session_start();
require_once ('../Commun/VariablesGlobal.php');

if (isset($_POST['Amdp'],
    $_POST['Nmdp'],
    $_POST['Nmdp2'])) {
    foreach ($_POST as $k => $v) {
        $$k = $v;
    }

    $pseudo = $_SESSION['pseudo'];

    $token = (bool)($connexion = mysqli_connect(HOSTNAME, USERNAME, PASSWORD));
    // je verifie ma connexion
    if ($token) {
        $token2 = ($bd = mysqli_select_db($connexion, DATABASE));
        if ($token2) {
            // hashage mdp
            $AmdpC = password_hash($Amdp, PASSWORD_DEFAULT);
            $NmdpC = password_hash($Nmdp, PASSWORD_DEFAULT);
            $Nmpd2C = password_hash($Nmdp2, PASSWORD_DEFAULT);

            $conn = mysqli_connect(HOSTNAME, USERNAME, PASSWORD) or die("Impossible de se connecter au serveur");
            $bd = new PDO('mysql:host=localhost;dbname=notrebase', USERNAME, PASSWORD) or die("Impossible de se connecter au serveur");

            mysqli_select_db($conn, DATABASE) or die("Impossible de sélectionner la base de données");
        
            $table_u = T_UTILISATEUR;

            $sql = "SELECT * from $table_u where pseudo = '$pseudo' ";
            $resultat = $bd->prepare($sql);
            $resultat->execute();

            if ($resultat->rowCount() > 0) {
                $data = $resultat->fetchAll();
                if (password_verify($Amdp, $data[0]["mdp"])) {
                    if ($Nmdp == $Nmdp2){
                        // requetes prepares de la modification du MDP :
                        $sql = "UPDATE $table_u SET mdp = ? WHERE pseudo = ?;";
                        $sqlp = mysqli_prepare($connexion,$sql);
                        mysqli_stmt_bind_param($sqlp,'ss',$NmdpC, $pseudo);
                        mysqli_stmt_execute($sqlp);
                        echo "<script>
                        alert('Mot de passe modifié.');
                        window.location = '../PagesCompte/PageModifMDP/ModifMDP.php';
                        </script>";
                    }else {
                     echo "<script>
                     alert('Erreur : Les mots de passe ne correspondent pas !');
                     window.location = '../PagesCompte/PageModifMDP/ModifMDP.php';
                     </script>";
                     }
                } else {
                echo "<script>
                alert('Erreur : Le mot de passe actuel ne correspond pas !');
                window.location = '../PagesCompte/PageModifMDP/ModifMDP.php';
                </script>";
                }
            }

    }else {
        echo "<script>
               alert('Erreur de connexion à la BD !');
               window.location = '../PagesCompte/PageModifMDP/ModifMDP.php';
            </script>";
    }
}
}