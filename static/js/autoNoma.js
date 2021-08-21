const fullLodzins = document.getElementById('lodzinjs')
let jaunsLogi = []

window.addEventListener('load', () => {
    jaunsLogi = JSON.parse(localStorage.getItem("jaunsLogi") || "[]");
    console.log(jaunsLogi)
    render();
});

document.getElementById('jaunaNoma').addEventListener('click', () => {
    fullLodzins.style.display = 'block';

});

document.getElementById('PrecesPoga').addEventListener('click', () => {
    fullLodzins.style.display = 'none';

    let jaunsLogs = { Id: id.value, Vards: vards.value, Uzvards: uzvards.value, DzivesVieta: dzivesVieta.value, Numurs: numurs.value, Budzets: budzets.value, Marka: marka.value, Datums: datums.value };

    id.value = 0;
    vards.value = " ";
    uzvards.value = " ";
    dzivesVieta.value = " ";
    numurs.value = " ";
    budzets.value = " ";
    marka.value = " ";
    datums.value = " ";

    jaunsLogi.push(jaunsLogs);

    render();
});

function render() {
    let biblioteka = document.getElementById('biblioteka');
    biblioteka.innerHTML = "";
    for (let i = 0; i < jaunsLogi.length; i++) {
        let jaunsLogs = `
        <div class="jaunsLogs">
            <h4> ID: ${jaunsLogi[i].Id++};
            <h4> Vārds: ${jaunsLogi[i].Vards}</h4>
            <h4>Uzvārds: ${jaunsLogi[i].Uzvards}</h4>
            <h4>Dzīves vieta: ${jaunsLogi[i].DzivesVieta}</h4>
            <h4>Telefona numurs: ${jaunsLogi[i].Numurs}</h4>
            <h4>Budžets: ${jaunsLogi[i].Budzets}Eur</h4>
            <h4>Automobīļa marka: ${jaunsLogi[i].Marka}</h4>
            <h4>Nomas datums: ${jaunsLogi[i].Datums}</h4>
            <button onclick="aps(${jaunsLogi[i].Id})">Aptiprināt</button>
            <button onclick="neaps(${jaunsLogi[i].Id})">Neapstiprināt</button>
            <h5 id="${jaunsLogi[i].Id}">Noma apstiprināta!</h5>
            <h5 id="${jaunsLogi[i].Id}>Noma noraidīta!</h5>
            <script>
        </div>`;

        biblioteka.innerHTML += jaunsLogs;
    }

    let pazinojum = document.getElementById('pazinojum');
    pazinojum.innerHTML = "";
    for (let i = 0; i < jaunsLogi.length; i++) {
        let pazinojumi = `
        <div class="alert">
            <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
            <strong>Ziņojums!</strong> Automašinas nomas sūtijums nosūtīts mājas lapas adminiem!
        </div>`;

        pazinojum.innerHTML += pazinojumi;
    }

    localStorage.setItem("jaunsLogi", JSON.stringify(jaunsLogi));
}

function aps(id) {
    for (let x = 0; x < jaunsLogi.length; x++) {
        var apst = document.getElementById(jaunsLogi[x].Id);
        if (id == jaunsLogi[x].Id) {
            if (apst.style.display === "none") {
                apst.style.display = "block";
            } else {
                apst.style.display = "none";
            }
        }
    }

}