!function() {
    function e(e) {
        return e.replace(y, "").replace(w, ",").replace(b, "").replace(x, "").replace(T, "").split(E)
    }
    function n(e) {
        return "'" + e.replace(/('|\\)/g, "\\$1").replace(/\r/g, "\\r").replace(/\n/g, "\\n") + "'"
    }
    function t(t, r) {
        function a(e) {
            return p += e.split(/\n/).length - 1,
            s && (e = e.replace(/\s+/g, " ").replace(/<!--[\w\W]*?-->/g, "")),
            e && (e = v[1] + n(e) + v[2] + "\n"),
            e
        }
        function i(n) {
            var t = p;
            if (u ? n = u(n, r) : o && (n = n.replace(/\n/g, function() {
                return p++,
                "$line=" + p + ";"
            })),
            0 === n.indexOf("=")) {
                var a = f && !/^=[=#]/.test(n);
                if (n = n.replace(/^=[=#]?|[\s;]*$/g, ""),
                a) {
                    var i = n.replace(/\s*\([^\)]+\)/, "");
                    $[i] || /^(include|print)$/.test(i) || (n = "$escape(" + n + ")")
                } else
                    n = "$string(" + n + ")";
                n = v[1] + n + v[2]
            }
            return o && (n = "$line=" + t + ";" + n),
            h(e(n), function(e) {
                if (e && !d[e]) {
                    var n;
                    n = "print" === e ? w : "include" === e ? b : $[e] ? "$utils." + e : g[e] ? "$helpers." + e : "$data." + e,
                    x += e + "=" + n + ",",
                    d[e] = !0
                }
            }),
            n + "\n"
        }
        var o = r.debug
          , c = r.openTag
          , l = r.closeTag
          , u = r.parser
          , s = r.compress
          , f = r.escape
          , p = 1
          , d = {
            $data: 1,
            $filename: 1,
            $utils: 1,
            $helpers: 1,
            $out: 1,
            $line: 1
        }
          , m = "".trim
          , v = m ? ["$out='';", "$out+=", ";", "$out"] : ["$out=[];", "$out.push(", ");", "$out.join('')"]
          , y = m ? "$out+=text;return $out;" : "$out.push(text);"
          , w = "function(){var text=''.concat.apply('',arguments);" + y + "}"
          , b = "function(filename,data){data=data||$data;var text=$utils.$include(filename,data,$filename);" + y + "}"
          , x = "'use strict';var $utils=this,$helpers=$utils.$helpers," + (o ? "$line=0," : "")
          , T = v[0]
          , E = "return new String(" + v[3] + ");";
        h(t.split(c), function(e) {
            e = e.split(l);
            var n = e[0]
              , t = e[1];
            1 === e.length ? T += a(n) : (T += i(n),
            t && (T += a(t)))
        });
        var j = x + T + E;
        o && (j = "try{" + j + "}catch(e){throw {filename:$filename,name:'Render Error',message:e.message,line:$line,source:" + n(t) + ".split(/\\n/)[$line-1].replace(/^\\s+/,'')};}");
        try {
            var S = new Function("$data","$filename",j);
            return S.prototype = $,
            S
        } catch (e) {
            throw e.temp = "function anonymous($data,$filename) {" + j + "}",
            e
        }
    }
    var r = function(e, n) {
        return "string" == typeof n ? m(n, {
            filename: e
        }) : o(e, n)
    };
    r.version = "3.0.0",
    r.config = function(e, n) {
        a[e] = n
    }
    ;
    var a = r.defaults = {
        openTag: "<%",
        closeTag: "%>",
        escape: !0,
        cache: !0,
        compress: !1,
        parser: null
    }
      , i = r.cache = {};
    r.render = function(e, n) {
        return m(e)(n)
    }
    ;
    var o = r.renderFile = function(e, n) {
        var t = r.get(e) || d({
            filename: e,
            name: "Render Error",
            message: "Template not found"
        });
        return n ? t(n) : t
    }
    ;
    r.get = function(e) {
        var n;
        if (i[e])
            n = i[e];
        else if ("object" == typeof document) {
            var t = document.getElementById(e);
            if (t) {
                var r = (t.value || t.innerHTML).replace(/^\s*|\s*$/g, "");
                n = m(r, {
                    filename: e
                })
            }
        }
        return n
    }
    ;
    var c = function(e, n) {
        return "string" != typeof e && (n = typeof e,
        "number" === n ? e += "" : e = "function" === n ? c(e.call(e)) : ""),
        e
    }
      , l = {
        "<": "&#60;",
        ">": "&#62;",
        '"': "&#34;",
        "'": "&#39;",
        "&": "&#38;"
    }
      , u = function(e) {
        return l[e]
    }
      , s = function(e) {
        return c(e).replace(/&(?![\w#]+;)|[<>"']/g, u)
    }
      , f = Array.isArray || function(e) {
        return "[object Array]" === {}.toString.call(e)
    }
      , p = function(e, n) {
        var t, r;
        if (f(e))
            for (t = 0,
            r = e.length; t < r; t++)
                n.call(e, e[t], t, e);
        else
            for (t in e)
                n.call(e, e[t], t)
    }
      , $ = r.utils = {
        $helpers: {},
        $include: o,
        $string: c,
        $escape: s,
        $each: p
    };
    r.helper = function(e, n) {
        g[e] = n
    }
    ;
    var g = r.helpers = $.$helpers;
    r.onerror = function(e) {
        var n = "Template Error\n\n";
        for (var t in e)
            n += "<" + t + ">\n" + e[t] + "\n\n";
        "object" == typeof console && console.error(n)
    }
    ;
    var d = function(e) {
        return r.onerror(e),
        function() {
            return "{Template Error}"
        }
    }
      , m = r.compile = function(e, n) {
        function r(t) {
            try {
                return new l(t,c) + ""
            } catch (r) {
                return n.debug ? d(r)() : (n.debug = !0,
                m(e, n)(t))
            }
        }
        n = n || {};
        for (var o in a)
            void 0 === n[o] && (n[o] = a[o]);
        var c = n.filename;
        try {
            var l = t(e, n)
        } catch (e) {
            return e.filename = c || "anonymous",
            e.name = "Syntax Error",
            d(e)
        }
        return r.prototype = l.prototype,
        r.toString = function() {
            return l.toString()
        }
        ,
        c && n.cache && (i[c] = r),
        r
    }
      , h = $.$each
      , v = "break,case,catch,continue,debugger,default,delete,do,else,false,finally,for,function,if,in,instanceof,new,null,return,switch,this,throw,true,try,typeof,var,void,while,with,abstract,boolean,byte,char,class,const,double,enum,export,extends,final,float,goto,implements,import,int,interface,long,native,package,private,protected,public,short,static,super,synchronized,throws,transient,volatile,arguments,let,yield,undefined"
      , y = /\/\*[\w\W]*?\*\/|\/\/[^\n]*\n|\/\/[^\n]*$|"(?:[^"\\]|\\[\w\W])*"|'(?:[^'\\]|\\[\w\W])*'|\s*\.\s*[$\w\.]+/g
      , w = /[^\w$]+/g
      , b = new RegExp(["\\b" + v.replace(/,/g, "\\b|\\b") + "\\b"].join("|"),"g")
      , x = /^\d[^,]*|,\d[^,]*/g
      , T = /^,+|,+$/g
      , E = /^$|,+/;
    "function" == typeof define ? define(function() {
        return r
    }) : "undefined" != typeof exports ? module.exports = r : this.template = r
}();