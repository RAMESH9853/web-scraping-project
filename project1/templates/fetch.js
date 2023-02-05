let timeoutId = null;

document.getElementById("url").addEventListener("input", function(event) {
  clearTimeout(timeoutId);
  timeoutId = setTimeout(() => {
    const url = document.getElementById("url").value;
    if (!url) return;
    fetchData(url);
  }, 3000);
});

const fetchData = url => {
  const socket = new WebSocket("ws://" + window.location.host + "/ws/fetch/");
  socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    // update the UI with the received data
  };
  socket.onopen = function(e) {
    socket.send(url);
  };
};
