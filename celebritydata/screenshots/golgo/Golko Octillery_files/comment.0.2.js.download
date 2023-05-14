if (!ldblogComment){
    var ldblogComment = {
        init : function () {
            if (location.hash == '#comment-form')
                this.checkLogin(document.getElementById('comment-login-link'), 0);
        },
        checkLogin : function (elm, jump) {
            if (!elm) return false;
            var api_url = elm.href.replace(/login$/, 'status');
            var obj = this;
            this.callJSONP(api_url, function (json) {
                if ( json.login == 1 ){
                    if (document.getElementById('comment-login-nickname'))
                        document.getElementById('comment-login-nickname').innerHTML = json.nickname;

                    document.getElementById('comment-author-form').innerHTML = json.nickname + '<input type="hidden" name="author" value="' + json.nickname + '" />';
                    document.getElementById('comment-login').style.display = "none";
                    document.getElementById('comment-logout').style.display = "";
                    if ( json.allowed == 1 ) {
                        document.getElementById('comment-form-body').style.display = "";
                    } else {
                        document.getElementById('authorized-err').style.display = "";
                    }
                }
                else if (jump == 1)
                    location.href = elm.href;
            });
            return false;
        },
        callJSONP : function (api_url, cb_func) {
            var uniq_name = "ldblog_comment_cb_" + Math.random().toString(36).slice(2);
            var scr = document.createElement("script");
            scr.type = "text/javascript";
            scr.src = api_url.indexOf('?', 0) > 0 ?
               api_url + '&callback=' + uniq_name :
               api_url + '?callback=' + uniq_name;
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
            obj.head = document.getElementsByTagName("head").item(0);
            setTimeout(function(){ obj.head.appendChild(scr); }, 100);
        }
    };
}
