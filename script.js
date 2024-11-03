const chatContainer = document.getElementById('chat-container');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const originalHeight = userInput.offsetHeight; 
const maxHeight = 100;
//const apiUrl = 'http://127.0.0.1:5000/data';

let messages = [];

userInput.addEventListener('input', () => {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, maxHeight) + 'px';
  });

sendButton.addEventListener('click', () => {
    const userInputValue = userInput.value.trim();
    if (userInputValue !== '') {
        addMessage('user', userInputValue);
        userInput.style.height = originalHeight + 'px';
        userInput.value = '';
        

        // simulate bot response
        getBotResponse(userInputValue)
        .then(botResponse => {
          addMessage('bot', botResponse);
        })
        .catch(error => {
          console.error("Error:", error);
          addMessage('bot', 'Sorry, something went wrong. Please try again later.');
        });
      }
    });

function addMessage(type, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message',`${type}-message`);
    messageElement.innerText = message;
    chatContainer.appendChild(messageElement);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    
  }

function getBotResponse(userMessage) {
  return new Promise((resolve, reject) => {
    const socket = new WebSocket('ws://localhost:5000/ws');

    socket.onopen = () => {
      socket.send(userMessage);
    };

    socket.onmessage = (event) => {
      const processedMessage = event.data;
      resolve(processedMessage); // Return the processed message
    };

    socket.onerror = (error) => {
      reject(error);
    };

    socket.onclose = () => {
      console.log('WebSocket connection closed');
    };
  });
}