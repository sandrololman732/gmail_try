function sendMessage() {
    var message = document.getElementById('textBox').value;
    
    if (message.trim() !== "") {
        // Use a simple AJAX call to send the message to the server
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/send-message", true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.send(JSON.stringify({ message: message }));

        alert("Message sent!");
        document.getElementById('textBox').value = "";
    } else {
        alert("Please enter a message before sending.");
    }
}
