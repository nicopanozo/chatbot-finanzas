const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const chatbox = document.querySelector(".chatbox");

let userMsg;

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi;
}

const generateResponse = (incomingChatLi) => {
    const API_URL = "http://127.0.0.1:7080/chat_data";
    const messageElement = incomingChatLi.querySelector("p");

    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            userContent: userMsg,
        })
    }

    fetch(API_URL, requestOptions)
        .then(res => res.json())
        .then(data => {
            messageElement.textContent = data.response;
        })
        .catch((error) => {
            messageElement.textContent = "Oops! Something went wrong. Please try again.";
        })
        .finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
}

const handleChat = () => {
    userMsg = chatInput.value.trim();
    if (!userMsg) return;
    chatInput.value = "";

    chatbox.appendChild(createChatLi(userMsg, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);

    setTimeout(() => {
        const incomingChatLi = createChatLi("Thinking...", "incoming");
        chatbox.appendChild(incomingChatLi);
        generateResponse(incomingChatLi);
    }, 600);
}

sendChatBtn.addEventListener("click", handleChat);