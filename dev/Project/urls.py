from django.conf.urls import include, url, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    #Automatically directs the page to index if it is a blank URL (127.0.0.1:8000)
    url(r'^$', 'Project.SecureWitness.views.index', name='index'),

    #Allows admin use through */admin
    url(r'^admin/', include(admin.site.urls)),

    #Allows access to */SecureWitness/urls (see SecureWitness/urls.py for urls
    url(r'^SecureWitness/',include('Project.SecureWitness.urls')),
]

#Allows for the access to the MEDIA_URL
if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            (r'media/(?P<path>.*)',
                             'serve',
                             {'document_root':settings.MEDIA_ROOT}), )
