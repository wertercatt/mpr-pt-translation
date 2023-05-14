if (typeof RelatedArticles === 'undefined') {
var RelatedArticles = (function(){
    var RA = function(target, category_id, article_id){
        this.target = target;
        this.category_id = category_id;
        this.wrapper = document.getElementById(target+'_'+this.category_id);
        this.api_url = ld_blog_vars.url+'_/category/'+this.category_id+'.json?ignore_id='+article_id;
    };

    RA.prototype = {
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
        render: function (rows) {
            var self = this;
            var xhr = this.xhr();
            if (!xhr) return;
            xhr.open('GET', self.api_url, true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    eval('var articles_json = ' + xhr.responseText);
                    articles_json.rows = rows;
                    if (articles_json.articles.length === 0) {
                      self.wrapper.parentNode.innerHTML = '';
                    } else {
                      self.wrapper.innerHTML = self.tmpl(articles_json);
                    }
                }
            };
            xhr.send();
        }
    };

    RA.load = function(target, article_id){
        if (!article_id) article_id = '';
        var parent = document.getElementById(target);
        var ctgs = [];
        if (parent.querySelectorAll)
            ctgs = parent.querySelectorAll('.'+target);
        else {
            var reg = new RegExp('(^|\\s+)'+target+'($|\\s+)');
            var tags = parent.getElementsByTagName('*');
            for (var i=0,l=tags.length;i<l;i++) {
                if (reg.test(tags[i].className))
                    ctgs.push(tags[i]);
            }
        }
        for (var i=0,l=ctgs.length;i<l;i++) {
            var id = ctgs[i].getAttribute('data-category-id');
            var no = ctgs[i].getAttribute('data-no');
            var rows = ctgs[i].getAttribute('data-article-rows');
            var ra = new RelatedArticles(target, id, article_id, no);
            ra.render(rows);
        }
    };

    return RA;
})();
}
