document.getElementById('jaunaNoma').addEventListener('click', () => {
    document.getElementById('lodzinjs').style.display = 'block'
})

function alerts() {
    alert("Automašinas nomas sūtijums nosūtīts mājas lapas adminiem!")
}

document.getElementById("PrecesPoga").addEventListener("click", (e) => {
    var scrollingElement = (document.scrollingElement || document.body)
    scrollingElement.scrollTop = scrollingElement.scrollHeight
})