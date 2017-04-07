var baseUrl = 'http://192.168.8.102:8081/';

function setUpAlarmElements() {
    var btn = document.getElementById('alarmToggler');
    var icon = document.getElementById('alarmState');

    getAlarmStatus(preparePage, btn, icon);
};

preparePage = function (btn, icon, response) {
    if (response === 'True') {
        icon.className = 'alarm_on';
        btn.value = 'Wyłącz alarm';
        document.getElementById('pin').className = '';
    }
};

alarmBtnTrigger = function () {
    var btn = document.getElementById('alarmToggler');
    var icon = document.getElementById('alarmState');

    getAlarmStatus(toggleAlarm, btn, icon);
}

toggleAlarm = function (btn, icon, alarmStatus) {
    if (alarmStatus === 'False') {
        turnAlarmOn(btn, icon);
    } else if (alarmStatus === 'True') {
        turnAlarmOff(btn, icon);
    }
}

turnAlarmOn = function (btn, icon) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", baseUrl + 'enableAlarm', true);
    xmlHttp.send(null);
    xmlHttp.onload = function () {
        icon.className = 'alarm_on';
        btn.value = 'Wyłącz alarm';
        document.getElementById('pin').className = '';
    };
}

turnAlarmOff = function (btn, icon) {
    var givenPin = document.getElementById('pin').value;

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", baseUrl + "disableAlarm/" + givenPin, false);
    xmlHttp.send();
    xmlHttp.onload = onSuccess(xmlHttp, btn, icon);
}

onSuccess = function (httpObj, btn, icon) {
    if (httpObj.status === 200) {
        icon.className = 'alarm_off';
        btn.value = 'Włącz alarm';
        document.getElementById('pin').className = 'hidden';
    } else if (httpObj.status === 401) {
        alert(httpObj.responseText);
    } else {
        alert('Rządanie zakończone niepowodzeniem');
    }
}

getAlarmStatus = function (callback, btn, icon) {
    var http = new XMLHttpRequest();
    http.open("GET", baseUrl + 'alarmState', true);
    http.send(null);
    http.onload = function () {
        callback(btn, icon, http.responseText);
    };
    return undefined;
};
