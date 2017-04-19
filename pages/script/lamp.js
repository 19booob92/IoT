var lampBaseUrl = 'http://192.168.8.101:8081/lamp/';

lampBtnTrigger = function () {
    var http = new XMLHttpRequest();
    http.open("GET", lampBaseUrl + "lampState", true);
    http.send();
    http.onload = function () {
        if (http.responseText === "False") {
            enableLamp();
        } else if (http.responseText === "True") {
            disableLamp();
        }
    };
};

enableLamp = function () {
    var http = new XMLHttpRequest();
    http.open("GET", lampBaseUrl + "enable", true);
    http.send();
    http.onload = function () {
        if (http.status === 200) {
            document.getElementById("lampState").className = 'alarm_on';
            document.getElementById("lampToggler").value = "Wyłącz lampę";
            document.getElementById('pin').className = '';
        }
    };
};

disableLamp = function () {
    var pinValue = document.getElementById("pin").value;

    var http = new XMLHttpRequest();
    http.open("GET", lampBaseUrl + "disable/" + pinValue , true);
    http.send();
    http.onload = function () {
        if (http.status === 200) {
            document.getElementById("lampState").className = 'alarm_off';
            document.getElementById("lampToggler").value = "Włącz lampę";
            document.getElementById('pin').className = 'hidden';
        } else if (http.status === 401) {
            alert("Błędny pin");
        } else {
            alert("Nie można wyłączyć lampy");
        }
    };
};

function setUpLampElements() {
    var btn = document.getElementById('lampToggler');
    var icon = document.getElementById('lampState');

    var http = new XMLHttpRequest();
    http.open("GET", lampBaseUrl + 'lampState', true);
    http.send(null);
    http.onload = function () {
        if (http.responseText === 'True') {
            icon.className = 'alarm_on';
            btn.value = 'Wyłącz lampę';
            document.getElementById('pin').className = '';
        }
    };
};

