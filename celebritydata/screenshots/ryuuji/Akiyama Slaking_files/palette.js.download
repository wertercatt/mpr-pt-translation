/* palette.js */
var toggleSubMenu = null, insertTempTag = null;
(function(){
	var debug = false;
	
	var palette = null;
	var domain  = "*";
	var targetWindow = parent.postMessage ? parent : (parent.document.postMessage ? parent.document : undefined);
	var parentUrl = location.href;
	var langCode = "";

	var query = location.href.split("?")[1].split("&");
	var dest = "", lang = "";
	for (var i in query) {
		if (query[i].match(/^u=/)) {
			dest = decodeURIComponent(query[i].replace("u=", ""));
		}
		if (query[i].match(/^lang=/)) {
			langCode = decodeURIComponent(query[i].replace("lang=", ""));
		}
	};

	var ie = (function(){
		var undef, v = 3, div = document.createElement('div');
		while (
			div.innerHTML = '<!--[if gt IE '+(++v)+']><i></i><![endif]-->',
			div.getElementsByTagName('i')[0]
		);
		return v > 4 ? v : undef;
	}());

	// 色選択
	var PALETTE = function() {
		this.colorSample = document.getElementById("sample");
		if (this.colorSample) {
			this.colorSample.appendChild(document.createTextNode(FC2Blog.Language.CommentTool.COLOR_SAMPLE_TEXT[langCode]));
		}
		return false;
	};
	PALETTE.prototype = {
		preview: function(color) {
			this.colorSample.style.color = "#" + color;
			return false;
		},
		insertTag: function(color) {
			var param = {
				start: "color:" + color,
				end  : "color",
				str  : "color"
			}
			send("instag", param);
		}
	};

	toggleSubMenu = function(target) {
		target = target || '';
		var method = "tglmenu";
		var param  = {target: target};
		
		send(method, param);
		return false;
	};
	
	insertTempTag = function(start, end, str) {
		var method = "instag";
		start = start;
		end   = end;
		str   = str;
		
		send(method, {start: start, end: end, str: str});
		return false;
	};
	
	previewColor = function(color) {
		palette.preview(color);
		return false;
	};
	
	insertColorTag = function(color) {
		palette.insertTag(color);
		return false;
	};
	
	var send = function(method, param) {
		method = escapeUnicode(method) || '';
		param  = (function(p){
			for (var i in p) {
				p[i] = escapeUnicode(p[i]);
			}
			return p;
		})(param) || '';
		var param = JSON.stringify({"m": method, "p": param});
		if (debug || !window.postMessage) {
			param = encodeURIComponent(param);
			parent.location = dest.replace( /#.*$/, '' ) + '#' + new Date().getTime() + '&' + param;
		} else {
			targetWindow.postMessage(param, "*");
		}
	};

	var escapeUnicode = function(str) {
		return str.replace(/[^ -~]|\\/g, function(m0) {
			var code = m0.charCodeAt(0);
			return '\\u' + ((code < 0x10)? '000' : 
			(code < 0x100)? '00' :
			(code < 0x1000)? '0' : '') + code.toString(16);
		});
	};

	var setTitle = function() {
		var elms = {};
		elms.bold_tool = document.getElementById("bold_tool");
		elms.italic_tool = document.getElementById("italic_tool");
		elms.underline_tool = document.getElementById("underline_tool");
		elms.strike_tool = document.getElementById("negated_tool");
		elms.color_tool = document.getElementById("color_tool");
		elms.icon_tool = document.getElementById("emoji_tool");
		for (var i in elms) {
			if (!elms[i]) continue;
			var title = i.replace("_tool", "").toUpperCase() + "_TAG_CAPTION";
			elms[i].children[0].setAttribute("title", FC2Blog.Language.CommentTool[title][langCode]);
		}
	};

	var init = function() {
		palette = new PALETTE();
		setTitle();
	}
	init();
})();
