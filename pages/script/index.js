alarmBtnTrigger = function() {
	var btn = document.getElementById('alarmToggler');
	var icon = document.getElementById('circle');
	var btnValue = btn.value;

	if (btnValue === 'Włącz alarm') {
		turnAlarmOn(btn, icon);
	} else {
		turnAlarmOff(btn, icon);
	}
}

turnAlarmOn = function(btn, icon) {
	icon.className = 'alarm_on';
	btn.value = 'Wyłącz alarm';
}

turnAlarmOff = function(btn, icon) {
	icon.className = 'alarm_off';
	btn.value = 'Włącz alarm';
}
