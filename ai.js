const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
const synth = window.speechSynthesis;

recognition.continuous = false;
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 1;

function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    synth.speak(utterance);
}

document.getElementById("start-btn").addEventListener("click", () => {
    recognition.start();
});

recognition.onresult = async (event) => {
    const userQuery = event.results[0][0].transcript;
    document.getElementById("output").innerText = `You: ${userQuery}`;

    try {
        const response = await fetch("https://your-deployed-api.com/voice-assistant", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: userQuery })
        });

        const data = await response.json();
        document.getElementById("response").innerText = `Assistant: ${data.reply}`;
        speak(data.reply); // Speak the response

    } catch (error) {
        console.error("Error:", error);
        speak("Hi, I am viraj,how can i help you.");
    }
};
