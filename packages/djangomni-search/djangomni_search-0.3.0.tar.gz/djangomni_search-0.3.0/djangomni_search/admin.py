import json
from functools import update_wrapper

from django.urls import path, reverse
from django.utils.html import format_html

from .views import OmniSearchModelView


class OmniSearchAdminSite:
    def get_omnisearch_model(self, app, model):
        cls = model['model']
        return {
            'app': {
                'name': str(app['name']),
                'label': str(app['app_label']),
                'url': str(app['app_url']),
            },
            'addUrl': str(model['add_url']),
            'adminUrl': str(model['admin_url']),
            'ident': str(cls._meta.model_name),
            'name': str(cls._meta.verbose_name_plural),
            'objectName': str(cls._meta.verbose_name),
        }

    def get_admin_model(self, model):
        return self._registry[model]

    def get_omnisearch_context(self, ctx):
        items = []
        for app in ctx['available_apps']:
            for model in app['models']:
                model_admin = self.get_admin_model(model['model'])
                if model_admin.search_fields:
                    items.append(self.get_omnisearch_model(app, model))
        if len(items) == 0:
            return None
        return {
            'homeUrl': reverse(f"{self.name}:index"),
            'models': items,
            'placeholder': str(ctx['site_header']),
            'publicUrl': self.site_url,
            'searchUrl': reverse(f"{self.name}:omnisearch"),
        }

    def omnisearch_view(self, request):
        return OmniSearchModelView.as_view(admin_site=self)(request)

    def each_context(self, request):
        ctx = super().each_context(request)
        ctx['omni_search'] = json.dumps(self.get_omnisearch_context(ctx))
        return ctx

    def get_urls(self):
        from django.urls import path

        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)
            wrapper.admin_site = self
            return update_wrapper(wrapper, view)
        return [
            path("omnisearch/", self.omnisearch_view, name="omnisearch"),
        ] + super().get_urls()


class OmniSearchDetailMixin():
    detail_route_ident = 'detail'
    detail_view_class = None

    def get_detail_route_name(self):
        app_name = self.model._meta.app_label
        model_name = self.model._meta.model_name
        return f"{app_name}_{model_name}_{self.detail_route_ident}"

    def get_detail_route_target(self):
        return f'{self.admin_site.name}:{self.get_detail_route_name()}'

    def get_urls(self):
        return [
            path(
                f'<pk>/{self.detail_route_ident}',
                self.admin_site.admin_view(
                    self.detail_view_class.as_view(
                        admin_site=self.admin_site,
                        extra_context={
                            'opts': self.model._meta,
                        },
                    )),
                name=self.get_detail_route_name(),
            ),
            *super().get_urls(),
        ]

    def detail_link(self, obj):
        url = reverse(f'{self.get_detail_route_target()}', args=[obj.pk])
        return format_html(f'<a href="{url}">{obj.pk}</a>')
