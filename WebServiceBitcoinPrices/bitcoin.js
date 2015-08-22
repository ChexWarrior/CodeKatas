document.addEventListener("DOMContentLoaded", function() {
    var goButton = document.querySelector("input[name='go']");
    goButton.addEventListener("click", function() {
        getBitcoinValue()
    });
});

function getBitcoinValue() {
    console.log("Press");
}