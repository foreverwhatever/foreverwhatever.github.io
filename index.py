# coding: utf-8

# <h1 class="text-center"><del><ins><code>forever whatever</code></ins></del><br/>
# <del><ins><code>whatever forever</code></ins></del></h1>
# 
# <hr># <h2 class="text-center"><del><code>code</code></del></h2>
# 
# <hr># <div class="container">
# <div class="row">
# {% for post in site.posts %}{% capture post_ %}
# ### [`{{post.title}}`]({{post.url}})
# 
# <del>{{post.description}}</del>
# 
# {% endcapture %}
# <div class="col col-md-6">{{post_ | markdownify}}</div>
# {% endfor %}
# </div>
# </div># <h2 class="text-center"><del><code>drawings</code></del></h2>
# 
# <hr>
# ---

if __name__ == '__main__':
    from _pages.index import sign
    sign()
