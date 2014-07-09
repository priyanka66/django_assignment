from django.conf.urls import patterns, include, url
from todoapp import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'todoapp.views.home', name='home'),
    url(r'^alltasks/','todoapp.views.get_tasks',name='get_tasks'),
    url(r'^public/','todoapp.views.get_public_tasks',name='public_tasks'),
    url(r'^private/','todoapp.views.get_private_tasks',name='private_tasks')
)




