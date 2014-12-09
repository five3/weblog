function show_submit(rep){
	alert(rep);
}
function upit(id){
	ajaxPost('/user/up', 'id='+id, show_upit);
}
function show_upit(rep){
	var json = eval(rep)[0];
	if (json.errorCode==0){
		var num = $('#up_'+json.id+' em').text();
//		alert(1+parseInt(num));
		$('#up_'+json.id+' em').text(1+parseInt(num));
	}else{
		alert(json.message);
	}
}
