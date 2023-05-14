setBlogCookie('name');
setBlogCookie('mail');
setBlogCookie('url');
function setBlogCookie(key){
	var form = (document.getElementById ? document.getElementById(key) : null);
	if(form && form.value == ""){
		var coookie = document.cookie+";",key_find = "blog_res_"+key+"=",key_begin = coookie.indexOf(key_find);
		if(key_begin != -1){
			form.value = decodeURIComponent(coookie.substring(key_begin+key_find.length, coookie.indexOf(";", key_begin)).replace(/\+/g, " "));
		}
	}
}
