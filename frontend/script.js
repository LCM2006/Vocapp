const search_section = document.getElementById("search-section")
const search_word = document.getElementById("search-word")
const search_button = document.getElementById("search-button")
const user_example = document.getElementById("user-example")
const check_sentence = document.getElementById("check-sentence")
const display_aifeedback = document.getElementById("display-aifeedback")
const definition_display = document.getElementById("definition-display")
const example_display = document.getElementById("example-display")

search_button.addEventListener("click", function() {
    fetch('https://vocapp-backend.onrender.com/word?query='+search_word.value)
    .then(response => response.json())
    .then(data => {
        if(data.message){
            definition_display.innerText = data.message
            example_display.style.display = "block"
        }
        else{
            definition_display.innerText = data.Definition, 
            example_display.innerText = data.Example}
        })
})

check_sentence.addEventListener('click', function(){
    fetch('https://vocapp-backend.onrender.com/check-sentence',{
        method: 'POST',
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        word: search_word.value,
        sentence: user_example.value
    })
    })
    .then(response => response.json())
    .then(data => display_aifeedback.innerHTML = marked.parse(data.feedback))
})