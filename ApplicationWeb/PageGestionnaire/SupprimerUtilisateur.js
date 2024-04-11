window.onload = init;

let request;

function init() {
    request = new XMLHttpRequest();
    request.open("POST", "SupprimerUtilisateur.php",true);
    }

function traitementReponse() {
    console.log(request.readyState + "" + request.status);
    if(request.readyState == 4 && request.status == 200){
        window.location = 'GestionBD.php'

    }
}


function deletUser(pseudo) {
    /**
     * Focntion qui prend en paramètre un pseudo et va le supprimer dans notre Base de donnée
     * @param pseudo
     * @type FormData
     * @returns void ne renvoie rien car éffectue juste une action
     */
    let data = new FormData();
    data.append("pseudo",pseudo.id);
    request.send(data);
    request.onreadystatechange = traitementReponse; // On définit la méthode onreadystatechange avant d'appeler la méthode send()

}