var baseUrl = 'http://192.168.8.101:8081/'

setUpPage = function () {
    setUpAlarmElements();

    setUpLampElements();
};

checkEnableComponents = function() {
    var http = new XMLHttpRequestEventTarget("GET", baseUrl + "isAnyModuleActive", true);
    http.send();
}
