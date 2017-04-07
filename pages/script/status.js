var baseUrl = 'http://192.168.8.102:8081/';


function loadData() {
    var http = new XMLHttpRequest();
    http.open("GET", baseUrl + "rpi/status", true);
    http.send(null);
    http.onload = function () {
        fillPage(http.responseText);
    };
};

function fillPage(status) {
    var rpiStatus = JSON.parse(status);

    createDiv(rpiStatus.temp);
    createDiv(rpiStatus.uptime);
    createDiv(rpiStatus.ifconfig);
    createDiv(rpiStatus.space);
    createDiv(rpiStatus.memory);
};

function createDiv(content) {
    var tempDiv = document.createElement('div');
    tempDiv.className = 'divWithBorder';
    tempDiv.innerHTML = content;
    document.getElementById('data').appendChild(tempDiv);
};