from django.conf.urls import patterns, include, url
from .views import Indexview

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myportfolio.views.home', name='home'),
    # url(r'^', include('portfolioapp.urls')),
    url(r'^$',Indexview.as_view(),name='index'),
 
)
