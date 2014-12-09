
function ajaxCore(url, async, type, data, contentType, context, callback){
	if (contentType == null){
		var contentType = "application/x-www-form-urlencoded";
	}
	if (context == null){
		var context = this;
	}
	$.ajax({ 
		url: url, //"/docmaster"
		async: async, //true
		type: type, //"POST","GET"
		data: data,  //text, object
		contentType: contentType, //"application/x-www-form-urlencoded"		
		context: context, 	//this	
		dataType: "text",
		cache: false,		
		success: callback,
	}); 
} 

function ajax(url, type, data, callback){
	ajaxCore(url, true, type, data, null, null, callback);
}

function ajaxPost(url, data, callback){
	ajaxCore(url, true, 'POST', data, null, null, callback);
}

function ajaxGet(url, data, callback){
	ajaxCore(url, true, 'GET', data, null, null, callback);
}

function getFormData(formID){
	var data = '';
	$('#'+formID+' [name]').each(
		function(){
			if (this.tagName=='INPUT' || this.tagName=='SELECT' || this.tagName=='TEXTAREA'){
				data += this.name + '=' + encodeURIComponent($(this).val()) + '&';
			}			
		});
	return data;
}
function refresh(){
	location.reload();
}
function updateSelect(sid, json){	
	var options = '';
	for(var i=0; i<json.length; i++){
		options += '<option value="'+json[i].id+'">'+json[i].name+'</option>'
	}
	$('#'+sid).append(options);
}
function getcookie(name) {
	var cookie_start = document.cookie.indexOf(name);
	var cookie_end = document.cookie.indexOf(";", cookie_start);
	return cookie_start == -1 ? '' : unescape(document.cookie.substring(cookie_start + name.length + 1, (cookie_end > cookie_start ? cookie_end : document.cookie.length)));
}
function really(msg){
	return confirm(msg);
}