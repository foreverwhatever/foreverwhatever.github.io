---
config_dir: /Users/tonyfast/.jupyter
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.5.3
metadata:
  modified_date: July 20, 2017
  name: 2017-07-20-Spinning-Pie
  path: whatever
output_extension: .md
output_files_dir: 2017-07-20-Spinning-Pie_files
unique_key: 2017-07-20-Spinning-Pie

---

Experiments with pie charts and CustomJsTransform


<div class="output_html rendered_html output_subarea ">

    <div class="bk-root">
        <a href="http://bokeh.pydata.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
        <span id="148730cd-a82b-4ed8-8ab1-f09d18c34159">Loading BokehJS ...</span>
    </div>
</div>



<div id="5bf66edd-f758-4f34-a29a-08eee8f15a9d"></div>
<div class="output_subarea output_javascript ">
<script type="text/javascript">
var element = $('#5bf66edd-f758-4f34-a29a-08eee8f15a9d');

(function(global) {
  function now() {
    return new Date();
  }

  var force = true;

  if (typeof (window._bokeh_onload_callbacks) === "undefined" || force === true) {
    window._bokeh_onload_callbacks = [];
    window._bokeh_is_loading = undefined;
  }


  
  if (typeof (window._bokeh_timeout) === "undefined" || force === true) {
    window._bokeh_timeout = Date.now() + 5000;
    window._bokeh_failed_load = false;
  }

  var NB_LOAD_WARNING = {'data': {'text/html':
     "<div style='background-color: #fdd'>\n"+
     "<p>\n"+
     "BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \n"+
     "may be due to a slow or bad network connection. Possible fixes:\n"+
     "</p>\n"+
     "<ul>\n"+
     "<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\n"+
     "<li>use INLINE resources instead, as so:</li>\n"+
     "</ul>\n"+
     "<code>\n"+
     "from bokeh.resources import INLINE\n"+
     "output_notebook(resources=INLINE)\n"+
     "</code>\n"+
     "</div>"}};

  function display_loaded() {
    if (window.Bokeh !== undefined) {
      var el = document.getElementById("148730cd-a82b-4ed8-8ab1-f09d18c34159");
      el.textContent = "BokehJS " + Bokeh.version + " successfully loaded.";
    } else if (Date.now() < window._bokeh_timeout) {
      setTimeout(display_loaded, 100)
    }
  }

  function run_callbacks() {
    window._bokeh_onload_callbacks.forEach(function(callback) { callback() });
    delete window._bokeh_onload_callbacks
    console.info("Bokeh: all callbacks have finished");
  }

  function load_libs(js_urls, callback) {
    window._bokeh_onload_callbacks.push(callback);
    if (window._bokeh_is_loading > 0) {
      console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
      return null;
    }
    if (js_urls == null || js_urls.length === 0) {
      run_callbacks();
      return null;
    }
    console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
    window._bokeh_is_loading = js_urls.length;
    for (var i = 0; i < js_urls.length; i++) {
      var url = js_urls[i];
      var s = document.createElement('script');
      s.src = url;
      s.async = false;
      s.onreadystatechange = s.onload = function() {
        window._bokeh_is_loading--;
        if (window._bokeh_is_loading === 0) {
          console.log("Bokeh: all BokehJS libraries loaded");
          run_callbacks()
        }
      };
      s.onerror = function() {
        console.warn("failed to load library " + url);
      };
      console.log("Bokeh: injecting script tag for BokehJS library: ", url);
      document.getElementsByTagName("head")[0].appendChild(s);
    }
  };var element = document.getElementById("148730cd-a82b-4ed8-8ab1-f09d18c34159");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid '148730cd-a82b-4ed8-8ab1-f09d18c34159' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ["https://cdn.pydata.org/bokeh/release/bokeh-0.12.5.min.js", "https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.5.min.js"];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      
    },
    
    function(Bokeh) {
      
      document.getElementById("148730cd-a82b-4ed8-8ab1-f09d18c34159").textContent = "BokehJS is loading...";
    },
    function(Bokeh) {
      console.log("Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-0.12.5.min.css");
      Bokeh.embed.inject_css("https://cdn.pydata.org/bokeh/release/bokeh-0.12.5.min.css");
      console.log("Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.5.min.css");
      Bokeh.embed.inject_css("https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.5.min.css");
    }
  ];

  function run_inline_js() {
    
    if ((window.Bokeh !== undefined) || (force === true)) {
      for (var i = 0; i < inline_js.length; i++) {
        inline_js[i](window.Bokeh);
      }if (force === true) {
        display_loaded();
      }} else if (Date.now() < window._bokeh_timeout) {
      setTimeout(run_inline_js, 100);
    } else if (!window._bokeh_failed_load) {
      console.log("Bokeh: BokehJS failed to load within specified timeout.");
      window._bokeh_failed_load = true;
    } else if (force !== true) {
      var cell = $(document.getElementById("148730cd-a82b-4ed8-8ab1-f09d18c34159")).parents('.cell').data().cell;
      cell.output_area.append_execute_result(NB_LOAD_WARNING)
    }

  }

  if (window._bokeh_is_loading === 0) {
    console.log("Bokeh: BokehJS loaded, going straight to plotting");
    run_inline_js();
  } else {
    load_libs(js_urls, function() {
      console.log("Bokeh: BokehJS plotting callback run at", now());
      run_inline_js();
    });
  }
}(this));
</script>
</div>


<div class="output_markdown rendered_html output_subarea ">

<pre><code>source = pd.util.testing.makeDataFrame().sum().to_frame('x').abs().pipe(plotting.ColumnDataSource)</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">

<pre><code>def T(field, code="""return xs;""", **args):
    return dict(field=field, transform=models.CustomJSTransform(args=args, v_func=coffee.compile(code, bare=True)))</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">
<p>A simple exmaple using customjstransform to modify datasources with coffeescript.</p>

<pre><code>p = plotting.figure()
p.add_glyph(
    source, 
    models.AnnularWedge(
        x=0, y=T('x', """return xs.map ()-&gt; 0"""),
        end_angle=T('x', """return xs.map (v,i)-&gt; i/xs.length*2*3.14159"""),
        start_angle=T('x', """return xs.map (v,i)-&gt; (i+1)/xs.length*2*3.14159"""),
        outer_radius=T('x', """return xs.map (v)-&gt;1"""),
    )
)
plotting.show(p)</code></pre>

</div>

<div class="output_html rendered_html output_subarea ">


    <div class="bk-root">
        <div class="bk-plotdiv" id="24aea4ab-95b2-4df4-8439-cbc7959b446d"></div>
    </div>
<script type="text/javascript">
  
  (function(global) {
    function now() {
      return new Date();
    }
  
    var force = false;
  
    if (typeof (window._bokeh_onload_callbacks) === "undefined" || force === true) {
      window._bokeh_onload_callbacks = [];
      window._bokeh_is_loading = undefined;
    }
  
  
    
    if (typeof (window._bokeh_timeout) === "undefined" || force === true) {
      window._bokeh_timeout = Date.now() + 0;
      window._bokeh_failed_load = false;
    }
  
    var NB_LOAD_WARNING = {'data': {'text/html':
       "<div style='background-color: #fdd'>\n"+
       "<p>\n"+
       "BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \n"+
       "may be due to a slow or bad network connection. Possible fixes:\n"+
       "</p>\n"+
       "<ul>\n"+
       "<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\n"+
       "<li>use INLINE resources instead, as so:</li>\n"+
       "</ul>\n"+
       "<code>\n"+
       "from bokeh.resources import INLINE\n"+
       "output_notebook(resources=INLINE)\n"+
       "</code>\n"+
       "</div>"}};
  
    function display_loaded() {
      if (window.Bokeh !== undefined) {
        var el = document.getElementById("24aea4ab-95b2-4df4-8439-cbc7959b446d");
        el.textContent = "BokehJS " + Bokeh.version + " successfully loaded.";
      } else if (Date.now() < window._bokeh_timeout) {
        setTimeout(display_loaded, 100)
      }
    }
  
    function run_callbacks() {
      window._bokeh_onload_callbacks.forEach(function(callback) { callback() });
      delete window._bokeh_onload_callbacks
      console.info("Bokeh: all callbacks have finished");
    }
  
    function load_libs(js_urls, callback) {
      window._bokeh_onload_callbacks.push(callback);
      if (window._bokeh_is_loading > 0) {
        console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
        return null;
      }
      if (js_urls == null || js_urls.length === 0) {
        run_callbacks();
        return null;
      }
      console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
      window._bokeh_is_loading = js_urls.length;
      for (var i = 0; i < js_urls.length; i++) {
        var url = js_urls[i];
        var s = document.createElement('script');
        s.src = url;
        s.async = false;
        s.onreadystatechange = s.onload = function() {
          window._bokeh_is_loading--;
          if (window._bokeh_is_loading === 0) {
            console.log("Bokeh: all BokehJS libraries loaded");
            run_callbacks()
          }
        };
        s.onerror = function() {
          console.warn("failed to load library " + url);
        };
        console.log("Bokeh: injecting script tag for BokehJS library: ", url);
        document.getElementsByTagName("head")[0].appendChild(s);
      }
    };var element = document.getElementById("24aea4ab-95b2-4df4-8439-cbc7959b446d");
    if (element == null) {
      console.log("Bokeh: ERROR: autoload.js configured with elementid '24aea4ab-95b2-4df4-8439-cbc7959b446d' but no matching script tag was found. ")
      return false;
    }
  
    var js_urls = [];
  
    var inline_js = [
      function(Bokeh) {
        (function() {
          var fn = function() {
            var docs_json = {"59d283a5-8dee-407e-89cd-abf2941518e5":{"roots":{"references":[{"attributes":{"formatter":{"id":"9a0f71c0-5cee-4e9d-a4cd-244e9e4e3537","type":"BasicTickFormatter"},"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"},"ticker":{"id":"fede1073-7f2a-4577-b811-c859b4544748","type":"BasicTicker"}},"id":"de329a51-093f-4226-951e-30334680ada1","type":"LinearAxis"},{"attributes":{"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"}},"id":"dbdbe08d-a7a4-40f2-bb76-0b4b99b89ca5","type":"ResetTool"},{"attributes":{"plot":null,"text":""},"id":"a59bbff8-3c41-41a0-a3b5-4bbf148f9a18","type":"Title"},{"attributes":{"formatter":{"id":"76ccf9a1-a3b8-4ee2-b459-3bdd3b7bb0cd","type":"BasicTickFormatter"},"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"},"ticker":{"id":"c108ccb1-d16c-4951-a50d-e18b417aa0e9","type":"BasicTicker"}},"id":"936c81a5-8cd0-4e66-b659-8f04fb30278c","type":"LinearAxis"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function() {\n  return 0;\n});\n"},"id":"b1025dba-4acc-4d5d-8471-a47ab6c459e7","type":"CustomJSTransform"},{"attributes":{"overlay":{"id":"92c44068-b4a1-4882-b3c0-04e701fdafaf","type":"BoxAnnotation"},"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"}},"id":"b343dd8b-6371-4115-8bcf-36941f1d6308","type":"BoxZoomTool"},{"attributes":{"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"},"ticker":{"id":"c108ccb1-d16c-4951-a50d-e18b417aa0e9","type":"BasicTicker"}},"id":"6020079a-3bdd-48f7-ace3-33f9d4595c99","type":"Grid"},{"attributes":{},"id":"76ccf9a1-a3b8-4ee2-b459-3bdd3b7bb0cd","type":"BasicTickFormatter"},{"attributes":{"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"}},"id":"24e63a5f-09e4-4457-865d-82f257ccc27d","type":"HelpTool"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function(v, i) {\n  return i / xs.length * 2 * 3.14159;\n});\n"},"id":"583f3610-0ee4-4f84-927e-9477f013b5bc","type":"CustomJSTransform"},{"attributes":{"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"}},"id":"b0db882b-484a-4fe8-b722-f4c6f1db47cc","type":"WheelZoomTool"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function(v) {\n  return 1;\n});\n"},"id":"3010075e-8c2d-4fde-9c6c-598c392d876e","type":"CustomJSTransform"},{"attributes":{"callback":null},"id":"dfb08da9-5b67-4bc1-a2f5-bbd8d9c41352","type":"DataRange1d"},{"attributes":{"end_angle":{"field":"x","transform":{"id":"583f3610-0ee4-4f84-927e-9477f013b5bc","type":"CustomJSTransform"},"units":"rad"},"outer_radius":{"field":"x","transform":{"id":"3010075e-8c2d-4fde-9c6c-598c392d876e","type":"CustomJSTransform"},"units":"data"},"start_angle":{"field":"x","transform":{"id":"0129e98a-67a5-4cb5-91d2-4f3e07756ee3","type":"CustomJSTransform"},"units":"rad"},"x":{"value":0},"y":{"field":"x","transform":{"id":"b1025dba-4acc-4d5d-8471-a47ab6c459e7","type":"CustomJSTransform"}}},"id":"a267b10f-c137-46a8-8892-6ea2c9620186","type":"AnnularWedge"},{"attributes":{},"id":"63f2da54-79b0-4b48-af8c-8c93d1d87cfc","type":"ToolEvents"},{"attributes":{"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"}},"id":"de583ec1-0592-425a-9cbb-d84d518a4060","type":"PanTool"},{"attributes":{"callback":null,"column_names":["index","x"],"data":{"index":["A","B","C","D"],"x":{"__ndarray__":"CZvmXcQ/G0B2K7Sdw3/TP+C/BCg/HwZAaN4gO4D3IEA=","dtype":"float64","shape":[4]}}},"id":"22d3e580-7e4d-4748-8013-f9bcd750130f","type":"ColumnDataSource"},{"attributes":{},"id":"fede1073-7f2a-4577-b811-c859b4544748","type":"BasicTicker"},{"attributes":{"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"}},"id":"5055e67d-1763-4648-9273-8f5eeace8eef","type":"SaveTool"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"de583ec1-0592-425a-9cbb-d84d518a4060","type":"PanTool"},{"id":"b0db882b-484a-4fe8-b722-f4c6f1db47cc","type":"WheelZoomTool"},{"id":"b343dd8b-6371-4115-8bcf-36941f1d6308","type":"BoxZoomTool"},{"id":"5055e67d-1763-4648-9273-8f5eeace8eef","type":"SaveTool"},{"id":"dbdbe08d-a7a4-40f2-bb76-0b4b99b89ca5","type":"ResetTool"},{"id":"24e63a5f-09e4-4457-865d-82f257ccc27d","type":"HelpTool"}]},"id":"2bf00162-96d5-4f0b-8877-1356c6e5792c","type":"Toolbar"},{"attributes":{},"id":"c108ccb1-d16c-4951-a50d-e18b417aa0e9","type":"BasicTicker"},{"attributes":{"below":[{"id":"936c81a5-8cd0-4e66-b659-8f04fb30278c","type":"LinearAxis"}],"left":[{"id":"de329a51-093f-4226-951e-30334680ada1","type":"LinearAxis"}],"renderers":[{"id":"936c81a5-8cd0-4e66-b659-8f04fb30278c","type":"LinearAxis"},{"id":"6020079a-3bdd-48f7-ace3-33f9d4595c99","type":"Grid"},{"id":"de329a51-093f-4226-951e-30334680ada1","type":"LinearAxis"},{"id":"5f17b369-6f66-41f1-b2b1-3c9f8e551ebc","type":"Grid"},{"id":"92c44068-b4a1-4882-b3c0-04e701fdafaf","type":"BoxAnnotation"},{"id":"c416e616-01f2-4d30-9fcc-a3e65bd82dfb","type":"GlyphRenderer"}],"title":{"id":"a59bbff8-3c41-41a0-a3b5-4bbf148f9a18","type":"Title"},"tool_events":{"id":"63f2da54-79b0-4b48-af8c-8c93d1d87cfc","type":"ToolEvents"},"toolbar":{"id":"2bf00162-96d5-4f0b-8877-1356c6e5792c","type":"Toolbar"},"x_range":{"id":"dfb08da9-5b67-4bc1-a2f5-bbd8d9c41352","type":"DataRange1d"},"y_range":{"id":"97fb58f3-d29e-46d2-a54a-3d99344160d7","type":"DataRange1d"}},"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"},{"attributes":{"callback":null},"id":"97fb58f3-d29e-46d2-a54a-3d99344160d7","type":"DataRange1d"},{"attributes":{"data_source":{"id":"22d3e580-7e4d-4748-8013-f9bcd750130f","type":"ColumnDataSource"},"glyph":{"id":"a267b10f-c137-46a8-8892-6ea2c9620186","type":"AnnularWedge"},"hover_glyph":null,"muted_glyph":null},"id":"c416e616-01f2-4d30-9fcc-a3e65bd82dfb","type":"GlyphRenderer"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function(v, i) {\n  return (i + 1) / xs.length * 2 * 3.14159;\n});\n"},"id":"0129e98a-67a5-4cb5-91d2-4f3e07756ee3","type":"CustomJSTransform"},{"attributes":{"dimension":1,"plot":{"id":"9cd411b6-7096-4a05-ad1d-15c951907262","subtype":"Figure","type":"Plot"},"ticker":{"id":"fede1073-7f2a-4577-b811-c859b4544748","type":"BasicTicker"}},"id":"5f17b369-6f66-41f1-b2b1-3c9f8e551ebc","type":"Grid"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"92c44068-b4a1-4882-b3c0-04e701fdafaf","type":"BoxAnnotation"},{"attributes":{},"id":"9a0f71c0-5cee-4e9d-a4cd-244e9e4e3537","type":"BasicTickFormatter"}],"root_ids":["9cd411b6-7096-4a05-ad1d-15c951907262"]},"title":"Bokeh Application","version":"0.12.5"}};
            var render_items = [{"docid":"59d283a5-8dee-407e-89cd-abf2941518e5","elementid":"24aea4ab-95b2-4df4-8439-cbc7959b446d","modelid":"9cd411b6-7096-4a05-ad1d-15c951907262"}];
            
            Bokeh.embed.embed_items(docs_json, render_items);
          };
          if (document.readyState != "loading") fn();
          else document.addEventListener("DOMContentLoaded", fn);
        })();
      },
      function(Bokeh) {
      }
    ];
  
    function run_inline_js() {
      
      if ((window.Bokeh !== undefined) || (force === true)) {
        for (var i = 0; i < inline_js.length; i++) {
          inline_js[i](window.Bokeh);
        }if (force === true) {
          display_loaded();
        }} else if (Date.now() < window._bokeh_timeout) {
        setTimeout(run_inline_js, 100);
      } else if (!window._bokeh_failed_load) {
        console.log("Bokeh: BokehJS failed to load within specified timeout.");
        window._bokeh_failed_load = true;
      } else if (force !== true) {
        var cell = $(document.getElementById("24aea4ab-95b2-4df4-8439-cbc7959b446d")).parents('.cell').data().cell;
        cell.output_area.append_execute_result(NB_LOAD_WARNING)
      }
  
    }
  
    if (window._bokeh_is_loading === 0) {
      console.log("Bokeh: BokehJS loaded, going straight to plotting");
      run_inline_js();
    } else {
      load_libs(js_urls, function() {
        console.log("Bokeh: BokehJS plotting callback run at", now());
        run_inline_js();
      });
    }
  }(this));
</script>
</div>


<div class="output_markdown rendered_html output_subarea ">
<p>Pie charts suck.  They are biased.  But if they didn't have an orientation they would suck less.</p>

<pre><code>p = plotting.figure()
r = p.add_glyph(
    source, 
    models.AnnularWedge(
        x=0, y=T('x', """return xs.map ()-&gt; 0"""),
        end_angle=T('x', """
        dx = Math.max 1, Math.abs(xx.start-xx.end)/2/1.5
        total = xs.reduce (p,n)-&gt;p+n
        current = ((Math.log Math.abs(xx.start-xx.end)/10)%1)*dx*2*3.14159            
        return xs.map (v, i)-&gt; 
            if i &gt; 0
                current += xs[i-1]/total*2*3.14159
            current
        """, xx=p.x_range),
        start_angle=T('x', """
        dx = Math.max 1, Math.abs(xx.start-xx.end)/2/1.5
        total = xs.reduce (p,n)-&gt;p+n
        current = ((Math.log Math.abs(xx.start-xx.end)/10)%1)*dx*2*3.14159
        return xs.map (v, i)-&gt; 
            current += v/total*2*3.14159 
            current
        """, xx=p.x_range),
        outer_radius=T('x', """
        dx = Math.max 1, Math.abs(xx.start-xx.end)/2/1.5
        return xs.map (v)-&gt; dx
        """, xx=p.x_range),
        inner_radius=T('x', """
        dx = .1*Math.max 1, Math.abs(xx.start-xx.end)/2/1.5
        return xs.map (v)-&gt; dx
        """, xx=p.x_range),
        fill_alpha=.6
    )
)
p.x_range.callback = p.y_range.callback = models.CustomJS(args=dict(source=source), code="""
source.trigger('change');
dx = Math.abs(cb_obj.start - cb_obj.end)/2
cb_obj.start = dx
cb_obj.end = -dx
""")
plotting.show(p)

</code></pre>
<p>This pie chart doesn't suck if you enable wheel zoom.</p>

</div>

<div class="output_html rendered_html output_subarea ">


    <div class="bk-root">
        <div class="bk-plotdiv" id="314e2ffc-8fb3-4542-bd05-fe24e7e27278"></div>
    </div>
<script type="text/javascript">
  
  (function(global) {
    function now() {
      return new Date();
    }
  
    var force = false;
  
    if (typeof (window._bokeh_onload_callbacks) === "undefined" || force === true) {
      window._bokeh_onload_callbacks = [];
      window._bokeh_is_loading = undefined;
    }
  
  
    
    if (typeof (window._bokeh_timeout) === "undefined" || force === true) {
      window._bokeh_timeout = Date.now() + 0;
      window._bokeh_failed_load = false;
    }
  
    var NB_LOAD_WARNING = {'data': {'text/html':
       "<div style='background-color: #fdd'>\n"+
       "<p>\n"+
       "BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \n"+
       "may be due to a slow or bad network connection. Possible fixes:\n"+
       "</p>\n"+
       "<ul>\n"+
       "<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\n"+
       "<li>use INLINE resources instead, as so:</li>\n"+
       "</ul>\n"+
       "<code>\n"+
       "from bokeh.resources import INLINE\n"+
       "output_notebook(resources=INLINE)\n"+
       "</code>\n"+
       "</div>"}};
  
    function display_loaded() {
      if (window.Bokeh !== undefined) {
        var el = document.getElementById("314e2ffc-8fb3-4542-bd05-fe24e7e27278");
        el.textContent = "BokehJS " + Bokeh.version + " successfully loaded.";
      } else if (Date.now() < window._bokeh_timeout) {
        setTimeout(display_loaded, 100)
      }
    }
  
    function run_callbacks() {
      window._bokeh_onload_callbacks.forEach(function(callback) { callback() });
      delete window._bokeh_onload_callbacks
      console.info("Bokeh: all callbacks have finished");
    }
  
    function load_libs(js_urls, callback) {
      window._bokeh_onload_callbacks.push(callback);
      if (window._bokeh_is_loading > 0) {
        console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
        return null;
      }
      if (js_urls == null || js_urls.length === 0) {
        run_callbacks();
        return null;
      }
      console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
      window._bokeh_is_loading = js_urls.length;
      for (var i = 0; i < js_urls.length; i++) {
        var url = js_urls[i];
        var s = document.createElement('script');
        s.src = url;
        s.async = false;
        s.onreadystatechange = s.onload = function() {
          window._bokeh_is_loading--;
          if (window._bokeh_is_loading === 0) {
            console.log("Bokeh: all BokehJS libraries loaded");
            run_callbacks()
          }
        };
        s.onerror = function() {
          console.warn("failed to load library " + url);
        };
        console.log("Bokeh: injecting script tag for BokehJS library: ", url);
        document.getElementsByTagName("head")[0].appendChild(s);
      }
    };var element = document.getElementById("314e2ffc-8fb3-4542-bd05-fe24e7e27278");
    if (element == null) {
      console.log("Bokeh: ERROR: autoload.js configured with elementid '314e2ffc-8fb3-4542-bd05-fe24e7e27278' but no matching script tag was found. ")
      return false;
    }
  
    var js_urls = [];
  
    var inline_js = [
      function(Bokeh) {
        (function() {
          var fn = function() {
            var docs_json = {"84ff5251-32b6-4977-986d-dab4e81c9221":{"roots":{"references":[{"attributes":{"callback":{"id":"d3603b53-4516-4f67-b12e-fc14a475bdd5","type":"CustomJS"}},"id":"15a69148-3817-417b-a608-212a9edb408f","type":"DataRange1d"},{"attributes":{"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"},"ticker":{"id":"e5cac4d4-269b-44c3-83b9-7e576ee53ebd","type":"BasicTicker"}},"id":"38701d76-ae17-4e7a-9dad-6f559598324c","type":"Grid"},{"attributes":{"below":[{"id":"92e5c49e-ee26-4e33-9433-768fc654dd03","type":"LinearAxis"}],"left":[{"id":"17d1df54-27c0-474d-9ef1-85885ed25223","type":"LinearAxis"}],"renderers":[{"id":"92e5c49e-ee26-4e33-9433-768fc654dd03","type":"LinearAxis"},{"id":"38701d76-ae17-4e7a-9dad-6f559598324c","type":"Grid"},{"id":"17d1df54-27c0-474d-9ef1-85885ed25223","type":"LinearAxis"},{"id":"ef074eb8-88f7-47fa-a275-df9eb4b8e9d7","type":"Grid"},{"id":"cfa58219-3427-45f6-90bf-5d1b76b5f324","type":"BoxAnnotation"},{"id":"ab6edc96-7946-4478-b352-333c0440978c","type":"GlyphRenderer"}],"title":{"id":"5ee09e98-7865-48a5-bc50-226271dbf412","type":"Title"},"tool_events":{"id":"ba0ea57b-1266-48e8-b774-9948f7eb24f7","type":"ToolEvents"},"toolbar":{"id":"c81e1116-ded5-421c-8476-2af5cd9af5c6","type":"Toolbar"},"x_range":{"id":"15a69148-3817-417b-a608-212a9edb408f","type":"DataRange1d"},"y_range":{"id":"7896b6b6-de61-4600-aac8-a4286d5a629b","type":"DataRange1d"}},"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"},{"attributes":{"overlay":{"id":"cfa58219-3427-45f6-90bf-5d1b76b5f324","type":"BoxAnnotation"},"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"}},"id":"906cb8bb-b7f0-46d9-a205-cbcdfd0086fb","type":"BoxZoomTool"},{"attributes":{"plot":null,"text":""},"id":"5ee09e98-7865-48a5-bc50-226271dbf412","type":"Title"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function() {\n  return 0;\n});\n"},"id":"397cff7b-f284-44f1-9e8c-cf1b84155b56","type":"CustomJSTransform"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"90d123e7-676d-40a6-ad02-31207c3e1246","type":"PanTool"},{"id":"7d22b637-424b-4bce-9d7e-071dee7523f2","type":"WheelZoomTool"},{"id":"906cb8bb-b7f0-46d9-a205-cbcdfd0086fb","type":"BoxZoomTool"},{"id":"c32e837e-af0e-4655-8eaf-90840c8dd842","type":"SaveTool"},{"id":"ccb9f06c-39ee-4373-a5ae-7118fa1a4078","type":"ResetTool"},{"id":"a60b478e-607f-46e7-a9e4-23a441048164","type":"HelpTool"}]},"id":"c81e1116-ded5-421c-8476-2af5cd9af5c6","type":"Toolbar"},{"attributes":{"callback":null,"column_names":["index","x"],"data":{"index":["A","B","C","D"],"x":{"__ndarray__":"CZvmXcQ/G0B2K7Sdw3/TP+C/BCg/HwZAaN4gO4D3IEA=","dtype":"float64","shape":[4]}}},"id":"22d3e580-7e4d-4748-8013-f9bcd750130f","type":"ColumnDataSource"},{"attributes":{"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"}},"id":"7d22b637-424b-4bce-9d7e-071dee7523f2","type":"WheelZoomTool"},{"attributes":{"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"}},"id":"a60b478e-607f-46e7-a9e4-23a441048164","type":"HelpTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"cfa58219-3427-45f6-90bf-5d1b76b5f324","type":"BoxAnnotation"},{"attributes":{},"id":"a66078b6-8201-4049-ac80-f6e10be88d24","type":"BasicTickFormatter"},{"attributes":{"formatter":{"id":"a66078b6-8201-4049-ac80-f6e10be88d24","type":"BasicTickFormatter"},"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"},"ticker":{"id":"e5cac4d4-269b-44c3-83b9-7e576ee53ebd","type":"BasicTicker"}},"id":"92e5c49e-ee26-4e33-9433-768fc654dd03","type":"LinearAxis"},{"attributes":{"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"}},"id":"ccb9f06c-39ee-4373-a5ae-7118fa1a4078","type":"ResetTool"},{"attributes":{},"id":"ba0ea57b-1266-48e8-b774-9948f7eb24f7","type":"ToolEvents"},{"attributes":{"end_angle":{"field":"x","transform":{"id":"85c7ed7e-b394-421b-b298-dd177bd98115","type":"CustomJSTransform"},"units":"rad"},"fill_alpha":{"value":0.6},"inner_radius":{"field":"x","transform":{"id":"56e1c8d6-53b5-4841-91c7-ef7abc4c244c","type":"CustomJSTransform"},"units":"data"},"outer_radius":{"field":"x","transform":{"id":"59a8423e-cbce-4d7c-960f-509397bd5277","type":"CustomJSTransform"},"units":"data"},"start_angle":{"field":"x","transform":{"id":"4fc1679e-fdce-41ab-8d71-839c26fb7135","type":"CustomJSTransform"},"units":"rad"},"x":{"value":0},"y":{"field":"x","transform":{"id":"397cff7b-f284-44f1-9e8c-cf1b84155b56","type":"CustomJSTransform"}}},"id":"1f50d375-2b33-4e61-b9f9-4b050b6379d3","type":"AnnularWedge"},{"attributes":{"data_source":{"id":"22d3e580-7e4d-4748-8013-f9bcd750130f","type":"ColumnDataSource"},"glyph":{"id":"1f50d375-2b33-4e61-b9f9-4b050b6379d3","type":"AnnularWedge"},"hover_glyph":null,"muted_glyph":null},"id":"ab6edc96-7946-4478-b352-333c0440978c","type":"GlyphRenderer"},{"attributes":{"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"}},"id":"90d123e7-676d-40a6-ad02-31207c3e1246","type":"PanTool"},{"attributes":{"args":{"xx":{"id":"15a69148-3817-417b-a608-212a9edb408f","type":"DataRange1d"}},"v_func":"// Generated by CoffeeScript 1.11.1\nvar dx;\n\ndx = Math.max(1, Math.abs(xx.start - xx.end) / 2 / 1.5);\n\nreturn xs.map(function(v) {\n  return dx;\n});\n"},"id":"59a8423e-cbce-4d7c-960f-509397bd5277","type":"CustomJSTransform"},{"attributes":{},"id":"e5cac4d4-269b-44c3-83b9-7e576ee53ebd","type":"BasicTicker"},{"attributes":{"formatter":{"id":"0522f32e-bbbc-440a-b754-fe348d3f3198","type":"BasicTickFormatter"},"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"},"ticker":{"id":"a26076a9-7bbc-4cb9-b6f8-9d99c838d6ea","type":"BasicTicker"}},"id":"17d1df54-27c0-474d-9ef1-85885ed25223","type":"LinearAxis"},{"attributes":{"args":{"source":{"id":"22d3e580-7e4d-4748-8013-f9bcd750130f","type":"ColumnDataSource"}},"code":"\nsource.trigger('change');\ndx = Math.abs(cb_obj.start - cb_obj.end)/2\ncb_obj.start = dx\ncb_obj.end = -dx\n"},"id":"d3603b53-4516-4f67-b12e-fc14a475bdd5","type":"CustomJS"},{"attributes":{},"id":"0522f32e-bbbc-440a-b754-fe348d3f3198","type":"BasicTickFormatter"},{"attributes":{"args":{"xx":{"id":"15a69148-3817-417b-a608-212a9edb408f","type":"DataRange1d"}},"v_func":"// Generated by CoffeeScript 1.11.1\nvar current, dx, total;\n\ndx = Math.max(1, Math.abs(xx.start - xx.end) / 2 / 1.5);\n\ntotal = xs.reduce(function(p, n) {\n  return p + n;\n});\n\ncurrent = ((Math.log(Math.abs(xx.start - xx.end) / 10)) % 1) * dx * 2 * 3.14159;\n\nreturn xs.map(function(v, i) {\n  current += v / total * 2 * 3.14159;\n  return current;\n});\n"},"id":"4fc1679e-fdce-41ab-8d71-839c26fb7135","type":"CustomJSTransform"},{"attributes":{"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"}},"id":"c32e837e-af0e-4655-8eaf-90840c8dd842","type":"SaveTool"},{"attributes":{"dimension":1,"plot":{"id":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d","subtype":"Figure","type":"Plot"},"ticker":{"id":"a26076a9-7bbc-4cb9-b6f8-9d99c838d6ea","type":"BasicTicker"}},"id":"ef074eb8-88f7-47fa-a275-df9eb4b8e9d7","type":"Grid"},{"attributes":{"callback":{"id":"d3603b53-4516-4f67-b12e-fc14a475bdd5","type":"CustomJS"}},"id":"7896b6b6-de61-4600-aac8-a4286d5a629b","type":"DataRange1d"},{"attributes":{},"id":"a26076a9-7bbc-4cb9-b6f8-9d99c838d6ea","type":"BasicTicker"},{"attributes":{"args":{"xx":{"id":"15a69148-3817-417b-a608-212a9edb408f","type":"DataRange1d"}},"v_func":"// Generated by CoffeeScript 1.11.1\nvar dx;\n\ndx = .1 * Math.max(1, Math.abs(xx.start - xx.end) / 2 / 1.5);\n\nreturn xs.map(function(v) {\n  return dx;\n});\n"},"id":"56e1c8d6-53b5-4841-91c7-ef7abc4c244c","type":"CustomJSTransform"},{"attributes":{"args":{"xx":{"id":"15a69148-3817-417b-a608-212a9edb408f","type":"DataRange1d"}},"v_func":"// Generated by CoffeeScript 1.11.1\nvar current, dx, total;\n\ndx = Math.max(1, Math.abs(xx.start - xx.end) / 2 / 1.5);\n\ntotal = xs.reduce(function(p, n) {\n  return p + n;\n});\n\ncurrent = ((Math.log(Math.abs(xx.start - xx.end) / 10)) % 1) * dx * 2 * 3.14159;\n\nreturn xs.map(function(v, i) {\n  if (i > 0) {\n    current += xs[i - 1] / total * 2 * 3.14159;\n  }\n  return current;\n});\n"},"id":"85c7ed7e-b394-421b-b298-dd177bd98115","type":"CustomJSTransform"}],"root_ids":["4c3a1e90-f2f8-45c9-9187-6a957c12bc2d"]},"title":"Bokeh Application","version":"0.12.5"}};
            var render_items = [{"docid":"84ff5251-32b6-4977-986d-dab4e81c9221","elementid":"314e2ffc-8fb3-4542-bd05-fe24e7e27278","modelid":"4c3a1e90-f2f8-45c9-9187-6a957c12bc2d"}];
            
            Bokeh.embed.embed_items(docs_json, render_items);
          };
          if (document.readyState != "loading") fn();
          else document.addEventListener("DOMContentLoaded", fn);
        })();
      },
      function(Bokeh) {
      }
    ];
  
    function run_inline_js() {
      
      if ((window.Bokeh !== undefined) || (force === true)) {
        for (var i = 0; i < inline_js.length; i++) {
          inline_js[i](window.Bokeh);
        }if (force === true) {
          display_loaded();
        }} else if (Date.now() < window._bokeh_timeout) {
        setTimeout(run_inline_js, 100);
      } else if (!window._bokeh_failed_load) {
        console.log("Bokeh: BokehJS failed to load within specified timeout.");
        window._bokeh_failed_load = true;
      } else if (force !== true) {
        var cell = $(document.getElementById("314e2ffc-8fb3-4542-bd05-fe24e7e27278")).parents('.cell').data().cell;
        cell.output_area.append_execute_result(NB_LOAD_WARNING)
      }
  
    }
  
    if (window._bokeh_is_loading === 0) {
      console.log("Bokeh: BokehJS loaded, going straight to plotting");
      run_inline_js();
    } else {
      load_libs(js_urls, function() {
        console.log("Bokeh: BokehJS plotting callback run at", now());
        run_inline_js();
      });
    }
  }(this));
</script>
</div>


