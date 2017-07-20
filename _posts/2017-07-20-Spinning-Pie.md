---
config_dir: /home/travis/.jupyter
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
        <span id="460ea793-3dbd-4936-9c23-7c91b2f9c10c">Loading BokehJS ...</span>
    </div>
</div>



<div id="61a190ae-4421-4e22-94a1-8d55db2e8331"></div>
<div class="output_subarea output_javascript ">
<script type="text/javascript">
var element = $('#61a190ae-4421-4e22-94a1-8d55db2e8331');

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
      var el = document.getElementById("460ea793-3dbd-4936-9c23-7c91b2f9c10c");
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
  };var element = document.getElementById("460ea793-3dbd-4936-9c23-7c91b2f9c10c");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid '460ea793-3dbd-4936-9c23-7c91b2f9c10c' but no matching script tag was found. ")
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
      
      document.getElementById("460ea793-3dbd-4936-9c23-7c91b2f9c10c").textContent = "BokehJS is loading...";
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
      var cell = $(document.getElementById("460ea793-3dbd-4936-9c23-7c91b2f9c10c")).parents('.cell').data().cell;
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




<div class="output_html rendered_html output_subarea ">


    <div class="bk-root">
        <div class="bk-plotdiv" id="47bb13ba-e6f0-4314-a098-e25e76841a94"></div>
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
        var el = document.getElementById("47bb13ba-e6f0-4314-a098-e25e76841a94");
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
    };var element = document.getElementById("47bb13ba-e6f0-4314-a098-e25e76841a94");
    if (element == null) {
      console.log("Bokeh: ERROR: autoload.js configured with elementid '47bb13ba-e6f0-4314-a098-e25e76841a94' but no matching script tag was found. ")
      return false;
    }
  
    var js_urls = [];
  
    var inline_js = [
      function(Bokeh) {
        (function() {
          var fn = function() {
            var docs_json = {"60c4e47d-aad2-4fbb-b6e4-96dec2e85b70":{"roots":{"references":[{"attributes":{"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"}},"id":"ceee7811-e29d-4096-834e-bea2c17bd56f","type":"HelpTool"},{"attributes":{"plot":null,"text":""},"id":"56ffc562-c710-4a4d-99a0-e0929b547723","type":"Title"},{"attributes":{"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"}},"id":"bb2e2fb0-c82d-4e3b-9795-f37e38a89474","type":"ResetTool"},{"attributes":{},"id":"03590ba5-d567-417a-b91f-22630537c836","type":"BasicTicker"},{"attributes":{"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"}},"id":"4368ccb2-239d-48f3-aedc-b1e5cc1451e0","type":"PanTool"},{"attributes":{"data_source":{"id":"e97b63bd-7349-4650-b296-c074182cd0dc","type":"ColumnDataSource"},"glyph":{"id":"27eba54b-3844-4333-a240-6a9299afb7b2","type":"AnnularWedge"},"hover_glyph":null,"muted_glyph":null},"id":"dfe35c6a-96f3-460a-9cc3-baf3b29ed11c","type":"GlyphRenderer"},{"attributes":{},"id":"ce14dd4a-b623-43a5-9069-727ac3c5df9d","type":"BasicTickFormatter"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function(v) {\n  return 1;\n});\n"},"id":"2fe29a92-6bd6-4264-9fe2-ff407686a1ae","type":"CustomJSTransform"},{"attributes":{"callback":null},"id":"d66e32f2-9e8a-423d-b68c-0c6b669cfd8c","type":"DataRange1d"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"4368ccb2-239d-48f3-aedc-b1e5cc1451e0","type":"PanTool"},{"id":"5b570e0c-2917-42d8-93f7-676980c490af","type":"WheelZoomTool"},{"id":"202ec56b-45d4-49f7-80af-af9f06f91704","type":"BoxZoomTool"},{"id":"c16c21e5-9387-46da-ac03-703d2557fc8d","type":"SaveTool"},{"id":"bb2e2fb0-c82d-4e3b-9795-f37e38a89474","type":"ResetTool"},{"id":"ceee7811-e29d-4096-834e-bea2c17bd56f","type":"HelpTool"}]},"id":"5f3fb131-e855-42dd-8bb2-39f8366fe3cf","type":"Toolbar"},{"attributes":{"end_angle":{"field":"x","transform":{"id":"3756673d-8308-4c42-909a-db85daee4232","type":"CustomJSTransform"},"units":"rad"},"outer_radius":{"field":"x","transform":{"id":"2fe29a92-6bd6-4264-9fe2-ff407686a1ae","type":"CustomJSTransform"},"units":"data"},"start_angle":{"field":"x","transform":{"id":"caec11d8-861d-458a-981f-25cc7a624e65","type":"CustomJSTransform"},"units":"rad"},"x":{"value":0},"y":{"field":"x","transform":{"id":"40745b6e-fe0c-4a56-8272-872158899b98","type":"CustomJSTransform"}}},"id":"27eba54b-3844-4333-a240-6a9299afb7b2","type":"AnnularWedge"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"7d08b007-786b-4cea-8f13-4a120d4e588a","type":"BoxAnnotation"},{"attributes":{"overlay":{"id":"7d08b007-786b-4cea-8f13-4a120d4e588a","type":"BoxAnnotation"},"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"}},"id":"202ec56b-45d4-49f7-80af-af9f06f91704","type":"BoxZoomTool"},{"attributes":{},"id":"744b3d69-ddca-4d11-ab9d-715ee269092e","type":"BasicTicker"},{"attributes":{"callback":null,"column_names":["x","index"],"data":{"index":["A","B","C","D"],"x":{"__ndarray__":"4p3C2aoID0AXcUASePkgQLh8EwxbXqI/SI5QdjnqF0A=","dtype":"float64","shape":[4]}}},"id":"e97b63bd-7349-4650-b296-c074182cd0dc","type":"ColumnDataSource"},{"attributes":{"dimension":1,"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"},"ticker":{"id":"744b3d69-ddca-4d11-ab9d-715ee269092e","type":"BasicTicker"}},"id":"9e91300a-1567-4f89-a546-00da5caf59ee","type":"Grid"},{"attributes":{"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"},"ticker":{"id":"03590ba5-d567-417a-b91f-22630537c836","type":"BasicTicker"}},"id":"9eae3f8e-5618-468a-8e88-e3c611cd2973","type":"Grid"},{"attributes":{"formatter":{"id":"ce14dd4a-b623-43a5-9069-727ac3c5df9d","type":"BasicTickFormatter"},"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"},"ticker":{"id":"03590ba5-d567-417a-b91f-22630537c836","type":"BasicTicker"}},"id":"46ba6cf9-aab0-48d2-9e8f-12ddea8a7f2b","type":"LinearAxis"},{"attributes":{"below":[{"id":"46ba6cf9-aab0-48d2-9e8f-12ddea8a7f2b","type":"LinearAxis"}],"left":[{"id":"0d010602-1200-4404-9956-3f6a9cfa7f26","type":"LinearAxis"}],"renderers":[{"id":"46ba6cf9-aab0-48d2-9e8f-12ddea8a7f2b","type":"LinearAxis"},{"id":"9eae3f8e-5618-468a-8e88-e3c611cd2973","type":"Grid"},{"id":"0d010602-1200-4404-9956-3f6a9cfa7f26","type":"LinearAxis"},{"id":"9e91300a-1567-4f89-a546-00da5caf59ee","type":"Grid"},{"id":"7d08b007-786b-4cea-8f13-4a120d4e588a","type":"BoxAnnotation"},{"id":"dfe35c6a-96f3-460a-9cc3-baf3b29ed11c","type":"GlyphRenderer"}],"title":{"id":"56ffc562-c710-4a4d-99a0-e0929b547723","type":"Title"},"tool_events":{"id":"04a296a4-8b8d-4459-ada1-bc589294a382","type":"ToolEvents"},"toolbar":{"id":"5f3fb131-e855-42dd-8bb2-39f8366fe3cf","type":"Toolbar"},"x_range":{"id":"2dbf2280-6765-468d-bf61-d41a3de2e758","type":"DataRange1d"},"y_range":{"id":"d66e32f2-9e8a-423d-b68c-0c6b669cfd8c","type":"DataRange1d"}},"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function(v, i) {\n  return i / xs.length * 2 * 3.14159;\n});\n"},"id":"3756673d-8308-4c42-909a-db85daee4232","type":"CustomJSTransform"},{"attributes":{"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"}},"id":"5b570e0c-2917-42d8-93f7-676980c490af","type":"WheelZoomTool"},{"attributes":{"callback":null},"id":"2dbf2280-6765-468d-bf61-d41a3de2e758","type":"DataRange1d"},{"attributes":{"formatter":{"id":"441ac83a-adf0-45a1-9ede-f386203b0e1b","type":"BasicTickFormatter"},"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"},"ticker":{"id":"744b3d69-ddca-4d11-ab9d-715ee269092e","type":"BasicTicker"}},"id":"0d010602-1200-4404-9956-3f6a9cfa7f26","type":"LinearAxis"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function(v, i) {\n  return (i + 1) / xs.length * 2 * 3.14159;\n});\n"},"id":"caec11d8-861d-458a-981f-25cc7a624e65","type":"CustomJSTransform"},{"attributes":{"plot":{"id":"fa114ba7-c044-4f53-bd16-23fed9ee84d8","subtype":"Figure","type":"Plot"}},"id":"c16c21e5-9387-46da-ac03-703d2557fc8d","type":"SaveTool"},{"attributes":{},"id":"04a296a4-8b8d-4459-ada1-bc589294a382","type":"ToolEvents"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function() {\n  return 0;\n});\n"},"id":"40745b6e-fe0c-4a56-8272-872158899b98","type":"CustomJSTransform"},{"attributes":{},"id":"441ac83a-adf0-45a1-9ede-f386203b0e1b","type":"BasicTickFormatter"}],"root_ids":["fa114ba7-c044-4f53-bd16-23fed9ee84d8"]},"title":"Bokeh Application","version":"0.12.5"}};
            var render_items = [{"docid":"60c4e47d-aad2-4fbb-b6e4-96dec2e85b70","elementid":"47bb13ba-e6f0-4314-a098-e25e76841a94","modelid":"fa114ba7-c044-4f53-bd16-23fed9ee84d8"}];
            
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
        var cell = $(document.getElementById("47bb13ba-e6f0-4314-a098-e25e76841a94")).parents('.cell').data().cell;
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


<div class="output_html rendered_html output_subarea ">


    <div class="bk-root">
        <div class="bk-plotdiv" id="d6c7f627-618c-4463-8f84-4e02848ef62e"></div>
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
        var el = document.getElementById("d6c7f627-618c-4463-8f84-4e02848ef62e");
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
    };var element = document.getElementById("d6c7f627-618c-4463-8f84-4e02848ef62e");
    if (element == null) {
      console.log("Bokeh: ERROR: autoload.js configured with elementid 'd6c7f627-618c-4463-8f84-4e02848ef62e' but no matching script tag was found. ")
      return false;
    }
  
    var js_urls = [];
  
    var inline_js = [
      function(Bokeh) {
        (function() {
          var fn = function() {
            var docs_json = {"6d06bde6-226c-40b2-8dad-c0a1f84482fe":{"roots":{"references":[{"attributes":{},"id":"2cfa4fad-57ce-49a7-9ed9-a45224df0d8d","type":"ToolEvents"},{"attributes":{"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"}},"id":"2dc41755-47aa-4ed3-a90b-012c81706cda","type":"HelpTool"},{"attributes":{"overlay":{"id":"ae9febb9-eceb-4d26-8fcf-3440ac4f21bc","type":"BoxAnnotation"},"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"}},"id":"e5d39d41-dfe0-4c7f-87a9-09c298867a1e","type":"BoxZoomTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"ae9febb9-eceb-4d26-8fcf-3440ac4f21bc","type":"BoxAnnotation"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"aaf6870b-aa24-434f-a277-78355d07ce1f","type":"PanTool"},{"id":"2f03b09d-a7a2-4e25-a686-685938eb25b9","type":"WheelZoomTool"},{"id":"e5d39d41-dfe0-4c7f-87a9-09c298867a1e","type":"BoxZoomTool"},{"id":"ba366a59-3a24-4336-8ff7-9f3ff86966dc","type":"SaveTool"},{"id":"52699325-34cb-42c3-aada-b8ed140df461","type":"ResetTool"},{"id":"2dc41755-47aa-4ed3-a90b-012c81706cda","type":"HelpTool"}]},"id":"7663126b-4daf-404a-b0d2-67150597ca26","type":"Toolbar"},{"attributes":{"args":{"xx":{"id":"8dea63e5-e651-49a0-9d27-24809de34d3e","type":"DataRange1d"}},"v_func":"// Generated by CoffeeScript 1.11.1\nvar current, dx, total;\n\ndx = Math.max(1, Math.abs(xx.start - xx.end) / 2 / 1.5);\n\ntotal = xs.reduce(function(p, n) {\n  return p + n;\n});\n\ncurrent = ((Math.log(Math.abs(xx.start - xx.end) / 10)) % 1) * dx * 2 * 3.14159;\n\nreturn xs.map(function(v, i) {\n  if (i > 0) {\n    current += xs[i - 1] / total * 2 * 3.14159;\n  }\n  return current;\n});\n"},"id":"439ed071-1501-43e3-9d42-b059bbfd6f61","type":"CustomJSTransform"},{"attributes":{"args":{"xx":{"id":"8dea63e5-e651-49a0-9d27-24809de34d3e","type":"DataRange1d"}},"v_func":"// Generated by CoffeeScript 1.11.1\nvar dx;\n\ndx = .1 * Math.max(1, Math.abs(xx.start - xx.end) / 2 / 1.5);\n\nreturn xs.map(function(v) {\n  return dx;\n});\n"},"id":"e5f10b81-edac-4cfc-8ad5-e3f75121ab08","type":"CustomJSTransform"},{"attributes":{},"id":"295efad4-163b-49d2-839a-ba85eefd6295","type":"BasicTicker"},{"attributes":{"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"}},"id":"aaf6870b-aa24-434f-a277-78355d07ce1f","type":"PanTool"},{"attributes":{"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"}},"id":"52699325-34cb-42c3-aada-b8ed140df461","type":"ResetTool"},{"attributes":{"args":{"xx":{"id":"8dea63e5-e651-49a0-9d27-24809de34d3e","type":"DataRange1d"}},"v_func":"// Generated by CoffeeScript 1.11.1\nvar dx;\n\ndx = Math.max(1, Math.abs(xx.start - xx.end) / 2 / 1.5);\n\nreturn xs.map(function(v) {\n  return dx;\n});\n"},"id":"d075c9ae-b132-4d73-af04-c90e70bd58f4","type":"CustomJSTransform"},{"attributes":{"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"}},"id":"2f03b09d-a7a2-4e25-a686-685938eb25b9","type":"WheelZoomTool"},{"attributes":{"data_source":{"id":"e97b63bd-7349-4650-b296-c074182cd0dc","type":"ColumnDataSource"},"glyph":{"id":"9babb3b3-085f-47fd-9976-fbe4fd489e47","type":"AnnularWedge"},"hover_glyph":null,"muted_glyph":null},"id":"435214f0-e433-4e75-bacd-3ebe4aadd22b","type":"GlyphRenderer"},{"attributes":{"callback":null,"column_names":["x","index"],"data":{"index":["A","B","C","D"],"x":{"__ndarray__":"4p3C2aoID0AXcUASePkgQLh8EwxbXqI/SI5QdjnqF0A=","dtype":"float64","shape":[4]}}},"id":"e97b63bd-7349-4650-b296-c074182cd0dc","type":"ColumnDataSource"},{"attributes":{"below":[{"id":"d9731052-46a8-4cbd-857b-10e1173e60f5","type":"LinearAxis"}],"left":[{"id":"ef8ed4ec-964b-47ea-8f6c-b1f28eeb0444","type":"LinearAxis"}],"renderers":[{"id":"d9731052-46a8-4cbd-857b-10e1173e60f5","type":"LinearAxis"},{"id":"c402f4b6-8d9d-42d7-91a0-48e178b68276","type":"Grid"},{"id":"ef8ed4ec-964b-47ea-8f6c-b1f28eeb0444","type":"LinearAxis"},{"id":"22bd078a-5717-459f-90f3-b607c6a5fe59","type":"Grid"},{"id":"ae9febb9-eceb-4d26-8fcf-3440ac4f21bc","type":"BoxAnnotation"},{"id":"435214f0-e433-4e75-bacd-3ebe4aadd22b","type":"GlyphRenderer"}],"title":{"id":"df893a60-751e-4c14-ad6e-d4d86e4bd286","type":"Title"},"tool_events":{"id":"2cfa4fad-57ce-49a7-9ed9-a45224df0d8d","type":"ToolEvents"},"toolbar":{"id":"7663126b-4daf-404a-b0d2-67150597ca26","type":"Toolbar"},"x_range":{"id":"8dea63e5-e651-49a0-9d27-24809de34d3e","type":"DataRange1d"},"y_range":{"id":"f974839a-e980-47cb-9348-2290d72c34dd","type":"DataRange1d"}},"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"},{"attributes":{"args":{"source":{"id":"e97b63bd-7349-4650-b296-c074182cd0dc","type":"ColumnDataSource"}},"code":"\nsource.trigger('change');\ndx = Math.abs(cb_obj.start - cb_obj.end)/2\ncb_obj.start = dx\ncb_obj.end = -dx\n"},"id":"300d282c-cd2b-4ec5-a5b1-540c559f705d","type":"CustomJS"},{"attributes":{"dimension":1,"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"},"ticker":{"id":"295efad4-163b-49d2-839a-ba85eefd6295","type":"BasicTicker"}},"id":"22bd078a-5717-459f-90f3-b607c6a5fe59","type":"Grid"},{"attributes":{},"id":"e89057fc-c73b-4e5b-83df-8ddd94ac8f40","type":"BasicTickFormatter"},{"attributes":{"plot":null,"text":""},"id":"df893a60-751e-4c14-ad6e-d4d86e4bd286","type":"Title"},{"attributes":{},"id":"877adbfd-40a6-4838-ac0d-77426017d57a","type":"BasicTicker"},{"attributes":{"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"},"ticker":{"id":"877adbfd-40a6-4838-ac0d-77426017d57a","type":"BasicTicker"}},"id":"c402f4b6-8d9d-42d7-91a0-48e178b68276","type":"Grid"},{"attributes":{"callback":{"id":"300d282c-cd2b-4ec5-a5b1-540c559f705d","type":"CustomJS"}},"id":"f974839a-e980-47cb-9348-2290d72c34dd","type":"DataRange1d"},{"attributes":{},"id":"9375c7af-3003-44f6-915c-0bcc2b669363","type":"BasicTickFormatter"},{"attributes":{"end_angle":{"field":"x","transform":{"id":"439ed071-1501-43e3-9d42-b059bbfd6f61","type":"CustomJSTransform"},"units":"rad"},"fill_alpha":{"value":0.6},"inner_radius":{"field":"x","transform":{"id":"e5f10b81-edac-4cfc-8ad5-e3f75121ab08","type":"CustomJSTransform"},"units":"data"},"outer_radius":{"field":"x","transform":{"id":"d075c9ae-b132-4d73-af04-c90e70bd58f4","type":"CustomJSTransform"},"units":"data"},"start_angle":{"field":"x","transform":{"id":"6535483e-83ff-4924-b3a5-fac83e7266b8","type":"CustomJSTransform"},"units":"rad"},"x":{"value":0},"y":{"field":"x","transform":{"id":"c38632a6-158b-4530-ab78-c3674f9306f6","type":"CustomJSTransform"}}},"id":"9babb3b3-085f-47fd-9976-fbe4fd489e47","type":"AnnularWedge"},{"attributes":{"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"}},"id":"ba366a59-3a24-4336-8ff7-9f3ff86966dc","type":"SaveTool"},{"attributes":{"formatter":{"id":"9375c7af-3003-44f6-915c-0bcc2b669363","type":"BasicTickFormatter"},"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"},"ticker":{"id":"877adbfd-40a6-4838-ac0d-77426017d57a","type":"BasicTicker"}},"id":"d9731052-46a8-4cbd-857b-10e1173e60f5","type":"LinearAxis"},{"attributes":{"v_func":"// Generated by CoffeeScript 1.11.1\nreturn xs.map(function() {\n  return 0;\n});\n"},"id":"c38632a6-158b-4530-ab78-c3674f9306f6","type":"CustomJSTransform"},{"attributes":{"formatter":{"id":"e89057fc-c73b-4e5b-83df-8ddd94ac8f40","type":"BasicTickFormatter"},"plot":{"id":"4445939f-a8e9-4bf9-b983-be561ebdb53f","subtype":"Figure","type":"Plot"},"ticker":{"id":"295efad4-163b-49d2-839a-ba85eefd6295","type":"BasicTicker"}},"id":"ef8ed4ec-964b-47ea-8f6c-b1f28eeb0444","type":"LinearAxis"},{"attributes":{"callback":{"id":"300d282c-cd2b-4ec5-a5b1-540c559f705d","type":"CustomJS"}},"id":"8dea63e5-e651-49a0-9d27-24809de34d3e","type":"DataRange1d"},{"attributes":{"args":{"xx":{"id":"8dea63e5-e651-49a0-9d27-24809de34d3e","type":"DataRange1d"}},"v_func":"// Generated by CoffeeScript 1.11.1\nvar current, dx, total;\n\ndx = Math.max(1, Math.abs(xx.start - xx.end) / 2 / 1.5);\n\ntotal = xs.reduce(function(p, n) {\n  return p + n;\n});\n\ncurrent = ((Math.log(Math.abs(xx.start - xx.end) / 10)) % 1) * dx * 2 * 3.14159;\n\nreturn xs.map(function(v, i) {\n  current += v / total * 2 * 3.14159;\n  return current;\n});\n"},"id":"6535483e-83ff-4924-b3a5-fac83e7266b8","type":"CustomJSTransform"}],"root_ids":["4445939f-a8e9-4bf9-b983-be561ebdb53f"]},"title":"Bokeh Application","version":"0.12.5"}};
            var render_items = [{"docid":"6d06bde6-226c-40b2-8dad-c0a1f84482fe","elementid":"d6c7f627-618c-4463-8f84-4e02848ef62e","modelid":"4445939f-a8e9-4bf9-b983-be561ebdb53f"}];
            
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
        var cell = $(document.getElementById("d6c7f627-618c-4463-8f84-4e02848ef62e")).parents('.cell').data().cell;
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


