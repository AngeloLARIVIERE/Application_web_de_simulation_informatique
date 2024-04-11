<?php
require_once ('../../../BaseDeDonnees/VerificationSession.php');
require_once ('../../../Commun/VariablesGlobal.php');

// Appel de la fonction getIDHitorique qui est dans VariablesGlobal.php
$Id_m=getIDModule('loi normale');

// Appel de la fonction ajoutStatistique qui est dans VariablesGlobal.php
ajoutStatistique($Id_m, 'nb_gens');
?>

<!DOCTYPE html>

<html lang="fr">

    <head>
        <meta charset="utf-8">
        <title>Simulation de probabilité</title>
        <link rel="icon" href="../../../Commun/Icon/FavIcon.ico" type="image/ico">
        <link href="StyleLoiNormale.css" rel="stylesheet" type="text/css">
        <link href="../../../Commun/StyleCommun.css" rel="stylesheet" type="text/css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
        <script src="LoiNormale.js"></script>
    </head>

    <body>
        <nav>
            <div class="titre">
                <h1>Bienvenue dans une simulation  de probabilités</h1>
            </div>

            <div class="profil">
                Profile<br />
                <span><a href="../../../PagesCompte/PageModifMDP/ModifMDP.php"><img class="icon" src="../../../Commun/Icon/CompteIcon.svg" alt="account_icon" width="20" height="20"> Compte</a></span>
                <span><a href="../../../BaseDeDonnees/Deconnexion.php"><img class="icon" src="../../../Commun/Icon/DeconnectionIcon.svg" alt="account_icon" width="20" height="20"> Déconnexion</a></span>
            </div>
            <div class="logo">
                <a href="../../../AccueilSimulation/Simulation.php"><img class="image" src="../../../Commun/Icon/LogoSite.png" alt="Logo"></a>
            </div>
        </nav>
        <br>

        <h2>La loi normale : </h2>

        <table class="table1">
            <tr>

                <td class="left"><p class='gros'>Formulaire pour les paramètres nécessaires à la simulation</p>
                <nav>
                    <ul class="menu">
                        <li class="dropdown"><span>Rectangles</span>
                        <div class="dropdown-content">
                            <a href="#" id="2" onclick="description(this.id)" >Rectangles droites</a>
                            <a href="#" id="1" onclick="description(this.id)" >Rectangles médians</a>
                            <a href="#" id="0" onclick="description(this.id)">Rectangles gauches</a>
                        </div>
                        </li>
                        <li><a href="#" id="3" onclick="description(this.id)" >Simpson</a></li>
                        <li><a href="#" id="4" onclick="description(this.id)">Trapèze</a></li>
                    </ul>
                </nav>

                <?php
                if (!isset($_SESSION['result'])) {

                    echo "
                <form class='form1' action='LoiNormaleParam.php' method='post'>
                        <label for='method'>Méthode utilisé : </label>
                        <input class='sansfond' id='method' name='Fct' type='text' required readonly>
                        
                        <label for='M'>Moyenne = </label>
                        <input class='ch1' id='M' type='number' name='M' placeholder='La moyenne' required>
                        
                        <label for='sigma'>Ecart Type = </label>
                        <input class='ch1' type='number' id='sigma' name='Sigma' placeholder='Ecart type' required>
                        
                        <label for='sup'>Borne superieur de l'interval = </label>
                        <input class='ch1' id='sup' type='number' name='B' placeholder='Borne supérieur de l interval' required>
                        
                        <label for='nbInt'>Nombre de sous interval = </label>
                        <input class='ch1' id='nbInt' type='number' name='N' placeholder='Nombre de sous interval' required>

                        <input type='submit' name='confirmer' value='Confirmer'> <br><br>
                    </form>";
                }
                else{
                    $resutlat = $_SESSION["result"];
                    $b = $_SESSION['B'];
                    $n = $_SESSION['N'];
                    $M = $_SESSION['M'];
                    $sigma = $_SESSION['Sigma'];
                    $fct = $_SESSION['Fct'];
                    echo "

                    <form class='form1' action='LoiNormaleParam.php' method='post'>
                        <label for='method'>Méthode utilisé : </label>
                        <input id='method' class='sansfond' name='Fct' value='$fct' required readonly>

                        <label for='M'>Moyenne = </label>
                        <input class='ch1' id='M' type='number' name='M' placeholder='La moyenne' value='$M' required>

                        <label for='sigma'>Ecart Type = </label>
                        <input class='ch1' id='sigma' type='number' name='Sigma' placeholder='Ecart type' value='$sigma' required>

                        <label for='sup'>Borne superieur de l'interval = </label>
                        <input class='ch1' id='sup' type='number' name='B' placeholder='Borne supérieur de l interval' value='$b' required>

                        <label for='nbInt'>Nombre de sous interval = </label>
                        <input class='ch1' type='number' id='nbInt' name='N' placeholder='Nombre de sous interval' value='$n' required>

                        <input type='submit' name='confirmer' value='Confirmer'>
                    </form>
                    <p class='gros'> Resultat = $resutlat </p>
                    ";
                }
                ?>
                </td>
                <hr>
                <td class='right'>
                    <h8>Description de la méthode :</h8>
                    <p class='description' id='description'></p>

                    <h8>Formule :</h8>
                    <p class='description' id='formule'></p>
                </td>

            </tr>

        </table>

    </body>

</html>
