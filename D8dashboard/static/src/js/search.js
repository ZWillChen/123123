function GoClick(){
	if(validationCheck()){
		var help = document.getElementsByClassName("help-block");
		for (var i = 0, len = help.length | 0; i < len; i=i+1 | 0){
			help[i].hidden = true;
		}
		document.getElementById("search_form").submit();
	}
	else{
		alert("Please check your input!");
	}
}
function validationCheck(){
	var sdate = document.getElementById("start_date-input").value.toString();
	var edate = document.getElementById("end_date-input").value.toString();
	var isValid = true;
	if(typeof(sdate) == "null" || sdate.length == 0){
		sdate = "1970-01-01";
		document.getElementById("start_date-input").value = sdate;

	}
	if(typeof(edate) == "null" || edate.length == 0){
		edate = "2100-01-01";
		document.getElementById("end_date-input").value = edate;
	}
	isValid = ((new Date(edate.replace(/-/g,"\/"))) > (new Date(sdate.replace(/-/g,"\/"))));
	if(!isValid){
		document.getElementById("sdate_err").hidden = false;
		document.getElementById("edate_err").hidden = false;
		document.getElementById("sdate_err").innerHTML += " Start date must be earlier than end date!";
	}
	return isValid;
}