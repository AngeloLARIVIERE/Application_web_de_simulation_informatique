window.onload = init;
function init() {
    /**
     * Fonction qui me permet de lancer une requete XMLHttp sur LoiNormale.json
     * @file LoiNormale.json fichier qui contient les informations de chaque méthode de calcule
     * @type {XMLHttpRequest}
     */
    request = new XMLHttpRequest();
    request.open("GET", "../../../JSON/LoiNormale.json");
    request.send();
    request.onreadystatechange = traitementReponse;
}

function traitementReponse() {
    /**
     * Fonction qui permet de transformer mes informations json en un objet Java Script
     * Si l'object html d'id method à une valeur on vient lui associer la methode aproprié du json
     * Sinon on met par défault celle des rectnagles gauches ( la première du fichier json)
     * @function utilisation de setValue()
     * @type JSON
     * @type Document
     * @type Request
     */
    if(request.readyState == 4 && request.status == 200){
        methodes = request.responseText;
        classesMethodes = JSON.parse(methodes);
        if (document.getElementById("method").value){
            for (let i = 0; i < classesMethodes.length; i++) {
                if (classesMethodes[i].nom == document.getElementById("method").value){
                    setValue(i);
                }
            }
        }
        else {
            setValue(0);

        }

    }
}

function description(id) {
    /**
     * @event onclick s'active quand l'utilisateur clique sur une méthode
     * @param id est un int qui correspond à l'indice dans l'object classeMethodes.
     * @function utilisation de setValue()
     */

    setValue(id);
}

function setValue(id){
    /**
     * Fonction qui permet d'indiquer automatiquement à l'utilisateur le nom de la méthode qui la choisi,
     * la description de cette méthode totu comme sa formule associé
     * @param id est un int qui correspond à l'indice dans l'object classeMethodes.
     * @type {Document.nom|*}
     */
    document.getElementById('method' ).value = classesMethodes[id].nom
    document.getElementById("description").textContent = classesMethodes[id].description
    document.getElementById("formule").textContent = classesMethodes[id].formules
}
