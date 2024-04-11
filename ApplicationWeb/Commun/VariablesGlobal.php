<?php
# Variables global pour la connexion à la base de données
define('DATABASE', "notrebase"); // nom de la table 
define('HOSTNAME', "localhost"); // 
define('USERNAME', "user"); //nom utilisateur pour la connexion de la base de donner
define('PASSWORD', "test"); //mot de passe pour la connexion de la base de donner

# Variables global pour les noms de tables
define('T_UTILISATEUR',"Utilisateur"); //nom de la table des utilisateurs
define('T_STATISTIQUE',"Statistique"); //nom de la table pour les statistiques
define('T_HISTORIQUE',"Historique"); // non de la table pour l'historique de l'utilisation des modules
define('T_MODULES',"Modules"); // nom de la table pour les modules

function getIDUtilisateur(string $pseudo) : int
{
    /**
     * Permet d'avoir l'id de l'utilisateur en lui donnant un nom d'utilisateur
     * elle prend un paramètre :
     * @param string $pseudo est le pseudo d'un utilisateur de la base
     * @return int $res[0] est l'id de notre utilisateur
     */
    $connexion = mysqli_connect(HOSTNAME, USERNAME, PASSWORD);
    $sqlId_u = "Select id_u from Utilisateur where pseudo = '$pseudo';";
    mysqli_select_db($connexion, DATABASE);
    $res = mysqli_fetch_row(mysqli_query($connexion, $sqlId_u));
    return  $res[0];

}


function getIDModule(string $nom_m): int
{
    /**
     * Permet d'avoir l'id du module en lui donnant un nom de module
     * elle prend un paramètre :
     * @param string $nom_m est le nom d'un module de la base
     * @return int $res est l'id de notre module
     */
    $connexion = mysqli_connect(HOSTNAME, USERNAME, PASSWORD);
    mysqli_select_db($connexion, DATABASE);
    $sqlId_u = "SELECT id_m FROM Modules WHERE nom_m = '$nom_m';";
    $res = mysqli_fetch_row(mysqli_query($connexion, $sqlId_u))[0];
    return $res;

}

function ajoutHistorique(int $Id_u, int $Id_m): void
{
    /**
     * Permet d'inserer une lige dans la table Historique de notre base de donnée avec le couple de paramètre
     * elle prend deux paramètres:
     * @param int $Id_u est l'id d'un utilisateur de la base
     * @param int $Id_m est l'id d'un module de la base
     */
    $bd = new PDO('mysql:host=localhost;dbname=notrebase', USERNAME, PASSWORD) or die("Impossible de se connecter au serveur");
    $sql2 = "Insert into Historique (id_m, id_u) values ($Id_m,$Id_u);";
    $resultat2 = $bd->prepare($sql2);
    $resultat2->execute();
}

function ajoutStatistique(int $Id_m, string $col): void
{
    $conn = mysqli_connect(HOSTNAME, USERNAME, PASSWORD) or die("Impossible de se connecter au serveur");

    mysqli_select_db($conn, DATABASE) or die("Impossible de sélectionner la base de données");

    $sql = "UPDATE Statistique SET $col = $col+1 WHERE id_s = ?;";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param('s', $Id_m);
    $stmt->execute();
    $stmt->get_result(); 
}

function getUserSort(String $pseudo,String $table)
{
    /*
     * Permet d'avoir une liste des utilisateurs trié par leur pseudo
     * elle prend un paramètres :
     * @param String $pseudo est le pseudo d'un utilisatuer de la base
     */
    if ($pseudo !== '') 
    {
        $connexion = mysqli_connect(HOSTNAME, USERNAME, PASSWORD);
        $bd2 = mysqli_select_db($connexion, DATABASE);
        $requette = "SELECT pseudo,nom,prenom,statut FROM $table WHERE pseudo like '%$pseudo%';";
        return mysqli_query($connexion, $requette);
        
    } else 
    {
        $connexion = mysqli_connect(HOSTNAME, USERNAME, PASSWORD);
        $bd2 = mysqli_select_db($connexion, DATABASE);
        $requette = "SELECT pseudo,nom,prenom,statut FROM Utilisateur WHERE pseudo != 'gestionnaire';";
        return mysqli_query($connexion, $requette);
    }

}

function getHistSort(String $pseudo)
{
    /*
     * Permet d'avoir une liste des utilisateurs trié par leur pseudo
     * elle prend un paramètres :
     * @param String $pseudo est le pseudo d'un utilisatuer de la base
     */
    if ($pseudo !== '') 
    {
        $connexion = mysqli_connect(HOSTNAME, USERNAME, PASSWORD);
        mysqli_select_db($connexion, DATABASE);
        $requette = "SELECT t1.nom_m, t2.pseudo, DATE_FORMAT(t3.do_at,'%d/%m/%Y à %H:%i:%s') from Modules t1, Utilisateur t2, Historique t3 where t1.id_m = t3.id_m and t2.id_u = t3.id_u and t2.pseudo like '%$pseudo%' order by do_at desc ;";
        return mysqli_query($connexion, $requette);
        
    } else 
    {
        $connexion = mysqli_connect(HOSTNAME, USERNAME, PASSWORD);
        mysqli_select_db($connexion, DATABASE);
        $requette = "SELECT t1.nom_m, t2.pseudo, DATE_FORMAT(t3.do_at,'%d/%m/%Y à %H:%i:%s') from Modules t1, Utilisateur t2, Historique t3 where t1.id_m = t3.id_m and t2.id_u = t3.id_u order by do_at desc;";
        return mysqli_query($connexion, $requette);
    }

}

?>