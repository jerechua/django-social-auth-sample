from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'', include('social_auth_core.urls')),

    url(r'auth/', include('social_auth.urls')),
)
