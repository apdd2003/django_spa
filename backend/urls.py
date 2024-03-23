from django.contrib import admin
from django.template import RequestContext
from django.urls import path, re_path, include
from django.shortcuts import render


def render_react(request):
    return render(request, "index.html", )


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),
    re_path(r"^$", render_react),
    re_path(r"^(?:.*)/?$", render_react),
]
