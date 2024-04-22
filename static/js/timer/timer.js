let timer;
let elapsedTime = 0;
let isRunning = false;

// Function to start the stopwatch
function startStopwatch() {
    isRunning = true;
    timer = setInterval(updateTime, 1000); // Update time every second
}

// Function to stop the stopwatch
function stopStopwatch() {
    isRunning = false;
    clearInterval(timer);
}

// Function to update the time on the stopwatch
function updateTime() {
    elapsedTime++; // Increment by 1 second
    let hours = Math.floor(elapsedTime / 3600);
    let minutes = Math.floor((elapsedTime % 3600) / 60);
    let seconds = elapsedTime % 60;
    document.getElementById('stopwatch').innerText = `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
}

// Function to pad numbers with leading zeros
function pad(num) {
    return num.toString().padStart(2, '0');
}

// Function to submit the form and stop the ride
function stopRide() {
    stopStopwatch();
    let elapsedTimeStr = document.getElementById('stopwatch').innerText;
    document.getElementById('elapsed-time').value = elapsedTimeStr;
    document.getElementById('stop-ride-form').submit();
}

// Event listener for Stop Ride button
document.getElementById('stop-ride-btn').addEventListener('click', stopRide);

// Wait for the DOM content to be fully loaded before executing JavaScript code
document.addEventListener('DOMContentLoaded', function() {
    startStopwatch(); // Start the stopwatch when the page loads
});
