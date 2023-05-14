var RecentComments = (function(){
    var RC = function(target){
        this.target = target;
        this.wrapper = document.getElementById(target+'_list');
        this.order = this.wrapper.getAttribute('data-order');
        this.rows = this.wrapper.getAttribute('data-rows');
        this.api_url = ld_blog_vars.url+'_/recent_comments.json?limit='+this.rows+'&_='+(new Date()).getTime();
    };

    RC.prototype = {
        tmpl: function (data) { // original by John Resig http://ejohn.org/ 'JavaScript Micro-Templating' - MIT Licensed.
            var tmpl_data = document.getElementById(this.target+'_tmpl').innerHTML;
            var fn = new Function("obj", "var p=[];with(obj){p.push('" +
                                  tmpl_data.replace(/[\r\t\n]/g, " ").split("<%").join("\t").replace(/(^|%>)[^\t]*?(\t|$)/g,function(){return arguments[0].split("'").join("\\'");}).replace(/\t==(.*?)%>/g,"',$1,'").replace(/\t=(.*?)%>/g, "',(($1)+'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\"/g,'&quot;'),'").split("\t").join("');").split("%>").join("p.push('") +
                                  "');}return p.join('');");
            return fn( data );
        },
        xhr: function () {
            if (window.XMLHttpRequest)
                return new XMLHttpRequest();
            else {
                var msxml = [
                    "Msxml2.ServerXMLHTTP.6.0", "Msxml2.ServerXMLHTTP.5.0", "Msxml2.ServerXMLHTTP.4.0", "Msxml2.ServerXMLHTTP.3.0",
                    "Msxml2.ServerXMLHTTP", "Microsoft.ServerXMLHTTP", "Msxml2.XMLHTTP.6.0", "Msxml2.XMLHTTP.5.0",
                    "Msxml2.XMLHTTP.4.0", "Msxml2.XMLHTTP.3.0", "Msxml2.XMLHTTP", "Microsoft.XMLHTTP"
                ];
                for (var i = 0; i<msxml.length; i++ ){
                    try {
                        return new ActiveXObject(msxml[i]);
                    }
                    catch(e) { }
                }
                return null;
            }
        },
        render: function () {
            var self = this;
            var xhr = this.xhr();
            if (!xhr) return;
            xhr.open('GET', self.api_url, true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    eval('var _json = ' + xhr.responseText);
                    _json.order = self.order;
                    self.wrapper.innerHTML = self.tmpl(_json);
                }
            };
            xhr.send();
        }
    };

    return RC;
})();
