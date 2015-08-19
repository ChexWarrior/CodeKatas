document.addEventListener("DOMContentLoaded", function() {
    var processButton = document.querySelector("input[name='process']");
    processButton.addEventListener('click', function() {
        var processInput = document.querySelector("input[name='input']");
        var inputValue = processInput.value;
        console.log(inputValue);
        alert(isWordAlphabetic(inputValue.trim().toLowerCase()));
    });
});

function isWordAlphabetic(input) {
    var currentLetterIndex;
    for(currentLetterIndex = 0; currentLetterIndex < input.length; currentLetterIndex += 1) {
        //console.log("Letter: " + input[currentLetterIndex] + " = " + input[currentLetterIndex].charCodeAt());
        if(currentLetterIndex > 0) {
            var previousLetter = input[currentLetterIndex - 1];
            var currentLetter = input[currentLetterIndex];
            console.log("previousLetter: " + previousLetter);
            console.log("currentLetter: " + currentLetter);
            if(previousLetter.charCodeAt() > currentLetter.charCodeAt()) {
                return false;
            }
        }
    }

    return true;
}