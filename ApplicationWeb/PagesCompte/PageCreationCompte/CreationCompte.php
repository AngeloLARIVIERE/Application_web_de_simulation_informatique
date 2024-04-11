<!DOCTYPE html>

<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Créer un compte</title>
    <link rel="icon" href="../../Commun/Icon/FavIcon.ico" type="image/ico">
    <link href="../StyleForm.css" rel="stylesheet" type="text/css">
    <link href="../../Commun/StyleCommun.css" rel="stylesheet" type="text/css">
</head>

<body>
    <p class="logo">
        <div class="logo">
            <a href="../../index.html"><img class="image" src="../../Commun/Icon/LogoSite.png" alt="Logo"></a>
        </div>
    </p>
    <div class='infos_login'>

        <h1>Créer un compte</h1>

        <div>
            <form class="form1" action="../../BaseDeDonnees/CreationUtilisateur.php" method="post">
                <label for='nom' hidden>Nom</label>
                <input class='ch1' required type='text' id='nom' name='nom' minlength="1" placeholder='Nom' autofocus
                       pattern="^(?!.*[<>]).{1,}$"
                       title="Les caractères '<' & '>' ne sont pas autorisés"><br>
                <label for='prenom' hidden>Prenom</label>
                <input class='ch1' required type='text' id='prenom' name='prenom' minlength="1" placeholder='Prenom'
                       pattern="^(?!.*[<>]).{1,}$"
                       title="Les caractères '<' & '>' ne sont pas autorisés"> <br>
                <label for='pseudo' hidden>Pseudo</label>
                <input class='ch1' required type='text' id='pseudo' name='pseudo' minlength="1" placeholder='Pseudo'
                       pattern="^(?!.*[<>]).{1,}$"
                       title="Les caractères '<' & '>' ne sont pas autorisés"> <br>
                <label for='mdp' hidden>Mdp</label>
                <input class='ch1' required type='password' id='mdp' name='mdp' placeholder='Mot de passe'
                       pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[<>]).{12,}$"
                       title="Critères : au moins 1 majuscule, 1 minuscule, 1 chiffre, 12 caractères minimum"> <br>
                <label for='mdp2' hidden>Mdp2</label>
                <input class='ch1' required type='password' id='mdp2' name='mdp2' placeholder='Confirmer mot de passe'
                       pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[<>]).{12,}$"
                       title="Critères : au moins 1 majuscule, 1 minuscule, 1 chiffre, 12 caractères minimum"> <br>
                <p>Résoudre le CAPTCHA suivant :</p>
                <?php
                session_start();
                $captcha_a = rand(1, 20);
                $captcha_b = rand(1, 20);
                echo "<p>$captcha_a + $captcha_b =
                <label for='captcha' hidden>Captcha</label>
                </p><input class='ch1' required type='number' id='captcha' name='captcha' placeholder='Réponse'> <br>";
                $_SESSION['captcha_a'] = $captcha_a;
                $_SESSION['captcha_b'] = $captcha_b;
                ?>
                <input class="se_connecter" type='submit' name='ok' value="S'inscrire"> <br><br>
            </form>
        </div>
    </div>
</body>

</html>
