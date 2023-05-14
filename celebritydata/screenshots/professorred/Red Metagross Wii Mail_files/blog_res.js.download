(function(){
	try {
		var loop = 5;
		var t = setInterval(function(){
			loop--;
			if (0 >= loop) clearInterval(t);
			var b = document.getElementsByTagName("body");
			if (!b[0]) return;
			clearInterval(t);
			var res_form_list = ['name','mail','url'];
			for (var i = 0, j = res_form_list.length; i < j; i++){
				setResForm(res_form_list[i]);
			}
		}, 200);

		function setResForm(name) {
			var res_data = getCommentCookie('blog_res_' + name);
			if (res_data.length > 0) {
				var blog_res_form = document.getElementsByName('comment[' + name + ']');
				if (blog_res_form.length) blog_res_form[0].value = res_data;
			}
		}

		function getCommentCookie(c_name) {
			var cookie_txt = document.cookie+";";
			if (cookie_txt.length > 0) {
				var start = cookie_txt.indexOf(c_name + "=");
				if (start != -1) { 
					start = start + c_name.length + 1;
					var end = cookie_txt.indexOf(";", start);
					if (end == -1) end = cookie_txt.length;
					var u = "";
					try {
						u = decodeURIComponent(cookie_txt.substring(start,end));
					} catch (ex) {}
					return u;
				} 
			}
			return "";
		}
	} catch (ex) {}
})();
