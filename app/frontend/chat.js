const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatMessages = document.getElementById("chat-messages");
const loader = document.querySelector(".loader");

sendButton.addEventListener("click", sendMessage);

messageInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    sendMessage();
  }
});

const websocket = new WebSocket("ws://localhost:8000/chat");

websocket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log(data);
  loader.style.display = "none";
  const messageElement = document.createElement("div");
  messageElement.innerHTML = `AI: ${data.answer.replace(/\n/g, "<br>")}`;
  chatMessages.appendChild(messageElement);
  chatMessages.scrollTop = chatMessages.scrollHeight;
};

function sendMessage() {
  const message = messageInput.value.trim();
  if (message) {
    loader.style.display = "block";
    websocket.send(JSON.stringify({ query: message, model: "gpt-3.5-turbo" }));
    messageInput.value = "";
  }
}
