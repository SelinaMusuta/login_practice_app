from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'django.contrib.auth.views.login'), #adding login url page
	  url(r'^login/$', 'django.contrib.auth.views.login'), #adding login url page
    # Examples:
    # url(r'^$', 'login_practice_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
