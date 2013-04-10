from django.conf.urls import patterns, include, url

import views as core_views

urlpatterns = patterns('',
    url(r'', core_views.LandingView.as_view(), name='landing_page'),
)