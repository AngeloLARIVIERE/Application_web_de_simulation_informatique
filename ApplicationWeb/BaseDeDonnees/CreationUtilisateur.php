<?php
session_start();
require_once ('../Commun/VariablesGlobal.php');

if (isset($_POST['ok'],
    $_POST['pseudo'],
    $_POST['nom'],
    $_POST['prenom'],
    $_POST['mdp'],
    $_POST['mdp2'],
    $_POST['captcha'])) {
    // on pourrait verifier si les variables sont bonnes

    foreach ($_POST as $k => $v) {
        $$k = $v;
    }
    $token = (bool)($connexion = mysqli_connect(HOSTNAME
        , USERNAME, PASSWORD));
    // je verifie ma connexion
    $table_u = T_UTILISATEUR;
    if ($token) {
        $token2 = ($bd = mysqli_select_db($connexion, DATABASE));
        if ($token2) {
            $bd = new PDO('mysql:host=localhost;dbname=notrebase', USERNAME, PASSWORD) or die("Impossible de se connecter au serveur");
            $sql = "SELECT * from $table_u where pseudo = '$pseudo' ";
            $resultat = $bd->prepare($sql);
            $resultat->execute();
            if ($resultat->rowCount() ==1) {
                echo "<script>alert('Le pseudo est déjà utilisé');
                window.location.href = '../PagesCompte/PageCreationCompte/CreationCompte.php';</script>";
            }
            else if ($_SESSION['captcha_a'] + $_SESSION['captcha_b'] == $captcha) {
                if ($mdp == $mdp2) {
                    if (strlen($mdp) >= 12) {
                        if (preg_match('/[0-9]/', $mdp) || preg_match('/[a-z]/', $mdp)) {
                            
                            // hashage mdp
                            $mdp = password_hash($mdp, PASSWORD_DEFAULT);
                            // requetes prepares :
                            $sql = "insert into $table_u(pseudo,nom,prenom,mdp) values(?,?,?,?)";
                            $sqlp = mysqli_prepare($connexion, $sql);
                            mysqli_stmt_bind_param($sqlp, 'ssss', $pseudo, $nom, $prenom, $mdp);
                            mysqli_stmt_execute($sqlp);

                            $_SESSION['pseudo'] = $pseudo;
                            $redirect = "../AccueilSimulation/Simulation.php";
                            header("Location:$redirect");
                        } else {
                            echo "<script>
                            alert('Erreur : Le mot de passe ne respecte pas les critères demandés !');
                            window.location = '../PagesCompte/PageCreationCompte/CreationCompte.php';
                            </script>";
                        }
                    } else {
                        echo "<script>
                            alert('Erreur : Le mot de passe ne respecte pas les critères demandés !');
                            window.location = '../PagesCompte/PageCreationCompte/CreationCompte.php';
                            </script>";
                    }
                } else {
                    echo "<script>
                            alert('Erreur : Les mots de passe ne correspondent pas !');
                            window.location = '../PagesCompte/PageCreationCompte/CreationCompte.php';
                            </script>";
                }
            } else {
                echo "<script>
                   alert('Erreur : Le CPATCHA rentré n\'est pas valide !');
                   window.location = '../PagesCompte/PageCreationCompte/CreationCompte.php';
                </script>";
            }
        }
    }
}else{
    header('Location: ../../ApplicationWeb/PagesConnexion/crea_compte.html');
}
