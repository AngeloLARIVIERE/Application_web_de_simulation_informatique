<?php

session_start();
require_once ('../Commun/VariablesGlobal.php');

$date = (new DateTime('NOW'))->format("d/m/Y H:i:s");
$filename = ((new DateTime('NOW'))->format("d_m_Y")).".csv";

function creationFichierLog($filename){
    if (!file_exists("logs/")){mkdir("logs/");}

    if (!file_exists("logs/".$filename)) {
        echo "Le fichier $filename n'existe pas.";
        fputcsv(fopen("logs/".$filename, "a"), array('pseudo', 'Mot_de_passe', 'Date', 'IP_Client', 'IP_Serveur'));
    }
    return fopen("logs/".$filename, "a");
}



//if (isset($_POST['connexion'])) {
//    $pseudo = $_POST['pseudo'];
//    $pass = $_POST['mdp'];
//
//    $conn = mysqli_connect(HOSTNAME, USERNAME, PASSWORD) or die("Impossible de se connecter au serveur");
//
//    mysqli_select_db($conn, DATABASE) or die("Impossible de sélectionner la base de données");
//
//    $table_u = T_UTILISATEUR;
////    $sql = "SELECT * FROM $table_u WHERE pseudo = ?";
////    $stmt = $conn->prepare($sql);
////    $stmt->bind_param('s', $pseudo);
////    $stmt->execute();
////    $result =$stmt->get_result();
//    $bd = new PDO('mysql:host=localhost;dbname=notrebase', USERNAME, PASSWORD) or die("Impossible de se connecter au serveur");
//
//    $table_u = T_UTILISATEUR;
//    $sql = "SELECT * from $table_u where pseudo = '$pseudo' ";
//    $resultat = $bd->prepare($sql);
//    $resultat->execute();
//
//    if ($resultat->rowCount() > 0) {
//        $data = $resultat->fetchAll();
//        if ($pseudo == 'gestionnaire') {
//            if (password_verify($pass, $data["mdp"])) {
//                echo "Connexion gestionnaire";
//                $_SESSION['pseudo'] = $pseudo;
//                header("Location: ../PageGestionnaire/GestionBD.php");
//                exit();
//            }
//            else if ($pseudo == 'admin') {
//                if (password_verify($pass, $data[0]["mdp"])) {
//                    echo "Connexion admin";
//                    $_SESSION['pseudo'] = $pseudo;
//                    header("Location: ../PageAdministrateur/Admin.php");
//                }
//            }
//            else if (password_verify($pass, $data[0]["mdp"])) {
//                echo "Connexion effectuée";
//
//                $_SESSION['pseudo'] = $pseudo;
//                $redirect = "../AccueilSimulation/Simulation.php";
//                header("Location:$redirect");
//                exit();
//            } else {
//                echo "<script>alert('Votre mot de passe est invalide.');
//                window.location.href = '../PagesCompte/PageConnexion/Connexion.html';</script>";
//                $log = creationFichierLog($filename);
//                fputcsv($log,[$pseudo, $pass, $date, $_SERVER['REMOTE_ADDR'], $_SERVER['SERVER_ADDR']]) or die ("impossible d’écrire dans le fichier");
//                fclose($log);
//                exit();
//            }
//        }
//    } else {
//        $log = creationFichierLog($filename);
//        fputcsv($log,[$pseudo, $pass, $date, $_SERVER['REMOTE_ADDR'], $_SERVER['SERVER_ADDR']]) or die ("impossible d’écrire dans le fichier");
//        fclose($log);
//        echo "<script>alert('Ce compte n\'existe pas.');
//        window.location.href = '../PagesCompte/PageConnexion/Connexion.html';</script>";
//        exit();
//    }
//}
if (isset($_POST['connexion'])) {
    $pseudo = $_POST['pseudo'];
    $pass = $_POST['mdp'];

    $bd = new PDO('mysql:host=localhost;dbname=notrebase', USERNAME, PASSWORD) or die("Impossible de se connecter au serveur");

    $table_u = T_UTILISATEUR;
    $sql = "SELECT * from $table_u where pseudo = '$pseudo' ";
    $resultat = $bd->prepare($sql);
    $resultat->execute();

    if ($resultat->rowCount() > 0) {
        $data = $resultat->fetchAll();
        if ($pseudo == 'gestionnaire') {
            if (password_verify($pass, $data[0]["mdp"])) {
                echo "Connexion gestionnaire";
                $_SESSION['pseudo'] = $pseudo;
                header("Location: ../PageGestionnaire/GestionBD.php");
            }
        }else if ($pseudo == 'admin') {
            if (password_verify($pass, $data[0]["mdp"])) {
                echo "Connexion admin";
                $_SESSION['pseudo'] = $pseudo;
                header("Location: ../PageAdministrateur/Admin.php");
            }
        }else if (password_verify($pass, $data[0]["mdp"])) {
            echo "Connexion effectuée";

            $_SESSION['pseudo'] = $pseudo;
            $redirect = "../AccueilSimulation/Simulation.php";
            header("Location:$redirect");
        }else {

            echo "<script>alert('Votre mot de passe est invalide.');
                window.location.href = '../PagesCompte/PageConnexion/Connexion.html';</script>";
            $log = creationFichierLog($filename);
            fputcsv($log, [$pseudo, $pass, $date, $_SERVER['REMOTE_ADDR'], $_SERVER['SERVER_ADDR']]) or die ("impossible d’écrire dans le fichier");
            fclose($log);
        }

    } else {
        $log = creationFichierLog($filename);
        fputcsv($log, [$pseudo, $pass, $date, $_SERVER['REMOTE_ADDR'], $_SERVER['SERVER_ADDR']]) or die ("impossible d’écrire dans le fichier");
        fclose($log);
        echo "<script>alert('Ce compte n\'existe pas.');
            window.location.href = '../PagesCompte/PageConnexion/Connexion.html';</script>";
    }
}

