"""plotlyDashDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os.path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
# wagtaildocs_urls is the location from where document files will be served.
# This can be omitted if you do not intend to use Wagtail’s document management features.

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),

    # path('admin/', admin.site.urls), MAKING SPACE FOR THE WAGTAIL ADMIN
    path('', include('home.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    # re_path(r'', include('myapp.urls')), THIS IS Optional URL for including your own vanilla Django urls/views
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism

    re_path(r'', include(wagtail_urls)),
    # If you want Wagtail to handle the entire URL space including the root URL,
    # this can be replaced with: re_path(r'', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Note that this only works in development mode (DEBUG = True); in production, you will need to configure
# your web server to serve files from MEDIA_ROOT. For further details, see the Django documentation:
# https://docs.djangoproject.com/en/3.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development
# https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/

# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#
#     urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
#     urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
#     urlpatterns += [
#         path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico'))
#     ]
