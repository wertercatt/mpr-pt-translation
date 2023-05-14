/* icon.js */
var insertIcon;
(function(){
	var debug = false;
	
	// icon page number
	var ICON_E_PAGE = 5;
	var ICON_I_PAGE = 2;
	var ICON_V_PAGE = 5;
	
	var icon = null;
	var mapResourceDir = "sample/";
	var imageDir       = "image/";
	var host           = "static.fc2.com/js/blog/view/comment/";
	
	var query = location.href.split("?")[1].split("&");
	var dest = "";
	for (var i in query) {
		if (query[i].match(/^u=/)) {
			dest = decodeURIComponent(query[i].replace("u=", ""));
			break;
		}
	}
	
	var iconTab = null;
	var domain  = "*";
	var targetWindow = parent.postMessage ? parent : (parent.document.postMessage ? parent.document : undefined);
	
	var ie = (function(){
		var undef, v = 3, div = document.createElement('div');
		while (
			div.innerHTML = '<!--[if gt IE '+(++v)+']><i></i><![endif]-->',
			div.getElementsByTagName('i')[0]
		);
		return v > 4 ? v : undef;
	}());
	
	toggleIconTab = function(num) {
		icon.toggleIconTab(num);
		return false;
	};
	
	toggleSubMenu = function(target) {
		target = target || '';
		var method = "tglmenu";
		var param  = {target: target};
		
		send(method, param);
		return false;
	};
	
	var send = function(method, param) {
		var param = JSON.stringify({"m": method, "p": param});
		if (debug || !window.postMessage) {
			param = encodeURIComponent(param);
			parent.location = dest.replace( /#.*$/, '' ) + '#' + new Date().getTime() + '&' + param;
		} else {
			targetWindow.postMessage(param, "*");
		}
	};
	
	var setHeight = function(obj) {
		if (!obj) return;
		var height = (obj.height)? obj.height: '';
		send("seth", {target: "icon", height: height});
	};
	
	var escapeUnicode = function(str) {
		return str.replace(/[^ -~]|\\/g, function(m0) {
			var code = m0.charCodeAt(0);
			return '\\u' + ((code < 0x10)? '000' : 
			(code < 0x100)? '00' :
			(code < 0x1000)? '0' : '') + code.toString(16);
		});
	};
	
	insertIcon = function(career,no) {
		icon.insertIcon(career,no);
	};
	
	var ICON = function() {
		this.CLICK_MAP = {
			prefix: "emoji_",
			page  : {
				e: ICON_E_PAGE,
				i: ICON_I_PAGE,
				v: ICON_V_PAGE
			}
		};
		this.MAP_PARAMS = {
			v: {
				1: { v_num: 10, h_num: 12, size : 15, margin: 5, limit: false },
				2: { v_num: 10, h_num: 12, size : 15, margin: 5, limit: false },
				3: { v_num: 10, h_num: 12, size : 15, margin: 5, limit: false },
				4: { v_num: 10, h_num: 12, size : 15, margin: 5, limit: false },
				5: { v_num: 6, h_num: 12, size : 15, margin: 5, limit: 61 }
			},
			i: {
				1: { v_num: 12, h_num: 12, size : 12, margin: 5, limit: false },
				2: { v_num: 12, h_num: 12, size : 12, margin: 5, limit: 138 }
			},
			e: {
				1: { v_num: 10, h_num: 12, size : 13, margin: 5, limit: false },
				2: { v_num: 10, h_num: 12, size : 13, margin: 5, limit: false },
				3: { v_num: 10, h_num: 12, size : 13, margin: 5, limit: false },
				4: { v_num: 10, h_num: 12, size : 13, margin: 5, limit: false },
				5: { v_num: 4, h_num: 12, size : 13, margin: 5, limit: 38 }
			}
		};
	
		this.clickableMap = {};
	};
	ICON.prototype = {
		request: function(val, callback) {
			return this.Core.request(val, callback);
		},
		
		insertIcon: function(career,no) {
			var param = {
				start: "icon:" + career + "-" + no + "",
				end  : "",
				str  : ""
			}
			send("instag", param);
			return;
		},
		
		onclickIconImage: function() {
			var alt = $(this).attr("alt");
			alt = alt.split("_");
			icon.insertIcon(alt[0], alt[1]);
		},
		
		toggleIconTab: function(num) {
			num = ("undefined" != typeof num)? num - 1 : 0;
			var tab   = document.getElementById("emoji_tab");
			var table = document.getElementById("emoji_table");
			var max   = tab.children.length -1;
			for (var i = 0; i < max; i++) {
				if (ie) {
					tab.children[i].className = "";
					table.children[i].className = "";
				} else {
					tab.children[i].removeAttribute("class", "tab_target");
					table.children[i].removeAttribute("class", "tab_target");
				}
			};
			if (0 <= num) {
				if (ie) {
					tab.children[num].className = "tab_target";
					table.children[num].className = "tab_target";
				} else {
					tab.children[num].setAttribute("class", "tab_target");
					table.children[num].setAttribute("class", "tab_target");
				}
			};
			return false;
		},
		
		generateClickableMap: function(career, page) {
			if (!career || !parseInt(page)) return;
			
			var career     = career;
			var currentPage= parseInt(page);
			var pageSetting= icon.MAP_PARAMS[career][currentPage];
			
			var verticval  = pageSetting.v_num;
			var horizontal = pageSetting.h_num;
			var html       = "";
			var htmlList   = [];
			var count      = 1;
			var size       = pageSetting.size;
			var margin     = pageSetting.margin;
			
			var start = (function(){
				var num   = 0;
				var count = 1;
				for (var page in icon.MAP_PARAMS[career]) {
					if (currentPage <= count || !icon.MAP_PARAMS[career][page]) break;
					
					if (!icon.MAP_PARAMS[career][page].limit) {
						num += icon.MAP_PARAMS[career][page]['v_num'] * icon.MAP_PARAMS[career][page]['h_num'];
					} else {
						num += icon.MAP_PARAMS[career][page].limit;
					}
					count++;
				};
				return num + 1;
			})();
		
			var number = start;
			var limit = (false === pageSetting.limit)? false: pageSetting.limit;
			for (var v = 0; v < verticval; v++) {
				for (var h = 0; h < horizontal; h++) {
					var left  = (size + margin) * h;
					var top   = (size + margin) * v;
					var right = left + size;
					var bottom= top + size;
					var coords= left + "," + top + "," + right + "," + bottom;
					
					var imgIcon = $("<img />").attr("alt", career + "_" + number)
						.attr("src", "//static.fc2.com/share/fc2footermenu/blank.gif")
						.addClass("page_" + career + page + " " + "icon_" + career + number);
					
					htmlList.push(imgIcon);
					if (false !== limit) {
						if (limit <= count) break;
					}
					count++;
					number++;
				}
			};
			// return html;
			return htmlList;
		},
		
		Pager: {
			iconPagerInit: function() {
				var prefix = icon.CLICK_MAP.prefix;
				
				for (var prop in icon.CLICK_MAP.page) {
					icon.clickableMap[prop] = {};
					var page_num = icon.CLICK_MAP.page[prop];
					
					for (var i = 1; i <= page_num; i++) {
						var par = document.getElementById("pager_" + prefix + prop);
						var anchor = document.createElement("a");
						anchor.setAttribute("href", "javascript:;");
						anchor.setAttribute("page", i);
						anchor.setAttribute("carr", prop);
						if (1 == i) {
							if (ie) {
								anchor.className = "currentPage";
							} else {
								anchor.setAttribute("class", "currentPage");
							}
						};
						anchor.appendChild(document.createTextNode(i));
						
						if (ie) {
							// attach
							anchor.attachEvent("onclick", function(e){
								icon.Pager.oncickIconPager((e.target? this : e.srcElement));
								return false;
							});
						} else {
							anchor.addEventListener("click", function(e){
								icon.Pager.oncickIconPager((e.target? this : e.srcElement));
								return false;
							});
						}
						par.appendChild(anchor);
						
						var path = mapResourceDir + prefix + prop + i + ".html";
						this._requestFiles(prop, i);
					}
				}
			},
			
			refleshContents: function(prop, idx) {
				var map = icon.clickableMap[prop][idx];
				var par = document.getElementById(icon.CLICK_MAP.prefix + prop);
				
				$(par).empty();
				var delay = setTimeout(function(){
					for (var i in map) {
						$(par).append(
							$(map[i]).on("click", icon.onclickIconImage)
						);
					}
					clearTimeout(delay);
				}, 50);
			},
			
			oncickIconPager: function(elm) {
				if ("object" != typeof elm) return;

				var page   = elm.getAttribute("page");
				var career = elm.getAttribute("carr");
				// var id     = "image_" + icon.CLICK_MAP.prefix + career;
				// var img    = document.getElementById(id);
				var par = document.getElementById("pager_" + icon.CLICK_MAP.prefix + career);

				var children = par.children;
				var pagerlist = [];
				for (var i = 0; i < children.length; i++) {
					if ("A" == children[i].tagName.toUpperCase()) {
						pagerlist.push(children[i]);
					}
				}
				for (var l = 0; l < pagerlist.length; l++) {
					icon.Util.rmClass(pagerlist[l], "currentPage");
				}
				icon.Util.addClass(pagerlist[page - 1], "currentPage");
				
				this.refleshContents(career, page);
				return false;
			},
			_requestFiles: function(prop, idx) {
				var map = icon.generateClickableMap(prop, idx);
				icon.clickableMap[prop][idx] = map;
			}
		},
		
		Util: {
			addClass: function(target, name) {
				if (ie) {
					var c = target.className || target.getAttribute("className");
					target.className = (c? c + " ": "") + name;
				} else {
					var c = target.getAttribute("class");
					target.setAttribute("class", (c? c + " ": "") + name);
				}
			},
			replaceClass: function(target, name) {
				if (ie) {
					target.className = name;
				} else {
					target.setAttribute("class", name);
				}
			},
			rmClass: function(target, name) {
				if (ie) {
					var c = target.className || target.getAttribute("className");
					if (c) target.className = c.replace(name, "");
				} else {
					var c = target.getAttribute("class");
					if (c) target.removeAttribute("class", name);
				}
			}
		},
		
		Core: {
			request: function(pageUrl, callback) {
				var self = this;
				var cb   = callback;
				var xhr = self.createXHR();
				xhr.onreadystatechange = function() {
					 if (xhr.readyState == 4) {
						if (xhr.status == 200) {
							// success
							if ("function" == typeof cb) {
								cb(xhr.responseText);
							} else {
								return xhr.responseText;
							}
						} else {
							// error
						};
					};
				};
				var param = "";
				if ("object" == typeof val) {
					for (var i in val) {
						param += i + "=" + val[i] + "&";
					};
				};
				param += "time=" + this.getTime();
				var url = "https://" + host + pageUrl + "?" + param;
				
				xhr.open("get", url, true);
				xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
				xhr.send();
			},
			createXHR: function() {
				if(XMLHttpRequest){return new XMLHttpRequest()}
				if(ActiveXObject){
					var a = "Msxml2.XMLHTTP.", b = [a + "6.0", a + "3.0", "Microsoft.XMLHTTP"];
					for (var i = 0; i < b.length; i++) {
						try {
							return new ActiveXObject(b[i])
						} catch (ex) {}
					};
				};
				return false;
			},
			
			getTime: function() {
				return new Date().getTime();
			}
		}
	};
	
	var init = function() {
		icon = new ICON();
		icon.Pager.iconPagerInit();
		icon.toggleIconTab();
		icon.Pager.refleshContents("v", 1);
	}
	
	try {
		window.addEventListener("load", init, false);
	} catch (ex) {
		window.attachEvent("onload", init);
	}
	
})();
