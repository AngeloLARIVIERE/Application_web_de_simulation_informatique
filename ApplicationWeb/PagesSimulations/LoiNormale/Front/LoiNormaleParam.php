<?php
session_start();
require_once ('../../../Commun/VariablesGlobal.php');

if (isset($_POST['confirmer']))
{
    $b = strval($_POST['B']);
    $n = strval($_POST['N']);
    $M = strval($_POST['M']);
    $sigma = strval($_POST['Sigma']);
    $fct = strval($_POST['Fct']);

    $_SESSION['B'] = $b;
    $_SESSION['N'] = $n;
    $_SESSION['M'] = $M;
    $_SESSION['Sigma'] = $sigma;
    $_SESSION['Fct'] = $fct;
}
$output = null;
$code = null;
if ($sigma == '0'){
    echo "<script>
                    alert('Ecart type doit être différentes de 0');
                    window.location = 'PageLoiNormale.php';
                    </script>";
    $_SESSION['Sigma']= '';
}
else {

    $command = "python3 ../Back/LoiNormale.py " . $M . ' ' . $sigma . ' ' . $n . ' ' . $b . ' ' .
        str_replace(" ", "_", $fct);


    exec($command, $output, $code);

    $pseudo = $_SESSION['pseudo'];

    // Appel de la fonction qui ets dans VariablesGlobal.php
    $Id_u=getIDUtilisateur($pseudo);

    // Appel de la fonction getIDHitorique qui est dans VariablesGlobal.php
    $Id_m=getIDModule('loi normale');

    // Appel de la fonction ajoutStatistique qui est dans VariablesGlobal.php
    ajoutStatistique($Id_m, 'nb_utilisation');

    // Appel de la fonction ajoutHisorique qui est dans VariablesGlobal.php
    ajoutHistorique($Id_u, $Id_m);

    $_SESSION["result"] = $output[0];

    header("Location: PageLoiNormale.php");
}
?>