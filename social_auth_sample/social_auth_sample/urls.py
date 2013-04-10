from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth_core.urls')),
    url(r'^auth/?$', include('social_auth.urls')),
    # Examples:
    # url(r'^$', 'social_auth_sample.views.home', name='home'),
    # url(r'^social_auth_sample/', include('social_auth_sample.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
