from django.conf.urls import patterns, include, url
from django.contrib import admin
from rating import views
# import all model views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ftrating.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view(), name="index"),
    url(r'^admin/', include(admin.site.urls)),
)
