(function () {

    var hd = document.createElement('div');
    var date = new Date();
    var month = date.getMonth()+1;
    var day = date.getDate();
    var str = '';

    str += '<div id="header2" style="z-index:10001"><table cellspacing="0" class="blog-common-header" id="header">';
    str += '<tr>';
    str += '<th><span class="common-header-logo"><a href="http://blog.livedoor.com/?_h_jp_pc=logo"><img height="17" width="43" alt="livedoor" src="https://parts.blog.livedoor.jp/img/user_blog/livedoor/logo_livedoor.gif" /></a><a href="http://blog.livedoor.com/?_h_jp_pc=logo"><img height="17" width="49" alt="livedoor Blog - ' + unescape('%u7121%u6599/%u6709%u6599%u30D6%u30ED%u30B0%u30B5%u30FC%u30D3%u30B9') + '" src="https://parts.blog.livedoor.jp/img/user_blog/livedoor/logo_blog.gif" /></a></span></th>';
    str += '<td class="catprbox"><span class="common-header-category">';
    if (typeof(ld_blog_vars) == 'object' && ld_blog_vars.blog_category) {
        if (ld_blog_vars.blog_category.is_adult) {
            str += ld_blog_vars.blog_category.name.replace(/^.+ > /,'');
        } else {
            str += '<a href="' + ld_blog_vars.blog_category.permalink + '?_h_jp_pc=category">' + ld_blog_vars.blog_category.name.replace(/^.+ > /,'') + '</a>';
        }
    }
    str += '</span></td>';
    str += '<td class="newstickerbox"><span class="common-header-pr"></span></td>';
    str += '<td class="pickuptheme">';

    str += '<td class="startblogbox startblogboxEntry">';
    str += '<a href="http://livedoor.blogcms.jp/member/">\u30d6\u30ed\u30b0\u3092\u66f8\u304f</a>';
    str += '</td>';

//        str += '<img alt="' + unescape('3D%u30C6%u30EC%u30D3%u306B%u8208%u5473%u306F%u3042%u308A%u307E%u3059%u304B%3F%28%u30D7%u30EC%u30BC%u30F3%u30C8%u4ED8%u304D%29') + '" src="https://parts.blog.livedoor.jp/img/user_blog/livedoor/pickup.gif" /><a href="http://blogpark.jp/common_theme-196840.html">' + unescape('3D%u30C6%u30EC%u30D3%u306B%u8208%u5473%u306F%u3042%u308A%u307E%u3059%u304B%3F%28%u30D7%u30EC%u30BC%u30F3%u30C8%u4ED8%u304D%29') + '</a>';
    str += '</td>';
    str += '<td class="startblogbox">';
    str += '<a href="http://blog.livedoor.com/news/?_h_jp_pc=news">'+ month +'\u6708' + day +"\u65E5"+'\u8A71\u984C\u306E\u8A18\u4E8B</a>';
    str += '</td>';
    str += '</tr>';
    str += '</table></div>';
    str += '<style type="text/css">';
    str += 'table#header{width:100%;height:20px!important;font-size:10px!important;margin:0!important;padding:0!important;}';
    str += 'table#header,table#header input{font-family:"' + unescape('%uFF2D%uFF33%20%uFF30%u30B4%u30B7%u30C3%u30AF') + '",Arial,Helvetica,sans-serif!important;}';
    str += 'table#header a{text-decoration:none!important;}';
    str += 'table#header img{border:0;vertical-align:top;}';
    str += 'table#header th{width:1%;}';
    str += 'table#header th img{margin:0;}';
    str += 'table#header span.common-header-logo{white-space:nowrap;margin:0 20px 0 10px;zoom:1;}';
    str += 'table#header span.common-header-category{margin-right:20px;}';
    str += 'table#header td.newstickerbox{width:97%;}';
    str += 'table#header td.startblogbox{width:1%;white-space:nowrap;padding:0;}';
    str += 'table#header td.catprbox{width:1%;white-space:nowrap;}';
    str += 'table#header td.catprbox span{margin-right:15px;}';
    str += 'table#header td.pickuptheme{width:1%;white-space:nowrap;}';
    str += 'table#header form{margin:0 10px 0 0;padding:2px 0 2px 0;}';
    str += 'table#header input{border:1px solid #d2d2d2;border-radius:2px;outline:0;vertical-align:top;}';
    str += 'table#header input.text{width:200px;background:#fff url(https://parts.blog.livedoor.jp/img/user_blog/livedoor/search_icon.png) no-repeat 2px 1px;padding:0 5px 0 19px;margin-right:5px;font-size:13px!important;line-height:15px;height:15px;box-shadow:0 2px 4px rgba(0,0,0,0.1) inset;}';
    str += 'table#header input:focus,table#header input.imgBtn:hover{border:1px solid #aaa;}';
    str += '</style>';

    str += '<style type="text/css">';
    str += 'table#header{width:100%;height:20px!important;font-size:10px!important;margin:0!important;padding:0!important;}';
    str += 'table#header,table#header input{font-family:"\uFF2D\uFF33 \uFF30\u30B4\u30B7\u30C3\u30AF",Arial,Helvetica,sans-serif!important;}';
    str += 'table#header a{text-decoration:none!important;}';
    str += 'table#header img{border:0;vertical-align:top;}';
    str += 'table#header th{width:1%;}';
    str += 'table#header th img{margin:0;}';
    str += 'table#header span.common-header-logo{white-space:nowrap;margin:0 20px 0 10px;zoom:1;}';
    str += 'table#header span.common-header-category{margin-right:20px;}';
    str += 'table#header td.newstickerbox{width:97%;}';
    str += 'table#header td.startblogbox{white-space:nowrap;padding:0;padding:0 10px 0 21px;font-size:12px;vertical-align:middle;background:url(https://parts.blog.livedoor.jp/img/user_blog/livedoor/calendar_icon.png) no-repeat center left;zoom:1;}';
    str += 'table#header td.startblogbox.startblogboxEntry{background:url(https://parts.blog.livedoor.jp/img/user_blog/livedoor/entry_icon.png) no-repeat center left;padding-right: 15px;}';
    str += 'table#header td.catprbox{width:1%;white-space:nowrap;}';
    str += 'table#header td.catprbox span{margin-right:15px;}';
    str += 'table#header td.pickuptheme{width:1%;white-space:nowrap;}';
    str += '</style>';

    hd.innerHTML = str;

    document.body.appendChild(hd);

    var deleteCount = 0;

    deleteOldHeader = function () {
        if (deleteCount++ > 0) return;
        var tables = document.getElementsByTagName("table");
        for(var i=0;  i<tables.length; i++) {
            if(tables[i].id == "header" && tables[i].parentNode.tagName == "BODY" && tables[i].parentNode.id != "header2") {
                tables[i].parentNode.removeChild(tables[i]);
                break;
            }
        }
        if (typeof(ld_blog_vars) == 'object') {
            ld_category_ad_encoding = ld_blog_vars.charset;
        }
    };

    if (navigator.userAgent.indexOf('AppleWebKit/') > -1) {
        var _interval = window.setInterval(function () {
            var st = document.readyState;
            if (st == 'complete' || st == 'loaded') {
                window.clearInterval(_interval);
                deleteOldHeader();
            }
        }, 100);
    } else if (window.attachEvent && !window.opera) {
        this.ie = 1;
        document.write('<scr' + 'ipt defer src="javascript:void(0)" onreadystatechange="if (document.readyState == \'complete\') deleteOldHeader();"></scr' + 'ipt>');
        window.attachEvent('onload', deleteOldHeader);
    } else {
        document.addEventListener("DOMContentLoaded", deleteOldHeader, false);
        window.addEventListener("load", deleteOldHeader, false);
    }

    var load_library_on_load = function (script_src, onload_callback_func) {
       var head = document.getElementsByTagName('head').item(0);
       var scr = document.createElement('script');
       scr.type = 'text/javascript';
       scr.onreadystatechange = function () {
          if (window.opera || this.readyState != 'loaded' || this.className == 'processed')
             return;
          this.className = 'processed';
          onload_callback_func();
       };
       scr.onload = function () {
          if (this.className == 'processed')
             return;
          this.className = 'processed';
          onload_callback_func();
       };
       if (scr.className == 'processed'){
          onload_callback_func();
       }
       scr.src = script_src;
       head.appendChild(scr);
       window.setTimeout(function(){
                            if (scr.className != 'processed')
                               onload_callback_func();
                         }, 300);
    };

    var call_jsonp = function (api_url, cb_func) {
        var uniq_name = 'ld_ads';
        var scr = document.createElement('script');
        scr.type = 'text/javascript';
        scr.charset = this.charset;
        scr.src = api_url + '&callback=' + uniq_name;
        scr.id = uniq_name;
        var obj = this;
        window[uniq_name] = function (json) {
            cb_func(json);
            var u_name = uniq_name;
            setTimeout(function() {
                obj.head.removeChild(document.getElementById(u_name));
                try{
                    window[u_name] = null;
                    delete window[u_name];
                } catch (e) {};
            }, 200);
        };

        obj.head = document.getElementsByTagName('head').item(0);
        setTimeout(function(){ obj.head.appendChild(scr); }, 100);
    };

    var load_ads = function (script_list) {
        call_jsonp(script_list.shift(), function (json) {
            if (!json) return;
            var element = document.createElement('div');
            element.id = "ld_header_ads";
            element.innerHTML = json.tag;
            document.getElementById('header2').appendChild(element);
        });
        return false;
    };

    var add_listener = (
       function() {
          if ( window.addEventListener ) {
             return function(target, type, func) {
                target.addEventListener(type, func, false);
                return true;
             };
          } else if( window.attachEvent ) {
             return function(target, type, func) {
                target.attachEvent("on"+type, func);
                return true;
             };
          } else {
             return function(target, type, func) {
                return false;
             };
          }
       })();

    add_listener(document, "mouseup",
       function(){
          var txt = '';
          if (window.getSelection) { txt = window.getSelection(); }
          else if (document.getSelection) { txt = document.getSelection(); }
          else if (document.selection) { txt = document.selection.createRange().text; }

          if (txt && txt != '') {
             var elm = document.getElementById('header2_query');
             if (elm) { elm.value = txt; }
          }
       }
    );

 })();
