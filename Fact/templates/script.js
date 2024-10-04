function sendMessage() {
  var userMessage = document.getElementById('user-input').value;
  if (userMessage.trim() === '') {
      return;
  }

  var chatBox = document.getElementById('chatBox');
  var videoDiv = document.getElementById('video-container');
  var userMessageDiv = document.createElement("div");
  userMessageDiv.classList.add("message");

  document.getElementById('user-input').value = '';

  fetch('/chat', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: 'user_message=' + encodeURIComponent(userMessage),
  })
  .then(response => response.json())
  .then(data => {
      var botResponse = data.bot_response;
      var vidID = data.vid_id;

      chatBox.innerHTML = '';
      videoDiv.innerHTML = '';

      var botMessageDiv = document.createElement("div");
      var vidDiv = document.createElement("div");
      botMessageDiv.classList.add("message-response");
      botMessageDiv.innerHTML = `<span>${botResponse}</span>`;
      vidDiv.innerHTML = `<div class="iframevid" id="iframevid"><iframe width="560" height="315" src="https://www.youtube.com/embed/${vidID}" 
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen></iframe></div>`;
      chatBox.appendChild(botMessageDiv);
      videoDiv.appendChild(vidDiv);

      scrollChatToBottom();
  });
}

function scrollChatToBottom() {
  var chatBox = document.getElementById('chatBox');
  chatBox.scrollTop = chatBox.scrollHeight;
}

document.getElementById('user-input').addEventListener('keyup', function (event) {
  if (event.key === 'Enter') {
      sendMessage();
  }
});