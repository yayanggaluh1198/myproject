$(window).scroll(function(){
	var scroll = $(window).scrollTop();

	document.getElementById("myBody").style.marginTop = (-100 - 0.5*scroll) + "px";

	if(scroll >= 300){
		$("#myNav").addClass("bg_dark");
	} else {
		$("#myNav").removeClass("bg-dark")
	}
});