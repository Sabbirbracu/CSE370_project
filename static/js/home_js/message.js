var successMessage = document.getElementById("successMessage");

if (successMessage) {
    successMessage.classList.remove("hidden");

    setTimeout(function() {
        successMessage.classList.add("hidden");
    }, 5000);
}


var errorMessage = document.getElementById("errorMessage");

if (errorMessage) {
    errorMessage.classList.remove("hidden");

    setTimeout(function() {
        errorMessage.classList.add("hidden");
    }, 5000);
}
