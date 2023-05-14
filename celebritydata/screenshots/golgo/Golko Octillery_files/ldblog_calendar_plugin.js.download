if (!ldBlogCalendarPlugin){
  var ldBlogCalendarPlugin = function (id) {
    this.plugin_id = id;
    this.cnt = 0;
    var obj = this;
  };
  ldBlogCalendarPlugin.prototype = {
    init: function (delay) {
      var date = this.getDate();
      if (!date)
        return;
      var cal = this.makeCalArray(date);
      var year = (date.getYear() < 1900 ? date.getYear()+1900 : date.getYear());
      var month = date.getMonth() + 1;
      if (delay) {
        var elm = document.getElementById('calendarplugin-'+this.plugin_id);
        if (elm)
          elm.innerHTML = this.tmpl({ cal: cal, plugin_id: this.plugin_id, year: year, month: month });
      } else
        document.write( this.tmpl({ cal: cal, plugin_id: this.plugin_id, year: year, month: month }) );
      var data_url = ld_blog_vars.url + 'archives/' + year + '-' + (month < 10 ? '0'+month : month) + '.json';
      if (window['calendar_url_pattern_hash_'+this.plugin_id]) {
          data_url += '?_=' + window['calendar_url_pattern_hash_'+this.plugin_id];
      }
      this.getCalData(data_url);
    },
    setLink: function (data) {
      var header = document.getElementById('calendarhead-'+this.plugin_id);
      if (data.next_url && header)
        header.innerHTML = header.innerHTML + '<a href="'+ data.next_url +'" class="calendarnext">&gt;&gt;</a>';
      if (data.prev_url && header)
        header.innerHTML = '<a href="'+ data.prev_url +'" class="calendarpre">&lt;&lt;</a>' + header.innerHTML;
      for (var i = 0; i < data.daily_links.length; i++){
        var elm = document.getElementById('calendar-'+this.plugin_id+'-day-'+data.daily_links[i].day);
        if (elm) {
          var title = data.daily_links[i].title.replace(/\"/g, '&quot;');
          elm.innerHTML = '<a href="'+data.daily_links[i].link+'" class="acalendar" title="'+title+'">'+elm.innerHTML+'</a>';
          elm.parentNode.className = 'calon calendardbg';
        }
      }
    },
    makeCalArray: function (date) {
      var st = date.getDay();
      var year = (date.getYear() < 1900 ? date.getYear()+1900 : date.getYear());
      var month = date.getMonth() + 1;
      var last = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
      var lt_date = last[month];
      if (month == 2 && ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0))
        lt_date = 29;
      var cal = new Array();
      var len = ((lt_date + st) % 7 == 0) ? lt_date + st : lt_date + st + 7 - (lt_date + st) % 7;
      for ( var i = 1 - st, j = 0, w = 0, ww = 0; j<len; i++, j++ ) {
        if (!cal[w]) cal[w] = new Array();
        if (i <= 0 || i > lt_date)
          cal[w][ww] = '&nbsp;';
        else
          cal[w][ww] = i;
        if (++ww % 7 == 0) {
          w++; ww = 0;
        }
      }
      return cal;
    },
    getDate: function () {
      var obj = this;
      if (ld_blog_vars.current_page.type == 'monthly') {
        return new Date(ld_blog_vars.current_page.year, ld_blog_vars.current_page.month - 1, 1);
      } else if (ld_blog_vars.articles[0]) {
        ld_blog_vars.articles[0].date.match(/^([0-9]{4})-([0-9]{2})/);
        return new Date(RegExp.$1, RegExp.$2 - 1, 1);
      } else {
        this.cnt++;
        if (this.cnt < 10) {
          setTimeout(function () { obj.init(true); }, 100);
          return null;
        }
        else {
          var now = new Date();
          return new Date(now.getFullYear(), now.getMonth(), 1);
        }
      }
    },
    tmpl: function (data) { // original by John Resig http://ejohn.org/ 'JavaScript Micro-Templating' - MIT Licensed.
      var tmpl_data = this.getTmpl();
      var fn = new Function("obj", "var p=[],print=function(){p.push.apply(p,arguments);};with(obj){p.push('" +
        tmpl_data.replace(/[\r\t\n]/g, " ").split("<%").join("\t").replace(/((^|%>)[^\t]*)'/g, "$1\r").replace(/\t=(.*?)%>/g, "',$1,'").split("\t").join("');").split("%>").join("p.push('").split("\r").join("\\'") +
        "');}return p.join('');");
      return fn( data );
    },
    getTmpl: function () {
      var custom = document.getElementById('ldblog_calendar_template');
      return custom ? custom.innerHTML : document.getElementById('ldblog_calendar_default_template-'+this.plugin_id).innerHTML;
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
    getCalData: function (url) {
      var obj = this;
      var xhr = this.xhr();
      if (!xhr)
        return;
      xhr.open('GET', url, true);
      xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
          eval('var ld_cal_json = ' + xhr.responseText);
          obj.setLink(ld_cal_json);
        }
      };
      xhr.send();
    }
  };
}
