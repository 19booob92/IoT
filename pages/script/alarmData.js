var baseUrl = 'http://192.168.8.101:8081/';

setUpPage = function() {
    var secondsToDeactivate = document.getElementsByName("secondsToDeactivate")[0];
    var sendMailDelay = document.getElementsByName("sendMailDelay")[0];

    var http = new XMLHttpRequest();
 	http.open( "GET", baseUrl + 'loadAlarmConfig', true );
	http.send();
	http.onload = function() {
        var alarmData = JSON.parse(http.responseText);

        secondsToDeactivate.value = alarmData.secondsToDeactivate;
        sendMailDelay.value = alarmData.sendMailDelay;
    };
};
