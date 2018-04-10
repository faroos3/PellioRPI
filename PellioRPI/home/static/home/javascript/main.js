$(document).ready(function(){
	var clicked = false;
	var moods = [0,0,0,0,0,0,0,0,0,0,0];
	var moods2 = [0,0,0,0,0,0,0,0,0,0,0];
	$("#firstClick").click(function() {
		if (clicked == true) {
			alert("Wrong survey! Fill out the one below.");
			return;
		}
		moods[0] = parseInt($('input[name=interested]:checked').val());
		moods[1] = parseInt($('input[name=distressed]:checked').val());
		moods[2] = parseInt($('input[name=alerted]:checked').val());
		moods[3] = parseInt($('input[name=excited]:checked').val());
		moods[4] = parseInt($('input[name=upset]:checked').val());
		moods[5] = parseInt($('input[name=strong]:checked').val());
		moods[6] = parseInt($('input[name=inspired]:checked').val());
		moods[7] = parseInt($('input[name=nervous]:checked').val());
		moods[8] = parseInt($('input[name=scared]:checked').val());
		moods[9] = parseInt($('input[name=jittery]:checked').val());
		moods[10] = parseInt($('input[name=enthusiastic]:checked').val());
		for (var i = 0; i < moods.length; i++) {
			if (isNaN(moods[i])) {
				alert("Please fill out all form fields");
				moods = [0,0,0,0,0,0,0,0,0,0,0];
				return;
			}
		}
		clicked = true;
		alert("Initial Results Submitted!");
	});
	$("#resultClick").click(function() {
		if (clicked == false) {
			alert("Fill out the first survey before this one");
			return;
		}
		moods2[0] = parseInt($('input[name=interested2]:checked').val());
		moods2[1] = parseInt($('input[name=distressed2]:checked').val());
		moods2[2] = parseInt($('input[name=alerted2]:checked').val());
		moods2[3] = parseInt($('input[name=excited2]:checked').val());
		moods2[4] = parseInt($('input[name=upset2]:checked').val());
		moods2[5] = parseInt($('input[name=strong2]:checked').val());
		moods2[6] = parseInt($('input[name=inspired2]:checked').val());
		moods2[7] = parseInt($('input[name=nervous2]:checked').val());
		moods2[8] = parseInt($('input[name=scared2]:checked').val());
		moods2[9] = parseInt($('input[name=jittery2]:checked').val());
		moods2[10] = parseInt($('input[name=enthusiastic2]:checked').val());
		for (var i = 0; i < moods2.length; i++) {
			if (isNaN(moods2[i])) {
				alert("Please fill out all form fields");
				moods2 = [0,0,0,0,0,0,0,0,0,0,0];
				return;
			}
		}
		clicked = false;
		var positive = moods[0] + moods[2] + moods[3] + moods[5] + moods[6] + moods[10];
		var negative = moods[1] + moods[4] + moods[7] + moods[8] + moods[9];
		var positive2 = moods2[0] + moods2[2] + moods2[3] + moods2[5] + moods2[6] + moods2[10];
		var negative2 = moods2[1] +  moods2[4] + moods2[7] + moods2[8] + moods2[9];
		var posChange  = "";
		var negChange = "";
		if (positive2 - positive < 0) { posChange = "Don't worry about these results if you feel better."; }
		if (positive2 - positive < -5) { posChange = "Perhaps these kinds of videos aren't for you."; }
		if (positive2 - positive >= 0) { posChange = "You responded well to the experiment."; }
		if (positive2 - positive > 5) { posChange = "You should watch videos like these more often!."; }
		if (positive2 - positive > 10) { posChange = "That's a huge improvement! Hope you're feeling better :)"; }
		if (positive2 - positive > 15) { posChange = "This is the power of PELLIO!."; }
		if (negative2 - negative > 0) { negChange = "Don't worry about these results if you feel better."; }
		if (negative2 - negative > 5) { negChange = "Perhaps these kinds of videos aren't for you."; }
		if (negative2 - negative <= 0) { negChange = "You responded well to the experiment."; }
		if (negative2 - negative < -5) { negChange = "You should watch videos like these more often!."; }
		if (negative2 - negative < -10) { negChange = "That's a huge improvement! Hope you're feeling better :)"; }
		if (negative2 - negative < -15) { negChange = "This is the power of PELLIO!."; }

		if (posChange == "") {
			alert("Survey filled out in an invalid way. Please try again.");
		}
		else {
			alert("Positive change: " + (positive2 - positive).toString() + ". " + posChange);
			alert("Negative change: " + (negative2 - negative).toString() + ". " + negChange);
		}
		posChange = "";
		negChange = "";
	});
});