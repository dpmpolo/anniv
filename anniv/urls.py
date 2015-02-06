from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import challenge.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anniv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^$', challenge.views.GoalInstanceView.as_view(),
        name='goalinstances-list',),
    url(r'^admin/', include(admin.site.urls)),
)

# TODO remove this eventually
urlpatterns += staticfiles_urlpatterns()
