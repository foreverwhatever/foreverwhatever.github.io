{% extends 'full.tpl' %}

{%- block header scoped-%}
---
{{ resources.metadata | dump | load | yaml(default_flow_style=False)}}
---
{{super()}}
{%- endblock header -%}