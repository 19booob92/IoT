function loadData() {
  var http = new XMLHttpRequest();
  http.open("GET", baseUrl+"rpi/status", true);
  http.send();
  http.onload = function() {
    fillPage(http.responseText);
  };
};

function fillPage(status) {
    var rpiStatus = JSON.parse(status);
};
