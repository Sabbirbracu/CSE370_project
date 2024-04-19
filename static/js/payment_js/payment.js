function handlePayment() {
    var payNowButton = document.getElementById("payNowButton");
    payNowButton.innerText = "Paid";
    payNowButton.classList.add("paid");
    payNowButton.disabled = true;
    payNowButton.style.animation = "none";
    payNowButton.style.pointerEvents = "none";


    var successMessage = document.createElement("div");
    successMessage.textContent = "Your payment is successful.";
    successMessage.style.position = "fixed";
    successMessage.style.top = "60px";
    successMessage.style.left = "50%";
    successMessage.style.transform = "translateX(-50%)";
    successMessage.style.backgroundColor = "rgba(76, 213, 255, 0.7)";
    successMessage.style.padding = "10px 20px";
    successMessage.style.borderRadius = "10px";
    successMessage.style.boxShadow = "2px -2px 2px rgba(0, 0, 0, 0.9)";
    successMessage.style.color = "#000";
    successMessage.style.zIndex = "9999";

    document.body.appendChild(successMessage);

    setTimeout(function() {
        successMessage.remove();
    }, 5000);
}
