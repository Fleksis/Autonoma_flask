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

// document.getElementById('PrecesPoga').addEventListener('click', () => {
//     fullLodzins.style.display = 'none';
//     let jaunsLogs = {
//     Vards: vards.value,
//     Uzvards: uzvards.value,
//     DzivesVieta: dzivesVieta.value,
//     Numurs: numurs.value,
//     Marka: marka.value,
//     No: no.value,
//     Lidz: lidz.value
//     };

//     vards.value = " ";
//     uzvards.value = " ";
//     dzivesVieta.value = " ";
//     numurs.value = " ";
//     marka.value = " ";
//     no.value = " ";
//     lidz.value = " ";

//     jaunsLogi.push(jaunsLogs);

//     render();
// });

// function render() {
//     let biblioteka = document.getElementById('biblioteka');
//     biblioteka.innerHTML = "";
//     let x = 0
//     for (let i = 0; i < jaunsLogi.length; i++) {
//         x = x + 1
//         let jaunsLogs = `
//         <div class="jaunsLogs">
//             <h4> ID: ${x};
//             <h4> Vārds: ${jaunsLogi[i].Vards}</h4>
//             <h4>Uzvārds: ${jaunsLogi[i].Uzvards}</h4>
//             <h4>Dzīves vieta: ${jaunsLogi[i].DzivesVieta}</h4>
//             <h4>Telefona numurs: ${jaunsLogi[i].Numurs}</h4>
//             <h4>Automobīļa marka: ${jaunsLogi[i].Marka}</h4>
//             <h4>Nomas datums no: ${jaunsLogi[i].No}</h4>
//             <h4>Nomas datums līdz: ${jaunsLogi[i].Lidz}</h4>
//             <button onclick="aps(${jaunsLogi[i].Id})">Aptiprināt</button>
//             <button onclick="neaps(${jaunsLogi[i].Id})">Neapstiprināt</button>
//             <h5 id="${jaunsLogi[i].Id}">Noma apstiprināta!</h5>
//             <h5 id="${jaunsLogi[i].Id}>Noma noraidīta!</h5>
//         </div>`;
//         console.log(x)
        
//         biblioteka.innerHTML += jaunsLogs;
//     }

//     let pazinojum = document.getElementById('pazinojum');
//     pazinojum.innerHTML = "";
//     for (let i = 0; i < 1; i++) {
//         let pazinojumi = `
//         <div class="alert">
//             <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
//             <strong>Ziņojums!</strong> Automašinas nomas sūtijums nosūtīts mājas lapas adminiem!
//         </div>`;

//         pazinojum.innerHTML += pazinojumi;
//     }
//     console.log(x)
//     console.log(typeof x)

//     localStorage.setItem("jaunsLogi", JSON.stringify(jaunsLogi));
// }

function alerts() {
    alert("Automašinas nomas sūtijums nosūtīts mājas lapas adminiem!");
}

function aps(id) {
    for (let x = 0; x < jaunsLogi.length; x++) {
        let apst = document.getElementById(jaunsLogi[x].Id);
        if (id == jaunsLogi[x].Id) {
            if (apst.style.display === "none") {
                apst.style.display = "block";
            } else {
                apst.style.display = "none";
            }
        }
    }
}

function neaps(id) {
    for (let x = 0; x < jaunsLogi.length; x++) {
        let neapst = document.getElementById(jaunsLogi[x].Id);
        if (id == jaunsLogi[x].Id) {
            if (neapst.style.display === "none") {
                neapst.style.display = "block";
            } else {
                neapst.style.display = "none";
            }
        }
    }
}