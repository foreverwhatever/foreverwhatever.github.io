{% extends 'markdown.tpl' %}{%- block header scoped-%}
---
{{ resources.metadata | dump | load | yaml(default_flow_style=False)}}
layout: post
---
{{super()}}
{% endblock header %}{%- block data_javascript scoped %}
{% set div_id = uuid4() %}
<div id="{{ div_id }}"></div>
<div class="output_subarea output_javascript {{ extra_class }}">
<script type="text/javascript">
var element = $('#{{ div_id }}');
{{ output.data['application/javascript'] }}
</script>
</div>
{%- endblock -%}{% block stream %}
---
{{ output.text | indent }}
---
{% endblock stream %}
