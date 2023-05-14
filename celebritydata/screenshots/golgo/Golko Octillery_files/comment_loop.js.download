var LDBlogCommentLoop = function(count, entries_per_page, desc, num_base, skip, is_tree) {
    this.json_url = ld_blog_vars.url+'archives/'+ld_blog_vars.articles[0].id+'/comment.json';
    this.article_id = ld_blog_vars.id+'-'+ld_blog_vars.articles[0].id;
    this.last = Math.floor(count / entries_per_page) + (count % entries_per_page ? 1 : 0);
    this.desc = desc;
    this.page = is_tree && desc ? 1 : 0;
    this.num_base = num_base;
    this.skip = skip;
    this.init();
    this.is_tree = is_tree;
};
LDBlogCommentLoop.prototype = {
    init: function() {
        this.create_tmpl('ld_blog_article_comment_entries_tmpl');
        this.entries_wrapper    = document.getElementById('ld_blog_article_comment_entries');
        this.comment_pager      = document.getElementById('ld_blog_article_comment_pager');
        this.comment_pager_link = document.getElementById('ld_blog_article_comment_pager_link');
        this.comment_loading    = document.getElementById('ld_blog_article_comment_loading');
    },
    next: function() {
      if (this.is_tree && this.desc) {
        this.load(this.page + 1)
      } else {
        this.load(((this.page == 0)?this.last:this.page) - 1)
      }
    },
    load: function(page) {
        this.page = page;
        var self = this;
        self.loading(1);
        this.get(self.json_url, { p: page }, function(res) {
            self.render_entries(res);
            self.loading(0);
            if (window.Animation) {
              __comment_animation = null;
              __comment_animation = new Animation.Hover('.comment-like');
            }
        });
    },
    loading: function(flg) {
        if (flg)
            this.comment_pager_link.style.display = 'none', this.comment_loading.style.display = 'block'
        else
            this.comment_pager_link.style.display = 'block', this.comment_loading.style.display = 'none';
    },
    render_entries: function(res) {
        var tmp = [];
        for (var i=0,l=res.comments.length; i<l; i++) {
            var ii = (!this.is_tree &&this.desc) ? (l-i-1) : i;
            var entry = res.comments[ii];
            if (!this.is_tree && this.skip <= entry.id) {
                if (this.desc) continue
                else break;
            }
            entry.odd_even = (i%2==1) ? 'odd' : 'even';
            if (this.num_base)
                entry.num += this.num_base;
            tmp.push(this.tmpl({entry:entry}));
        }

        var ul = document.createElement('ul');
        ul.innerHTML = tmp.join('');

        if (window.LDBlogConvertEmoji) {
            window.LDBlogConvertEmoji(ul);
        }

        var fragment = document.createDocumentFragment();
        while (ul.firstChild)
            fragment.appendChild(ul.firstChild);

        if (this.desc)
            this.entries_wrapper.appendChild(fragment)
        else
            this.entries_wrapper.insertBefore(fragment, this.entries_wrapper.firstChild);
        if ((this.is_tree && this.desc && this.page == this.last) || (!(this.is_tree && this.desc) && this.page == 1))
            this.comment_pager.style.display = 'none';
    },
    xhr: function () {
        if (window.XMLHttpRequest)
            return new XMLHttpRequest();
        else if (this._msxml)
            return new ActiveXObject(this._msxml);
        else {
            var msxml = [
                "Msxml2.ServerXMLHTTP.6.0", "Msxml2.ServerXMLHTTP.5.0", "Msxml2.ServerXMLHTTP.4.0", "Msxml2.ServerXMLHTTP.3.0",
                "Msxml2.ServerXMLHTTP", "Microsoft.ServerXMLHTTP", "Msxml2.XMLHTTP.6.0", "Msxml2.XMLHTTP.5.0",
                "Msxml2.XMLHTTP.4.0", "Msxml2.XMLHTTP.3.0", "Msxml2.XMLHTTP", "Microsoft.XMLHTTP"
            ];
            for (var i=0,l=msxml.length; i<l; i++){
                try {
                    var xhr = new ActiveXObject(msxml[i]);
                    this._msxml = msxml[i];
                    return xhr;
                }
                catch(e) { }
            }
            return null;
        }
    },
    get: function (api, params, onload) {
        if ( !params ) params = {};
        params['t'] = + new Date;
        var queries = [];
        for ( var key in params )
            queries.push( key + '=' + encodeURIComponent(params[key]) );
        var xhr = this.xhr(),
            tid = setTimeout(function () {
                xhr.abort();
                clearTimeout(tid);
                tid = xhr = null;
            }, 10000);
        if (!xhr)
            return;
        xhr.open('GET', api + '?' + queries.join('&'), true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                if ( tid != null ) clearTimeout(tid), ( tid = null );
                eval('var data = ' + xhr.responseText);
                return onload(data, xhr);
            }
        };
        xhr.send(null);
    },
    create_tmpl: function(id) {
        if (this.tmpl) return this.tmpl;
        var str = document.getElementById(id).innerHTML;
        // Simple JavaScript Templating
        // John Resig - http://ejohn.org/ - MIT Licensed
        this.tmpl
            = new Function("obj",
                           "var p=[];" +
                           "with(obj){p.push('" +
                           str
                           .replace(/[\r\t\n]/g, " ")
                           .split("<%").join("\t")
                           .replace(/(^|%>)[^\t]*?(\t|$)/g, function(){return arguments[0].split("'").join("\\'");})
                           .replace(/\t==(.*?)%>/g,"',$1,'")
                           .replace(/\t=(.*?)%>/g, "',(($1)+'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\"/g,'&quot;'),'")
                           .split("\t").join("');")
                           .split("%>").join("p.push('")
                           + "');}return p.join('');");
        return this.tmpl;
    }
};
