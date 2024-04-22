
var successMessage = document.getElementById("successMessage");

if (successMessage) {
    successMessage.classList.remove("hidden");

    setTimeout(function() {
        successMessage.classList.add("hidden");
    }, 5000);
}
