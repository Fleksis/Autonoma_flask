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

    let jaunsLogs = {Vards: vards.value, Uzvards: uzvards.value, DzivesVieta: dzivesVieta.value, Numurs: numurs.value, Budzets: budzets.value, Marka: marka.value, Datums: datums.value};

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

    for(let i = 0; i < jaunsLogi.length; i++) {
        let jaunsLogs = `
        <div class="jaunsLogs">
            <h4>Vārds: ${jaunsLogi[i].Vards}</h4>
            <h4>Uzvārds: ${jaunsLogi[i].Uzvards}</h4>
            <h4>Dzīves vieta: ${jaunsLogi[i].Dzivesvieta}</h4>
            <h4>Telefona numurs: ${jaunsLogi[i].Numurs}</h4>
            <h4>Budžets: ${jaunsLogi[i].Budzets}Eur</h4>
            <h4>Automobīļa marka: ${jaunsLogi[i].Marka}</h4>
            <h4>Nomas datums: ${jaunsLogi[i].Datums}</h4>
        </div>`;

        biblioteka.innerHTML += jaunsLogs;
    }

    localStorage.setItem("jaunsLogi", JSON.stringify(jaunsLogi));
}