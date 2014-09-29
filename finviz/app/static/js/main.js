$(document).ready(function() {
	console.log("ready");
	$("form").on("submit",function() {
		console.log("the form has been submitted")
		var valueOne = $('input[name="number-one"]').val()
		var valueTwo = $('input[name="number-two"]').val()
		console.log(valueOne, valueTwo)

	});
});
