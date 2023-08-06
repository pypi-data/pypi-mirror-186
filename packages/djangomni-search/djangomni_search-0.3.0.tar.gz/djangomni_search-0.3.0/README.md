# djangomni-search

> Django Admin Site extension, that allows searching all entities from single
> field

## Installation

Please read the instructions carefully, extending Django Admin on this level
can go wrong very easily.

### 1. Pip your deps

Basically, install the dependency. You can use `poetry`, or any other package
manager.

```shell
pip install djangomni-search
```

### 2. Put `djangomni_search` into `INSTALLED_APPS`

It is important to put it on the top.

```python
INSTALLED_APPS = [
    'djangomni_search',
    'django.contrib.admin',
    'django.contrib.auth',
    '...',
]
```

### 3. Configure Admin Site

Now you will need to configure your Admin Site(s) to inherit from
`djangomni_search.admin.OmniSearchAdminSite`. If you're using the default
[AdminSite](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/), you must
[create a custom
one](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#overriding-default-admin-site).

```python
class SiteAdmin(OmniSearchAdminSite, AdminSite):
    ...
```

### 4. Extend your custom `base_site.html`

If you do not have a custom `base_site.html`, it should already work. In case you have done some customizations to your base site file, you will need to add one script to all pages in admin. This can be only done by
extending the base template.

```
{% block extrahead %}
{% if omni_search %}
  <link
    href="{% static 'djangomni-search/main.css' %}"
    rel="stylesheet"
    type="text/css"
  />
  <script
    data-config="{{omni_search}}"
    id="djangomni-search"
    src="{% static 'djangomni-search/main.js' %}"
  ></script>
{% endif %}
{% endblock %}
```

### 5. Configure autocomplete

The Omni Search looks for data using the [`autocomplete_fields`](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields) attribute of `ModelAdmin`. Configure it for all the models, that you want to search.

## Examples

Go to the [../dev-site](../dev-site) implementation, it serves as example page.
