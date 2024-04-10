document.getElementById('btn').addEventListener('change', function() {
    var isChecked = this.checked;
    if (isChecked) {
        recordVoiceCommand();
    }
});

// Function to start recording voice commands
function startRecording() {
    const recognition = new webkitSpeechRecognition(); // Create a new SpeechRecognition object
    recognition.lang = 'en-US'; // Set the language to English (United States)

    recognition.onstart = function() {
        console.log('Recording voice command...');
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript; // Get the transcribed voice command
        console.log('Voice command recorded:', transcript);
        sendCommandToServer(transcript); // Call sendCommandToServer() with the recorded command
    };

    recognition.onerror = function(event) {
        console.error('Error recording voice command:', event.error);
    };

    recognition.start(); // Start recording
}

// Function to stop recording voice commands
function stopRecording() {
    recognition.stop(); // Stop recording
}

// Event listener for checkbox change
document.getElementById('btn').addEventListener('change', function() {
    var isChecked = this.checked;
    if (isChecked) {
        startRecording(); // Start recording when checkbox is checked
    } else {
        stopRecording(); // Stop recording when checkbox is unchecked
    }
});
function updateOutputText(text) {
    const outputDiv = document.getElementById('output-text');
    outputDiv.innerHTML = '<p>' + text + '</p>';
}
function sendCommandToServer(command) {
    fetch('/submit_command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ command: command }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response:', data.output_text);
        updateOutputText(data.output_text); // Update the output text on the HTML page
        document.getElementById('btn').checked = false; // Uncheck the checkbox after receiving the command
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
