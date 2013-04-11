from django.conf.urls import patterns, include, url

import views as core_views

urlpatterns = patterns('',
    url(r'^/?$', core_views.LandingView.as_view(), name='landing_page'),

    url(r'^login-err/?$', core_views.LoginError.as_view(), name='login_error'),
)